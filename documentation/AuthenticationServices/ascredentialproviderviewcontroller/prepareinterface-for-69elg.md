# prepareInterface(for:)

**Framework**: Authentication Services  
**Kind**: method

Prepares the interface to display a prompt to save a password credential.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
func prepareInterface(for savePasswordRequest: ASSavePasswordRequest)
```

#### Discussion

The system calls this method to tell your extension’s view controller to prepare to present a prompt to save a password credential. After calling this method, the system presents the view controller to the user.

Upon success, call [`completeSavePasswordRequest(completionHandler:)`](ascredentialproviderextensioncontext/completesavepasswordrequest(completionhandler:).md).

Always provide a way for someone to cancel the operation from your view controller, for example, by including a Cancel button in the navigation bar. When someone cancels the operation, call `ASCredentialProviderExtensionContext/cancelRequest(with:)`, using [`userCanceled`](asextensionerror/usercanceled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterface(for:)-69elg)*