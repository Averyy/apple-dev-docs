# Service Config

**Framework**: Device Management  
**Kind**: httpRequest

Provides the full list of web service URLs, notification types, request limits, and possible error codes.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Managing Users](managing-users.md)
- [Getting App and Book Information (Legacy)](getting-app-and-book-information-legacy.md)
- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
- [Managing Assets](managing-assets.md)
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)

#### Discussion

##### Example Response

**Request**:

```None

```

**Response**:

```json
{
    "errorCodes": [
        {
            "errorMessage": "Login required.",
            "errorNumber": 9601
        },
        {
            "errorMessage": "Invalid argument.",
            "errorNumber": 9602
        },
        {
            "errorMessage": "Internal error.",
            "errorNumber": 9603
        },
        {
            "errorMessage": "Unable to find the registered user.",
            "errorNumber": 9609
        },
        {
            "errorMessage": "The token has expired. You need to generate a new token online using your organization's account at either school.apple.com or business.apple.com.",
            "errorNumber": 9621
        },
        {
            "errorMessage": "The server has revoked the sToken.",
            "errorNumber": 9625
        },
        {
            "errorMessage": "Service removed.",
            "errorNumber": 9634
        },
        {
            "errorMessage": "There are too many recent requests. Try again momentarily.",
            "errorNumber": 9646
        },
        {
            "errorMessage": "The provided page index must be greater than 0, and less than the total number of pages.",
            "errorNumber": 9650
        },
        {
            "errorMessage": "Max assets limit on request has been passed, please stay within given limit.",
            "errorNumber": 9700
        },
        {
            "errorMessage": "Max clientUserIds limit on request has been passed, please stay within given limit.",
            "errorNumber": 9701
        },
        {
            "errorMessage": "Max serialNumbers limit on request has been passed, please stay within given limit.",
            "errorNumber": 9702
        },
        {
            "errorMessage": "Duplicate assets found in request, please send unique assets.",
            "errorNumber": 9703
        },
        {
            "errorMessage": "Duplicate clientUserIds found in request, please send unique clients.",
            "errorNumber": 9704
        },
        {
            "errorMessage": "Duplicate serialNumbers found in request, please send unique serials.",
            "errorNumber": 9705
        },
        {
            "errorMessage": "Asset in request is not revocable, please send revocable assets.",
            "errorNumber": 9706
        },
        {
            "errorMessage": "Asset in request is not device assignable, please send device assignable assets.",
            "errorNumber": 9707
        },
        {
            "errorMessage": "EventId could not be found.",
            "errorNumber": 9708
        },
        {
            "errorMessage": "There are not enough licenses for this app or book available to assign to the selected group.",
            "errorNumber": 9709
        },
        {
            "errorMessage": "Both the notification URL and the authentication token are necessary.",
            "errorNumber": 9710
        },
        {
            "errorMessage": "Either the notification URL or the authentication token exceeds its maximum length. Change the request to stay within the specified limit.",
            "errorNumber": 9711
        },
        {
            "errorMessage": "The provided notification URL must be a valid URL and use HTTPS as the protocol.",
            "errorNumber": 9712
        },
        {
            "errorMessage": "The MDM metadata exceeds the maximum length. Change the request to stay within the specified limit.",
            "errorNumber": 9713
        },
        {
            "errorMessage": "The number of users exceeds the maximum. Change the request to stay within the specified limit.",
            "errorNumber": 9714
        },
        {
            "errorMessage": "This request contains duplicate users. Change the request to send unique users.",
            "errorNumber": 9715
        },
        {
            "errorMessage": "A registered user already exists with the specified clientUserId.",
            "errorNumber": 9716
        },
        {
            "errorMessage": "This request contains an invalid email address. Change the request to send valid email addresses.",
            "errorNumber": 9717
        },
        {
            "errorMessage": "This request doesn't contain an asset, which is a required argument. Change the request to provide an asset.",
            "errorNumber": 9718
        },
        {
            "errorMessage": "Either clientUserIds or serialNumbers are required arguments. Change the request to provide assignable users and devices.",
            "errorNumber": 9719
        },
        {
            "errorMessage": "Users are a required argument. Change the request to provide a user.",
            "errorNumber": 9720
        },
        {
            "errorMessage": "This request contains an invalid version ID. Change the request to send the version ID from the read APIs.",
            "errorNumber": 9721
        },
        {
            "errorMessage": "This request contains an invalid authorization header. Change the request to send an authorization header that matches the format 'Bearer {sToken}'.",
            "errorNumber": 9722
        },
        {
            "errorMessage": "You must provide an MDM name, ID, and metadata when setting the MDM information.",
            "errorNumber": 9723
        },
        {
            "errorMessage": "The MDM ID exceeds the maximum length. Change the request to stay within the specified limit.",
            "errorNumber": 9724
        },
        {
            "errorMessage": "The MDM name exceeds the maximum length. Change the request to stay within the specified limit.",
            "errorNumber": 9725
        },
        {
            "errorMessage": "This request contains an unsupported HTTP method for the requested endpoint.",
            "errorNumber": 9726
        },
        {
            "errorMessage": "This request contains an unsupported Content-Type for the requested endpoint.",
            "errorNumber": 9727
        },
        {
            "errorMessage": "The provided notification URL is unreachable.",
            "errorNumber": 9728
        }
    ],
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
    "notificationTypes": [
        "ASSET_MANAGEMENT",
        "USER_MANAGEMENT",
        "USER_ASSOCIATED",
        "ASSET_COUNT"
    ],
    "urls": {
        "invitationEmail": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?inviteCode=%25inviteCode%25&mt=8",
        "clientConfig": "https://vpp.itunes.apple.com/mdm/v2/client/config",
        "createUsers": "https://vpp.itunes.apple.com/mdm/v2/users/create",
        "getAssignments": "https://vpp.itunes.apple.com/mdm/v2/assignments",
        "revokeAssets": "https://vpp.itunes.apple.com/mdm/v2/assets/revoke",
        "contentMetadataLookup": "https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup",
        "getUsers": "https://vpp.itunes.apple.com/mdm/v2/users",
        "eventStatus": "https://vpp.itunes.apple.com/mdm/v2/status",
        "associateAssets": "https://vpp.itunes.apple.com/mdm/v2/assets/associate",
        "disassociateAssets": "https://vpp.itunes.apple.com/mdm/v2/assets/disassociate",
        "updateUsers": "https://vpp.itunes.apple.com/mdm/v2/users/update",
        "getAssets": "https://vpp.itunes.apple.com/mdm/v2/assets",
        "retireUsers": "https://vpp.itunes.apple.com/mdm/v2/users/retire"
    }
}
```

## Topics

### Response
- [object ServiceConfigResponse](serviceconfigresponse.md)
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/service/config`

## See Also

- [Client Config](client-config-4szk1.md)
  Store client-specific information on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/service-config)*