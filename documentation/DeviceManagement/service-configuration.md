# Service Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Provides the full list of web service URLs and a list of possible error numbers.

**Availability**:
- VPP License Management 1.0+

#### Discussion

Clients should use this endpoint every 5 minutes to retrieve the list of service URLs, because the URLs may change. This endpoint exists to provide a level-of-service discovery, so service URLs can be changed in a transparent way.

##### Example Response

**Request**:

```None
{}
```

**Response**:

```json
{
  "clientConfigSrvUrl": "https://vpp.itunes.apple.com/mdm/VPPClientConfigSrv",
  "contentMetadataLookupUrl": "https://uclient-api.itunes.apple.com/WebObjects/MZStorePlatform.woa/wa/lookup",
  "editUserSrvUrl": "https://vpp.itunes.apple.com/mdm/editVPPUserSrv",
  "errorCodes": [
    {
      "errorMessage": "Missing required argument",
      "errorNumber": 9600
    },
    {
      "errorMessage": "Login required",
      "errorNumber": 9601
    },
    {
      "errorMessage": "Invalid argument",
      "errorNumber": 9602
    },
    {
      "errorMessage": "Internal error",
      "errorNumber": 9603
    },
    {
      "errorMessage": "Result not found",
      "errorNumber": 9604
    },
    {
      "errorMessage": "Account storefront incorrect",
      "errorNumber": 9605
    },
    {
      "errorMessage": "Error constructing token",
      "errorNumber": 9606
    },
    {
      "errorMessage": "License is irrevocable",
      "errorNumber": 9607
    },
    {
      "errorMessage": "Empty response from SharedData service",
      "errorNumber": 9608
    },
    {
      "errorMessage": "Registered user not found",
      "errorNumber": 9609
    },
    {
      "errorMessage": "License not found",
      "errorNumber": 9610
    },
    {
      "errorMessage": "Admin user not found",
      "errorNumber": 9611
    },
    {
      "errorMessage": "Failed to create claim job",
      "errorNumber": 9612
    },
    {
      "errorMessage": "Failed to create unclaim job",
      "errorNumber": 9613
    },
    {
      "errorMessage": "Invalid date format",
      "errorNumber": 9614
    },
    {
      "errorMessage": "OrgCountry not found",
      "errorNumber": 9615
    },
    {
      "errorMessage": "License already assigned",
      "errorNumber": 9616
    },
    {
      "errorMessage": "The URL has been moved. Please call VPPServiceConfigSrv to find the new URL.",
      "errorNumber": 9617
    },
    {
      "errorMessage": "The user has already been retired.",
      "errorNumber": 9618
    },
    {
      "errorMessage": "License not associated",
      "errorNumber": 9619
    },
    {
      "errorMessage": "The user has already been deleted.",
      "errorNumber": 9620
    },
    {
      "errorMessage": "The token has expired. You need to generate a new token online using your organization's account at https://vpp.itunes.apple.com.",
      "errorNumber": 9621
    },
    {
      "errorMessage": "Invalid authentication token",
      "errorNumber": 9622
    },
    {
      "errorMessage": "Invalid APN token",
      "errorNumber": 9623
    },
    {
      "errorMessage": "License was refunded and is no longer valid.",
      "errorNumber": 9624
    },
    {
      "errorMessage": "The sToken has been revoked",
      "errorNumber": 9625
    },
    {
      "errorMessage": "License already assigned to other user",
      "errorNumber": 9626
    },
    {
      "errorMessage": "License disassociation fail due to frequent reassociation",
      "errorNumber": 9627
    },
    {
      "errorMessage": "License not eligible for device assignment.",
      "errorNumber": 9628
    },
    {
      "errorMessage": "The sToken is inapplicable to batchToken",
      "errorNumber": 9629
    },
    {
      "errorMessage": "Too many recent identical calls were made to assign a license that failed due to license being already assigned to the user or device",
      "errorNumber": 9630
    },
    {
      "errorMessage": "Too many recent identical calls were made to assign a license that failed due to no license being being available.",
      "errorNumber": 9631
    },
    {
      "errorMessage": "Too many recent calls to manage licenses with identical requests",
      "errorNumber": 9632
    },
    {
      "errorMessage": "No batch data recovered for token.",
      "errorNumber": 9633
    },
    {
      "errorMessage": "Service removed.",
      "errorNumber": 9634
    },
    {
      "errorMessage": "Apple Account can't be associated with registered user.",
      "errorNumber": 9635
    },
    {
      "errorMessage": "No registered user found.",
      "errorNumber": 9636
    },
    {
      "errorMessage": "Facilitator operation not allowed.",
      "errorNumber": 9637
    },
    {
      "errorMessage": "Apple Account already associated to registered user.",
      "errorNumber": 9641
    },
    {
      "errorMessage": "Apple Account passed cannot be used at this time because it's a VPP manager and the iTunes Store account not yet created and such creation requires user to agree to Terms.",
      "errorNumber": 9642
    },
    {
      "errorMessage": "The license is currently locked for a pending transfer. Please try again.",
      "errorNumber": 9643
    },
    {
      "errorMessage": "Volume Purchase Program is currently in maintenance mode. Please try again later.",
      "errorNumber": 9644
    },
    {
      "errorMessage": "Too many recent requests. Please try again momentarily",
      "errorNumber": 9646
    }
  ],
  "getLicensesSrvUrl": "https://vpp.itunes.apple.com/mdm/getVPPLicensesSrv",
  "getUserSrvUrl": "https://vpp.itunes.apple.com/mdm/getVPPUserSrv",
  "getUsersSrvUrl": "https://vpp.itunes.apple.com/mdm/getVPPUsersSrv",
  "getVPPAssetsSrvUrl": "https://vpp.itunes.apple.com/mdm/getVPPAssetsSrv",
  "invitationEmailUrl": "https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?cc=us&inviteCode=%25inviteCode%25&mt=8",
  "manageVPPLicensesByAdamIdSrvUrl": "https://vpp.itunes.apple.com/mdm/manageVPPLicensesByAdamIdSrv",
  "maxBatchAssociateLicenseCount": 10,
  "maxBatchDisassociateLicenseCount": 10,
  "registerUserSrvUrl": "https://vpp.itunes.apple.com/mdm/registerVPPUserSrv",
  "retireUserSrvUrl": "https://vpp.itunes.apple.com/mdm/retireVPPUserSrv",
  "status": 0,
  "vppWebsiteUrl": "https://vpp.itunes.apple.com/"
}
```

## Topics

### Response
- [object VppServiceConfigResponse](vppserviceconfigresponse.md)
  The response with the service configuration.
### Product Metadata
- [Getting app and book information (Legacy)](getting-app-and-book-information-legacy.md)
  Use a web service to find details about apps and books to show to your users.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/VPPServiceConfigSrv`

## See Also

- [Client Configuration](client-configuration.md)
  Store client-specific information on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/service-configuration)*