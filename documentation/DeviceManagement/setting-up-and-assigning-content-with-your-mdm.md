# Setting up and assigning content with your MDM

**Framework**: Device Management

Distribute purchased licenses to managed users through your MDM server.

#### Overview

Distributing purchased licenses includes configuring an MDM client, registering users, purchasing content through Apple School Manager or Apple Business Manager, and assigning that content to users. Each step includes a `curl` example with the v2 API at `https://vpp.itunes.apple.com/mdm` and the corresponding response.

The API uses bearer token authentication. All v2 endpoints require an `Authorization: Bearer {sToken}` header, where the `sToken` is a location-based content token that a content manager downloads from Apple School Manager or Apple Business Manager. For details about how the token works, see [`Getting started with the management API`](getting-started-with-the-management-api.md).

#### Fetch the Service Configuration

Start by retrieving the service configuration. Send a GET request to `/v2/service/config` to discover request limits, available URLs, and notification settings for the location you manage.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/service/config' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "limits": {
        "maxAssets": 25,
        "maxUsers": 100,
        "maxNotificationLength": 512,
        "maxRevokeClientUserIds": 100,
        "maxClientUserIds": 1000,
        "maxSerialNumbers": 1000,
        "maxRevokeSerialNumbers": 100,
        "maxSubscriptions": 25,
        "maxSubscriptionClientUserIds": 1000,
        "maxMdmNameLength": 100,
        "maxMdmMetadataLength": 255,
        "maxMdmIdLength": 100
    },
    "urls": {
        "invitationEmail": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?inviteCode=%25inviteCode%25&mt=8"
    }
}
```

The `limits` object contains the maximum sizes for each request type. For example, `maxAssets` is the maximum number of unique assets in a single manage request, and `maxClientUserIds` is the maximum number of unique user identifiers per request. These limits are dynamic and change without notice, so sync them every 5 minutes.

#### Configure Your Mdm Client

After fetching the service configuration, register your MDM client with the server. Send a POST request to `/v2/client/config` to set your MDM identity and subscribe to notifications. The request body includes an `mdmInfo` object that identifies your MDM client, along with a notification URL, authentication token, and the notification types you want to receive.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/client/config' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "mdmInfo": {
        "id": "522d5c43-44ca-4f7e-ba7a-53570cf60765",
        "name": "My MDM Server",
        "metadata": "1.0.0"
    },
    "notificationUrl": "https://mdm.example.com/notifications",
    "notificationAuthToken": "example-auth-token-value",
    "notificationTypes": [
        "ASSET_MANAGEMENT",
        "USER_MANAGEMENT",
        "USER_ASSOCIATED",
        "ASSET_COUNT",
        "SUBSCRIPTION_MANAGEMENT",
        "SUBSCRIPTION_COUNT"
    ]
}'
```

The server responds with the following:

```json
{
    "mdmInfo": {
        "id": "522d5c43-44ca-4f7e-ba7a-53570cf60765",
        "name": "My MDM Server",
        "metadata": "1.0.0"
    },
    "notificationUrl": "https://mdm.example.com/notifications",
    "subscribedNotificationTypes": [
        "ASSET_MANAGEMENT",
        "USER_MANAGEMENT",
        "USER_ASSOCIATED",
        "ASSET_COUNT",
        "SUBSCRIPTION_MANAGEMENT",
        "SUBSCRIPTION_COUNT"
    ],
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The response echoes your configuration along with location information. Subscribe to all notification types so your MDM server receives real-time updates about asset count changes, assignment events, user state changes, and subscription activity.

> ❗ **Important**: The server sends a `TEST_NOTIFICATION` to your `notificationUrl` when you configure notifications. If delivery fails, the server rejects the configuration. Make sure your notification endpoint is reachable and returns an HTTP 2xx response before sending this request.

#### Register a User

With your MDM client configured, register a user by sending a POST request to `/v2/users/create`. Include a `users` array in the request body with each user’s `clientUserId` and `managedAppleId`.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/users/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "users": [
        {
            "clientUserId": "user-1",
            "managedAppleId": "jappleseed@appleschool.example.com"
        }
    ]
}'
```

