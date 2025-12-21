# performWithoutUserInteraction(generatePasswordsRequest:)

**Framework**: Authentication Services  
**Kind**: method

Attempt to generate passwords based on developer-specified rules.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
func performWithoutUserInteraction(generatePasswordsRequest: ASGeneratePasswordsRequest)
```

#### Discussion

To return results, you must call ``ASCredentialProviderExtensionContext/completeGeneratePasswordRequest(results:completionHandler:)`.

> **Note**: When this method is called, your extension’s view controller is not present on the screen. [`userInteractionRequired`](asextensionerror/userinteractionrequired.md) will not be honored and treated as a failure.

> **Note**: You should not update or replace any existing credentials when this API is called.

To indicate support for this feature, add `SupportsGeneratePasswordCredentials` under the `ASCredentialProviderExtensionCapabilities` dictionary.

```None
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ SupportsSavePasswordCredentials => true
            ├─ SupportsGeneratePasswordCredentials => true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/performwithoutuserinteraction(generatepasswordsrequest:))*