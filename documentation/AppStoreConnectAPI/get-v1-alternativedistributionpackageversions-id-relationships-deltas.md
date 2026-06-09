# List delta ids

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all delta Ids for a specific alternative distribution package version.

**Availability**:
- App Store Connect API 3.6+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/{id}/relationships/deltas`

## Parameters

- `limit` (integer): The maximum number of alternative distribution package delta resource identifiers to return.

## See Also

- [Read Information for an Alternative Distribution Package Version](get-v1-alternativedistributionpackageversions-_id_.md)
  Get detail information about a specific alternative distribution package version.
- [Read Version Information for an Alternative Distribution Package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.
- [List Deltas Information](get-v1-alternativedistributionpackageversions-_id_-deltas.md)
  List deltas for a specific alternative distribution package version.
- [List Variants Information](get-v1-alternativedistributionpackageversions-_id_-variants.md)
  List variants for specific alternative distribution package version.
- [List variant ids information](get-v1-alternativedistributionpackageversions-_id_-relationships-variants.md)
  List variant Ids for specific alternative distribution package version.
- [Read version ids for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-relationships-versions.md)
  Get version IDs about a specific alternative distribution package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributionpackageversions-_id_-relationships-deltas)*