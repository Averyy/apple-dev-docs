# Read the app information of a beta license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the app information for a specific beta license agreement.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaLicenseAgreements/{id}/app`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.

## See Also

- [List beta license agreements](get-v1-betalicenseagreements.md)
  Find and list beta license agreements for all apps.
- [Read beta license agreement information](get-v1-betalicenseagreements-_id_.md)
  Get a specific beta license agreement.
- [Get the app ID for a beta license agreement](get-v1-betalicenseagreements-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betalicenseagreements-_id_-app)*