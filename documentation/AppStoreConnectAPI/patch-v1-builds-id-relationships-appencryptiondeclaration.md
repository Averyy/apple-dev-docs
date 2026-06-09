# Assign the app encryption declaration for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Assign an app encryption declaration to a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/appEncryptionDeclaration`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Modify a build](patch-v1-builds-_id_.md)
  Expire a build or change its encryption exemption setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-builds-_id_-relationships-appencryptiondeclaration)*