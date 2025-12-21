# Managing Users

**Framework**: Device Management

Retrieve key information to effectively manage users across an organization.

#### Overview

Deployment of an organization’s owned assets to users’ owned devices requires registering those users for the location you’re managing. The provided API allows for asynchronous management of these users in the organization.

##### Retrieve Users

Before managing the users in the organization, the MDM client needs to determine what users are currently active. Making a request to [`Get Users`](get-users-4mwln.md) allows you to retrieve all users in the organization, and you can include an optional query parameter to return only active users. You can identify an active user by their unique `clientUserId`.

The following code shows an example of requesting an organization’s users:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/users' \ 
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "currentPageIndex": 0,
    "size": 3,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 1,
    "uId": "2049025000431439",
    "users": [
        {
            "clientUserId": "client-101",
            "email": "client-101@apple.com",
            "inviteCode": "46bc93ea3acd41e0a4919c02db0d7d3a",
            "status": "Registered"
        },
        {
            "clientUserId": "client-102",
            "email": "client-102@apple.com",
            "inviteCode": "d2ab1319ff6448f89bb1b0e010cf68e0",
            "status": "Registered"
        },
        {
            "clientUserId": "client-103",
            "email": "client-1031@apple.com",
            "status": "Retired"
        }
    ],
    "versionId": "021f10a0-7035-11eb-9f67-bd1df52e1e13"
}
```

##### Invite Users

You invite users by sending them an email with an invitation link. Accepting the invitation associates the user’s `appleId` with the managed location.

Use [`ServiceConfigResponse.Urls`](serviceconfigresponse/urls-data.dictionary.md) to retrieve the `invitationEmail` template URL, and then replace `%25inviteCode%25` with the user’s `inviteCode` from [`ResponseUser`](responseuser.md).

The following code shows an example of retrieving the URL from [`Service Config`](service-config.md):

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/service/config'
```

The code above results in a response like the following:

```javascript
{
    ...
    "urls": {
        "invitationEmail": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?inviteCode=%25inviteCode%25&mt=8",
        ...
    }
}
```

##### Interpret User States

A user has an `email` key and either an `idHash` or an `inviteCode` key, depending on the status. A registered user has an `inviteCode` because the system has created the user, but that user doesn’t have an associated Apple Account yet. An associated user has an `idHash` that uniquely identifies the user’s associated Apple Account. A retired user may have an `idHash` if the user had an associated `appleId` previously.

| State | Description |
| --- | --- |
| Registered | Indicates that the server has created the user, but the user doesn’t have an associated Apple Account yet. |
| Associated | Indicates that the user has an associated Apple Account. When the server associates a user with an Apple Account, it generates an `idHash` for that user. |
| Retired | Indicates that the server has retired the user. |
| Deleted | A legacy state that indicates that the server has retired the user and has associated that user’s Apple Account with a new user that shares the same `clientUserId`. |

##### Request Sizes

The size limits for a [`ManageUsersRequest`](manageusersrequest.md) are dynamic and can change without notice, so the MDM server should sync these every 5 minutes. These limits are in [`ServiceConfigResponse.Limits`](serviceconfigresponse/limits-data.dictionary.md).

The sole key that is specific to [`ManageUsersRequest`](manageusersrequest.md) is `maxUsers,` which represents the maximum number of unique users in a manage request.

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

##### Manage Users

Use [`ManageUsersRequest`](manageusersrequest.md) to asynchronously create, update, or retire users.

The following code shows an example of creating users to associate in the organization:

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/users/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {cToken}' \
--data-raw '{
    "users": [
        {
            "clientUserId": "client-1",
            "email": "client-1@apple.com"
        },
        {
            "clientUserId": "client-2",
            "email": "client-2@apple.com"
        }
    ]
}'
```

The code above results in a response like the following:

```javascript
{
    "eventId": "1039246b-97f5-4bdc-b3b6-78362dbf7652",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The following code shows an example of updating users in the organization:

```javascript
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/users/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {cToken}' \
--data-raw '{
    "users": [
        {
            "clientUserId": "client-3",
            "email": "client-3@apple.com"
        }
    ]
}'
```

The code above results in a response like the following:

```javascript
{
    "eventId": "79b658bc-f36c-4988-a6fe-a07fae196519",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

To view progress for your create, update, or retire event, make a request to [`Event Status`](events-status.md) using the unique identifier that the synchronous [`EventResponse`](eventresponse.md) returns, as the following code demonstrates:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=1039246b-97f5-4bdc-b3b6-78362dbf7652' \
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "eventStatus": "PENDING",
    "eventType": "CREATE",
    "numCompleted": 1,
    "numRequested": 2,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The following code shows the status of a complete create event:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/status?eventId=1039246b-97f5-4bdc-b3b6-78362dbf7652' \
--header 'Authorization: Bearer {cToken}'
```

The code above results in a response like the following:

```javascript
{
    "eventStatus": "COMPLETE",
    "eventType": "CREATE",
    "numCompleted": 2,
    "numRequested": 2,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

The [`StatusResponse`](statusresponse.md) returns as `PENDING`, `COMPLETE`, or `FAILED,` which represents the overall status of the asynchronous request.

##### Handle Notifications

For MDM clients that subscribe to `USER_MANAGEMENT` notifications in [`Client Config`](client-config-4szk1.md), the server sends incremental notifications as it manages users. For more information, see [`Subscribing to Notifications`](subscribing-to-notifications.md).

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
  Associate app and book purchases with users or devices.
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
  Manage devices and content across your organization using the new API version.
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.
- [Managing Assets](managing-assets.md)
  Retrieve key information to effectively manage assets across an organization’s users and devices.
- [Using Paginated Endpoints](using-paginated-endpoints.md)
  Manage paginated endpoints to efficiently work with large record sets.
- [Subscribing to Notifications](subscribing-to-notifications.md)
  Listen to notifications to keep track of the latest events for an organization.
- [Handling Error Responses](handling-error-responses.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managing-users)*