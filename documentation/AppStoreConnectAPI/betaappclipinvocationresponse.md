# BetaAppClipInvocationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single TestFlight App Clip invocation URL.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BetaAppClipInvocationResponse
```

## Properties

- `data` (BetaAppClipInvocation) *(required)*: The resource data.
- `included` ([BetaAppClipInvocationLocalization]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

- [object BetaAppClipInvocation](betaappclipinvocation.md)
  A TestFlight URL scheme invocation that allows beta testers to launch an App Clip during testing.
- [object BetaAppClipInvocationCreateRequest](betaappclipinvocationcreaterequest.md)
  The request body you use to create an App Clip invocation for testers.
- [object BetaAppClipInvocationUpdateRequest](betaappclipinvocationupdaterequest.md)
  The request body you use to update a Beta App Clip Invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappclipinvocationresponse)*