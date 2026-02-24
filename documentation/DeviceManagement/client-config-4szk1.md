# Client Config

**Framework**: Device Management  
**Kind**: httpRequest

Store client-specific information on the server.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
- [Managing Assets](managing-assets.md)
- [Managing Users](managing-users.md)
- [Subscribing to Notifications](subscribing-to-notifications.md)
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
{
    "mdmInfo": {
        "id": "522d5c43-44ca-4f7e-ba7a-53570cf60765",
        "name": "Apple Configurator 2",
        "metadata": "2.13.3"
    },
    "notificationAuthToken": "SUp3rS3Cr3t",
    "notificationUrl": "https://www.next.com/notification",
    "notificationTypes": [
        "ASSET_COUNT",
        "ASSET_MANAGEMENT",
        "USER_MANAGEMENT",
        "USER_ASSOCIATED"
    ]
}
```

**Response**:

```json
{
    "countryISO2ACode": "US",
    "defaultPlatform": "volumestore",
    "locationName": "PS01",
    "mdmInfo": {
        "id": "522d5c43-44ca-4f7e-ba7a-53570cf60765", 
        "name": "Apple Configurator 2", 
        "metadata": "2.13.3"
    },
    "notificationAuthToken": "SUp3rS3Cr3t",
    "notificationUrl": "https://www.next.com/notification",
    "subscribedNotificationTypes": [
        "ASSET_COUNT",
        "ASSET_MANAGEMENT",
        "USER_MANAGEMENT",
        "USER_ASSOCIATED"
    ],
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439",
    "websiteURL": "https://school.apple.com"
}
```

## Topics

### Request and Response
- [object ClientConfigRequest](clientconfigrequest.md)
  The request for the client configuration.
- [object ClientConfigResponse](clientconfigresponse.md)
  The response that contains the client configuration.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Read-Only
- [Client Config](client-config-71glv.md)
  Read client-specific information from the server.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/client/config`

## Request Body

missing

## See Also

- [Service Config](service-config.md)
  Provides the full list of web service URLs, notification types, request limits, and possible error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/client-config-4szk1)*