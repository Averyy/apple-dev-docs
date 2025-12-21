# prepareInterface(for:)

**Framework**: Authentication Services  
**Kind**: method

Prepares the interface to display a prompt to generate passwords based on developer-specified rules.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
func prepareInterface(for generatePasswordsRequest: ASGeneratePasswordsRequest)
```

#### Discussion

The system calls this method to tell your extension’s view controller to prepare to present a prompt to generate passwords. After calling this method, the system presents the view controller to the user.

Upon success, call [`completeGeneratePasswordRequest(results:completionHandler:)`](ascredentialproviderextensioncontext/completegeneratepasswordrequest(results:completionhandler:).md).

Always provide a way for someone to cancel the operation from your view controller, for example, by including a Cancel button in the navigation bar. When someone cancels the operation, call `ASCredentialProviderExtensionContext/cancelRequest(with:)`, using [`userCanceled`](asextensionerror/usercanceled.md).

> **Note**: This flow can only be initiated by the user. It will not be triggered from `-performGeneratePasswordsRequestWithoutUserInteraction:`

> **Note**: You should not update or replace any existing credentials when this API is called.

Support of this feature is implied by default when adding support for generating passwords. You can opt out of showing UI by adding the `SupportsGeneratePasswordCredentialsWithUI` under the `ASCredentialProviderExtensionCapabilities` dictionary. When opting out, you must provide a value of `false` as the default value for this field is `true`. When you opt out, the OS will provide a relevant experience after requesting generated passwords from your extension.

```None
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ SupportsSavePasswordCredentials => true
            ├─ SupportsGeneratePasswordCredentials => true
            ├─ SupportsGeneratePasswordCredentialsWithUI => true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterface(for:)-7ideq)*