The server processes this request asynchronously and returns an `eventId`.

```json
{
    "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

Poll the Events Status endpoint with that `eventId` to track the operation’s progress.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=e0def1f8-9158-4343-9c52-8dd32da50b9b' \
--header 'Authorization: Bearer {sToken}'
```

When the operation finishes, the status returns as `COMPLETE`.

```json
{
    "eventStatus": "COMPLETE",
    "eventType": "CREATE",
    "numCompleted": 1,
    "numRequested": 1,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

If your MDM client subscribes to `USER_MANAGEMENT` notifications, the server also sends a notification to your `notificationUrl`.

```json
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "CREATE",
        "users": [
            {
                "clientUserId": "user-1",
                "idHash": "rRVS8rlBrJjRqYwL8aNGDJG2CbU=",
                "status": "Associated"
            }
        ]
    },
    "notificationId": "4c0bbb9b-d5a6-4860-83ef-5cf362783c1e",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The user’s status is `Associated` because you provided a `managedAppleId`, which allows the server to associate the user with a Managed Apple Account immediately. Verify the user’s state by querying the Get Users endpoint.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/users?clientUserId=user-1' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "currentPageIndex": 0,
    "size": 1,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "users": [
        {
            "clientUserId": "user-1",
            "idHash": "rRVS8rlBrJjRqYwL8aNGDJG2CbU=",
            "status": "Associated"
        }
    ],
    "versionId": "021f10a0-7035-11eb-9f67-bd1df52e1e13"
}
```

#### Purchase Content Through Your Management Portal

With a registered user in place, the next step is purchasing content. A content manager uses the Apple School Manager or Apple Business Manager portal to purchase licenses for the organization. In this walkthrough, the content manager purchases the following:

- An app — Pages (Adam ID `361309726`)
- A subscription — An auto-renewable subscription (Adam ID `67890`) belonging to Pages (parent Adam ID `361309726`)

As each purchase completes, the server sends count notifications to the MDM’s `notificationUrl`. For the app purchase, your MDM server receives an `ASSET_COUNT` notification.

```json
{
    "notification": {
        "adamId": "361309726",
        "countDelta": 25,
        "pricingParam": "STDQ"
    },
    "notificationId": "4a7801be-53f0-42e1-9505-81c0d1dc9da3",
    "notificationType": "ASSET_COUNT",
    "uId": "2049025000431439"
}
```

The `countDelta` field indicates how many licenses were added. For the subscription, the server sends a `SUBSCRIPTION_COUNT` notification with a `counts` object containing `available` and `total` breakdowns by renewing and expiring state. For the full notification format, see [`Subscribing to notifications`](subscribing-to-notifications.md).

#### Verify Asset Inventory

After the content manager completes the purchases, verify that your organization’s inventory reflects the new licenses.

Query the app inventory by sending a GET request to `/v2/assets` with the `adamId` for Pages.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assets?adamId=361309726' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "assets": [
        {
            "adamId": "361309726",
            "assignedCount": 0,
            "availableCount": 25,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 25
        }
    ],
    "currentPageIndex": 0,
    "size": 1,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "versionId": "70e8c740-514c-11eb-bb63-a90b882fcd52"
}
```

The `availableCount` of 25 confirms that you can assign the purchased licenses.

