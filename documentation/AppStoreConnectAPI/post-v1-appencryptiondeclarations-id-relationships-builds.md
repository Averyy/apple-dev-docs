# Assign builds to an app encryption declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Assign one or more builds to an app encryption declaration.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appEncryptionDeclarations/{id}/relationships/builds`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app encryption declaration resource ID from the [`List app encryption declarations`](get-v1-appencryptiondeclarations.md) response.

## See Also

- [Create an app encryption declaration](post-v1-appencryptiondeclarations.md)
  Add an app encryption delcaration for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appencryptiondeclarations-_id_-relationships-builds)*