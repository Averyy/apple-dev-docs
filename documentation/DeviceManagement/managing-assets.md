# Managing Assets

**Framework**: Device Management

Retrieve key information to effectively manage assets across an organization’s users and devices.

#### Overview

Assets are the apps and books that an organization owns. The Manage Assets endpoints allow for asynchronous management of these assets to users and devices with mobile device management (MDM) software.

##### Retrieve Asset Information

Before managing the assets in an organization, you need to retrieve all of the assets that the organization owns by making a request to [`Get Assets`](get-assets-4ski1.md).

The following code shows an example of requesting an organization’s assets:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assets' \ 
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "assets": [
        {
            "adamId": "408709785",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "377298193",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "361309726",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "361304891",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        },
        {
            "adamId": "361285480",
            "assignedCount": 5000,
            "availableCount": 10000,
            "deviceAssignable": true,
            "pricingParam": "STDQ",
            "productType": "App",
            "retiredCount": 0,
            "revocable": true,
            "supportedPlatforms": ["iOS"],
            "totalCount": 15000
        }
    ],
    "currentPageIndex": 0,
    "size": 5,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "versionId": "70e8c740-514c-11eb-bb63-a90b882fcd52"
}
```

You can identify assets by the unique pair of store identifier and quality properties in `RequestAsset`. Assets in the [`GetAssetsResponse`](getassetsresponse.md) have additional fields regarding quantity and assignability in [`ResponseAsset`](responseasset.md). For pagination response fields, see [`Using Paginated Endpoints`](using-paginated-endpoints.md).

##### Retrieve Assignments

Making a request to [`Get Assignments`](get-assignments-9wv1e.md) allows you to retrieve all active asset assignments for the organization.

The following code shows an example of retrieving an organization’s assignments:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments' 
\ --header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "assignments": [
        {
            "adamId": "408709785",
            "serialNumber": "443d8def-f14b-4422-9997-75c83f595c24",
            "pricingParam": "STDQ"
        },
        {
            "adamId": "377298193",
            "serialNumber": "443d8def-f14b-4422-9997-75c83f595c24",
            "pricingParam": "STDQ"
        },
        {
            "adamId": "361309726",
            "serialNumber": "443d8def-f14b-4422-9997-75c83f595c24",
            "pricingParam": "STDQ"
        },
        {
            "adamId": "361304891",
            "serialNumber": "443d8def-f14b-4422-9997-75c83f595c24",
            "pricingParam": "STDQ"
        },
        {
            "adamId": "361285480",
            "serialNumber": "443d8def-f14b-4422-9997-75c83f595c24",
            "pricingParam": "STDQ"
        },
        ...
    ],
    "currentPageIndex": 0,
    "size": 999,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "versionId": "ef149b10-55c7-11eb-a8a1-490feefbbca0"
}
```

You can assign an asset to either a user or a device. For all other response fields, see [`GetAssignmentsResponse`](getassignmentsresponse.md) and [`Using Paginated Endpoints`](using-paginated-endpoints.md).

##### Request Sizes

The size limits for a [`ManageAssetsRequest`](manageassetsrequest.md) and [`RevokeAssetsRequest`](revokeassetsrequest.md) are dynamic and can change without notice, so the MDM server should sync these every 5 minutes. These limits are in [`ServiceConfigResponse.Limits`](serviceconfigresponse/limits-data.dictionary.md).

The following keys are specific to [`ManageAssetsRequest`](manageassetsrequest.md):

- `maxAssets` - The maximum number of unique assets in a manage request
- `maxClientUserIds` - The maximum number of unique user identifiers in a manage request
- `maxSerialNumbers` - The maximum number of unique device identifiers in a manage request

The following keys are specific to [`RevokeAssetsRequest`](revokeassetsrequest.md):

- `maxRevokeClientUserIds` - The maximum number of unique user identifiers in a revoke request
- `maxRevokeSerialNumbers` - The maximum number of unique serial numbers in a revoke request