Query the subscription inventory by sending a GET request to `/v2/subscriptions` with the `parentAdamId`.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/subscriptions?parentAdamId=361309726' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "subscriptions": [
        {
            "parentAdamId": 361309726,
            "adamId": 67890,
            "status": "ACTIVE",
            "periodEndDate": "2027-01-15",
            "counts": {
                "assigned": {
                    "renewing": 0,
                    "expiring": 0
                },
                "available": {
                    "renewing": 25,
                    "expiring": 0
                },
                "total": {
                    "renewing": 25,
                    "expiring": 0
                }
            }
        }
    ],
    "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
    "uId": "2049025000431439",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "versionId": "3b4b51d3-07f0-5711-bf45-b48df0fec669"
}
```

The subscription response breaks down seat counts by renewal state. All 25 seats are available and set to renew at the end of each billing period. For more information about how renewal states affect seat allocation, see [`Managing subscriptions`](managing-subscriptions.md).

#### Assign the App to the User

With inventory confirmed, assign the app to your registered user. Send a POST request to `/v2/assets/associate` with the asset and user details.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/assets/associate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "assets": [
        {
            "adamId": "361309726",
            "pricingParam": "STDQ"
        }
    ],
    "clientUserIds": [
        "user-1"
    ]
}'
```

The server processes this request asynchronously and returns an `eventId`.

```json
{
    "eventId": "954910a8-3d9c-4fde-948d-253e5aef431a",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

Poll the Events Status endpoint to confirm the assignment completes.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=954910a8-3d9c-4fde-948d-253e5aef431a' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "eventStatus": "COMPLETE",
    "eventType": "ASSOCIATE",
    "numCompleted": 1,
    "numRequested": 1,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The server also sends an `ASSET_MANAGEMENT` notification with the assignment details.

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": "361309726",
                "clientUserId": "user-1",
                "pricingParam": "STDQ"
            }
        ],
        "eventId": "954910a8-3d9c-4fde-948d-253e5aef431a",
        "result": "SUCCESS",
        "type": "ASSOCIATE"
    },
    "notificationId": "ba8bbb23-44c2-44f6-a928-eff6ba5ffac3",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

Verify the assignment by querying the Get Assignments endpoint.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments?adamId=361309726&clientUserId=user-1' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "assignments": [
        {
            "adamId": "361309726",
            "clientUserId": "user-1",
            "pricingParam": "STDQ"
        }
    ],
    "currentPageIndex": 0,
    "size": 1,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "versionId": "ef149b10-55c7-11eb-a8a1-490feefbbca0"
}
```

#### Assign the Subscription to the User

Finally, assign the subscription to the user. Send a POST request to `/v2/subscriptions/associate` with the subscription Adam ID, the user’s identifier, and the `renewing` flag set to `true` so the seat auto-renews at the end of each billing period.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/associate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {sToken}' \
--data-raw '{
    "adamIds": [67890],
    "clientUserIds": ["user-1"],
    "renewing": true
}'
```

The server returns an `eventId`.

```json
{
    "eventId": "a1b2c3d4-5e6f-7a8b-9c0d-e1f2a3b4c5d6",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

Poll the Events Status endpoint to confirm the assignment completes.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=a1b2c3d4-5e6f-7a8b-9c0d-e1f2a3b4c5d6' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "eventStatus": "COMPLETE",
    "eventType": "ASSOCIATE",
    "numCompleted": 1,
    "numRequested": 1,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

Verify the subscription assignment by querying the Get Subscription Assignments endpoint.

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/assignments?adamId=67890&clientUserId=user-1' \
--header 'Authorization: Bearer {sToken}'
```

The server responds with the following:

```json
{
    "assignments": [
        {
            "adamId": 67890,
            "clientUserId": "user-1",
            "renewing": true
        }
    ],
    "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
    "uId": "2049025000431439",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "versionId": "ab290ee7-02c1-5ba7-aa0a-652bd6e595bc"
}
```

The `renewing` field confirms that the assigned seat auto-renews. For information about assigning expiring seats, deferred disassociation, and managing subscription administrators, see [`Managing subscriptions`](managing-subscriptions.md).

## See Also

- [Managing assets](managing-assets.md)
  Assign and revoke app and book licenses across your organization.
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.
- [Managing users](managing-users.md)
  Register and manage users for your organization’s managed location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/setting-up-and-assigning-content-with-your-mdm)*