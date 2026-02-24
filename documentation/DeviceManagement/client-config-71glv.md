# Client Config

**Framework**: Device Management  
**Kind**: httpRequest

Read client-specific information from the server.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

##### Example Response

**Request**:

```None

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

### Response
- [object ClientConfigResponse](clientconfigresponse.md)
  The response that contains the client configuration.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/client/config`


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/client-config-71glv)*