The following code shows an example of getting request limits from [`Service Config`](service-config.md):

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/service/config'
```

The code above results in a response like the following:

```javascript
{
    ...
    "limits": {
        "maxAssets": 25,
        "maxUsers": 100,
        "maxNotificationLength": 512,
        "maxRevokeClientUserIds": 100,
        "maxClientUserIds": 1000,
        "maxSerialNumbers": 1000,
        "maxRevokeSerialNumbers": 100,
        "maxMdmNameLength": 100,
        "maxMdmMetadataLength": 255,
        "maxMdmIdLength": 100
    },
    ...
}
```

##### Assign Assets

Use [`ManageAssetsRequest`](manageassetsrequest.md) to asynchronously associate or disassociate assets with users and devices.

The following code shows an example of disassociating assets from currently assigned users and devices:

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/assets/disassociate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {cToken}' \
--data-raw '{
    "assets": [
      {
        "adamId": "408709785"
      },
      {
        "adamId": "377298193"
      }
    ],
     "clientUserIds": [
      "client-1",
      "client-2",
      "client-3",
      "client-4"
    ],
    "serialNumbers": [
      "serial-1",
      "serial-2",
      "serial-3",
      "serial-4"
    ]
}'
```

The code above results in a response like the following:

```javascript
{
    "eventId": "9f418433-09c5-41e8-abc6-9016ac104d5b",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

You can then associate those assets to new users and devices.

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/assets/associate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {cToken}' \
--data-raw '{
    "assets": [
      {
        "adamId": "408709785"
      },
      {
        "adamId": "377298193"
      }
    ],
     "clientUserIds": [
      "client-1",
      "client-2",
      "client-3",
      "client-4"
    ],
    "serialNumbers": [
      "serial-1",
      "serial-2",
      "serial-3",
      "serial-4"
    ]
}'
```

The code above results in a response like the following:

```javascript
{
    "eventId": "954910a8-3d9c-4fde-948d-253e5aef431a",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

Use [`RevokeAssetsRequest`](revokeassetsrequest.md) to disassociate all assigned revocable assets from users and devices, as the following code shows:

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/assets/revoke' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {cToken}' \
--data-raw '{
     "clientUserIds": [
      "client-1",
      "client-2",
      "client-3",
      "client-4"
    ],
    "serialNumbers": [
      "serial-1",
      "serial-2",
      "serial-3",
      "serial-4"
    ]
}'
```

The code above results in a response like the following:

```javascript
{
    "eventId": "5c2113e7-bf12-458a-9a6d-55bd75904392",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

To view event progress, make a request to [`Event Status`](events-status.md) using the unique identifier that the synchronous [`EventResponse`](eventresponse.md) returns, as the following code demonstrates:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=29ddf6fe-8b2e-4c3f-91d9-aea3c63e4235' \
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "eventStatus": "PENDING",
    "eventType": "ASSOCIATE",
    "numCompleted": 8,
    "numRequested": 16,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The following code shows the status of a failed assignment event:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=a8e0edbf-bfc2-405f-92bd-08d6d72e7a1d' \
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "eventStatus": "FAILED",
    "eventType": "ASSOCIATE",
    "failures": [
        {
            "errorInfo": {
                "clientUserIds": [
                    "client-4"
                ]
            },
            "errorNumber": 9609,
            "errorMessage": "Registered user not found"
        },
    ],
    "numCompleted": 14,
    "numRequested": 16,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The following code shows getting the status of a complete assignment event:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=a2c5dfce-7e60-47f6-b19a-6c3abf7d9c7d' \
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "eventStatus": "COMPLETE",
    "eventType": "ASSOCIATE",
    "numCompleted": 16,
    "numRequested": 16,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The [`StatusResponse`](statusresponse.md) returns as `PENDING`, `COMPLETE`, or `FAILED,` which represents the overall status of the asynchronous request.

##### Handle Notifications

For MDM clients that subscribe to `ASSET_MANAGEMENT` notifications in [`Client Config`](client-config-4szk1.md), the server sends incremental notifications as it makes assignments. For more information, see [`Subscribing to Notifications`](subscribing-to-notifications.md).

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
  Associate app and book purchases with users or devices.
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
  Manage devices and content across your organization using the new API version.
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.
- [Managing Users](managing-users.md)
  Retrieve key information to effectively manage users across an organization.
- [Using Paginated Endpoints](using-paginated-endpoints.md)
  Manage paginated endpoints to efficiently work with large record sets.
- [Subscribing to Notifications](subscribing-to-notifications.md)
  Listen to notifications to keep track of the latest events for an organization.
- [Handling Error Responses](handling-error-responses.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-assets)*