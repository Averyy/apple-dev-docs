# Get the app encryption declaration id for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the beta app encryption declaration resource ID associated with a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/appEncryptionDeclaration`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Read the build beta details information of a build](get-v1-builds-_id_-buildbetadetail.md)
  Get the beta test details for a specific build.
- [Get the build beta detail ID for a build](get-v1-builds-_id_-relationships-buildbetadetail.md)
- [Read the app encryption declaration of a build](get-v1-builds-_id_-appencryptiondeclaration.md)
  Read an app encryption declaration associated with a specific build.
- [List all beta build localizations of a build](get-v1-builds-_id_-betabuildlocalizations.md)
  Get a list of localized beta test information for a specific build.
- [List beta build localization IDs for a build](get-v1-builds-_id_-relationships-betabuildlocalizations.md)
- [List all diagnostic signatures for a build](get-v1-builds-_id_-diagnosticsignatures.md)
  List the aggregate backtrace signatures captured for a specific build.
- [List all icons for a build](get-v1-builds-_id_-icons.md)
  List all the icons for various platforms delivered with a build.
- [List icon IDs for a build](get-v1-builds-_id_-relationships-icons.md)
- [List diagnostic signature IDs for a build](get-v1-builds-_id_-relationships-diagnosticsignatures.md)
- [Get the App Store version ID for a build](get-v1-builds-_id_-relationships-appstoreversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-relationships-appencryptiondeclaration)*