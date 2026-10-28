# performWithoutUserInteractionIfPossible(savePasswordRequest:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Attempt to save a password credential.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
func performWithoutUserInteractionIfPossible(savePasswordRequest: ASSavePasswordRequest)
```

```objc
- (void) performSavePasswordRequestWithoutUserInteractionIfPossible:(ASSavePasswordRequest *) savePasswordRequest;
```

## Discussion

To return results, you must call  [`completeSavePasswordRequest(completionHandler:)`](../ascredentialproviderextensioncontext/completesavepasswordrequest%28completionhandler%29.md).

> **Note**: When this method is called, your extension’s view controller is not present on the screen. You can request user interaction by calling `ASCredentialProviderExtensionContext/cancelRequest(with:)`, using [`userInteractionRequired`](../asextensionerror/userinteractionrequired.md).

To indicate support for this feature, add `SupportsSavePasswordCredentials` under the `ASCredentialProviderExtensionCapabilities` dictionary.

```
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ SupportsSavePasswordCredentials => true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(savepasswordrequest:))*