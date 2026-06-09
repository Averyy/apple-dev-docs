# BetaAppClipInvocationCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request body.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BetaAppClipInvocationCreateRequest.Data
```

## Topics

### Objects
- [object BetaAppClipInvocationCreateRequest.Data.Attributes](betaappclipinvocationcreaterequest/data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new Beta App Clip Invocations resource.
- [object BetaAppClipInvocationCreateRequest.Data.Relationships](betaappclipinvocationcreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (BetaAppClipInvocationCreateRequest.Data.Attributes) *(required)*: The attributes that describes the request that creates a Beta App Clip Invocations resource.
- `relationships` (BetaAppClipInvocationCreateRequest.Data.Relationships) *(required)*: The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BetaAppClipInvocationLocalizationInlineCreate](betaappclipinvocationlocalizationinlinecreate.md)
  An inline object for specifying a localized title for a beta App Clip invocation within a parent create or update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappclipinvocationcreaterequest/data-data.dictionary)*