# performWithoutUserInteractionIfPossible(savePasswordRequest:)

**Framework**: Authentication Services  
**Kind**: method

Attempt to save a password credential.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
func performWithoutUserInteractionIfPossible(savePasswordRequest: ASSavePasswordRequest)
```

#### Discussion

To return results, you must call  [`completeSavePasswordRequest(completionHandler:)`](ascredentialproviderextensioncontext/completesavepasswordrequest(completionhandler:).md).

> **Note**: When this method is called, your extension’s view controller is not present on the screen. You can request user interaction by calling `ASCredentialProviderExtensionContext/cancelRequest(with:)`, using [`userInteractionRequired`](asextensionerror/userinteractionrequired.md).

To indicate support for this feature, add `SupportsSavePasswordCredentials` under the `ASCredentialProviderExtensionCapabilities` dictionary.

```None
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ SupportsSavePasswordCredentials => true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(savepasswordrequest:))*