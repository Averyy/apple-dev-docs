# Subscribing to Notifications

**Framework**: Device Management

Listen to notifications to keep track of the latest events for an organization.

#### Overview

Notifications make it easy to learn about changes to an organization’s assets, assignments, and users. Using notifications is the simplest way to keep track of the latest events for an organization, such as:

- Asset count events
- Asset management events
- User management events
- User-associated events

For information about subscribing to different notification types, see  [`ClientConfigRequest`](clientconfigrequest.md).

Each notification has these common fields:

| Response field | Description |
| --- | --- |
| `notificationId` | Each notification has a unique ID that you can use for deduping notifications that the server happens to send multiple times. |
| `notificationType` | The type of notification. You can use this to determine how to deserialize the notification value. |
| `notification` | Contains the JSON object with the changed data. Each notification type has a uniquely structured notification JSON object. |
| `uId` | The ID of the location for the notification. |

Notifications resemble the following:

```javascript
{
    "notification": {...},
    "notificationId": "01654971-0d81-467a-9e62-bf8e15e8dabd",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The server delivers notifications on a best-effort basis. The server attempts to deliver them 3 times within 1-5 minute(s) and without intervals. An HTTP 2xx response status from an MDM server indicates a successful notification delivery.

Notifications require a URL and an authentication token. The URL must use the HTTPS protocol, and the authentication token is in a [`bearer token format`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6750). See the [`ClientConfigRequest`](clientconfigrequest.md) for more details about these parameters.

> ❗ **Important**:  The server sends a test notification of type TEST_NOTIFICATION when configuring notifications with [`Client Config`](client-config-4szk1.md). If delivery fails, the system rejects the configuration.

 The server sends a test notification of type TEST_NOTIFICATION when configuring notifications with [`Client Config`](client-config-4szk1.md). If delivery fails, the system rejects the configuration.

The test notification has the following format:

```javascript
{
    "notification": {},
    "notificationId": "792e327f-63ea-4658-9aec-f16f4327e3a8",
    "notificationType": "TEST_NOTIFICATION",
    "uId": "2049025000431439"
}
```

##### Update Asset Counts

Update total asset counts upon receiving an `ASSET_COUNT` notification type that the server sends when:

- A user buys an asset
- A user transfers an asset between locations
- A user refunds an asset

The notifications have the following format:

```javascript
{
    "notification": {
        "adamId": "408709785",
        "countDelta": -12,
        "pricingParam": "STDQ"
    },
    "notificationId": "4a7801be-53f0-42e1-9505-81c0d1dc9da3",
    "notificationType": "ASSET_COUNT",
    "uId": "2049025000431439"
}
```

The `adamId` and `pricingParam` pair represent the [`Asset`](asset.md) with the count that is changing, and the `countDelta` represents the amount that the count is changing by. The amount can be a positive or a negative number depending on whether the count is increasing or decreasing.

##### Track Assignments

Track assignments upon receiving an `ASSET_MANAGEMENT` notification type that the server sends when it associates or disassociates an asset. The body of the notification contains a list of [`Assignment`](assignment.md) objects.

The assignment notifications for associations have the following format:

```javascript
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "97c42a74-c30e-4172-a65f-6e5a5ba3d477"
            },
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "495622d3-76f1-4fd3-8647-3f0365159170"
            },
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "eabcbb89-8213-4185-afb4-30cae931ea37"
            },
            ...
        ],
        "eventId": "87cbc650-16cc-4f9e-a833-e622f377a9f7",
        "result": "SUCCESS",
        "type": "ASSOCIATE"
    },
    "notificationId": "ba8bbb23-44c2-44f6-a928-eff6ba5ffac3",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The assignment notifications for disassociations have the following format:

```javascript
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "clientUserId": "client-100",
                "pricingParam": "STDQ"
            }
        ],
        "eventId": "4bd7371e-6482-4933-8e97-c29f25b7f5f5",
        "result": "SUCCESS",
        "type": "DISASSOCIATE"
    },
    "notificationId": "545e1f6f-ca8b-4e6c-98fe-a7ac3ef63b29",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The assignment notifications for revoke calls have the following format:

```swift
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "clientUserId": "client-100",
                "pricingParam": "STDQ"
            },
            {
                "adamId": "329103948",
                "clientUserId": "client-100",
                "pricingParam": "STDQ"
            }

        ],
        "eventId": "4bd7371e-6482-4933-8e97-c29f25b7f5f5",
        "result": "SUCCESS",
        "type": "REVOKE"
    },
    "notificationId": "545e1f6f-ca8b-4e6c-98fe-a7ac3ef63b28",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}

```

##### Track User Events

Track users upon receiving a `USER_MANAGEMENT` notification type that the server sends when:

- Creating a user
- Updating a user
- Retiring a user

The notifications for creating a user have the following format:

```javascript
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "CREATE",
        "users": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Registered"
            }
        ]
    },
    "notificationId": "4c0bbb9b-d5a6-4860-83ef-5cf362783c1e",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}
```

The notifications for updating a user have the following format:

```swift
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "UPDATE",
        "users": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Registered"
            }
        ]
    },
    "notificationId": "4c0bbb9b-d5a6-4860-83ef-5cf362783c1e",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}

```

The notifications for retiring a user have the following format:

```swift
{
    "notification": {
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "RETIRE",
        "users": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Retired"
            }
        ]
    },
    "notificationId": "4c0bbb9b-d5a6-4860-83ef-5cf362783c1e",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}

```

##### Track User Associations

Track users upon receiving a USER_ASSOCIATED notification type that the server sends when a user accepts an invite.

The notifications have the following format:

```javascript
{
    "notification": {
        "associatedUsers": [
            {
                "clientUserId": "client-100",
                "email": "client-100@apple.com",
                "idHash": "leSKk3IaE2vk2KLmv2k3/200D3=",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Associated"
            }
        ]
    },
    "notificationId": "90b83144-fb93-4837-9c52-0ae147bdc421",
    "notificationType": "USER_ASSOCIATED",
    "uId": "2049025000431439"
}
```

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
  Associate app and book purchases with users or devices.
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
  Manage devices and content across your organization using the new API version.
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.
- [Managing Assets](managing-assets.md)
  Retrieve key information to effectively manage assets across an organization’s users and devices.
- [Managing Users](managing-users.md)
  Retrieve key information to effectively manage users across an organization.
- [Using Paginated Endpoints](using-paginated-endpoints.md)
  Manage paginated endpoints to efficiently work with large record sets.
- [Handling Error Responses](handling-error-responses.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/subscribing-to-notifications)*