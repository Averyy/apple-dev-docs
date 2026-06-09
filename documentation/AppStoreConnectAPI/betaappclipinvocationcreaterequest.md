# BetaAppClipInvocationCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create an App Clip invocation for testers.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BetaAppClipInvocationCreateRequest
```

## Topics

### Objects
- [object BetaAppClipInvocationLocalizationInlineCreate](betaappclipinvocationlocalizationinlinecreate.md)
  An inline object for specifying a localized title for a beta App Clip invocation within a parent create or update request.
- [object BetaAppClipInvocationCreateRequest.Data](betaappclipinvocationcreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (BetaAppClipInvocationCreateRequest.Data) *(required)*: The resource data.
- `included` ([BetaAppClipInvocationLocalizationInlineCreate]): The relationship data to include in the response.

## See Also

- [object BetaAppClipInvocation](betaappclipinvocation.md)
  A TestFlight URL scheme invocation that allows beta testers to launch an App Clip during testing.
- [object BetaAppClipInvocationResponse](betaappclipinvocationresponse.md)
  A response containing a single TestFlight App Clip invocation URL.
- [object BetaAppClipInvocationUpdateRequest](betaappclipinvocationupdaterequest.md)
  The request body you use to update a Beta App Clip Invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappclipinvocationcreaterequest)*