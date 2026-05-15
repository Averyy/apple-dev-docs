# Assign Builds to an App Encryption Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Assign one or more builds to an app encryption declaration.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}/relationships/builds`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the App Encryption Declarations resource ID from the [`List App Encryption Declarations`](get-v1-appencryptiondeclarations.md) response.

## See Also

- [Create an App Encryption Declarations](post-v1-appencryptiondeclarations.md)
  Add an app encryption delcaration for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appencryptiondeclarations-_id_-relationships-builds)*