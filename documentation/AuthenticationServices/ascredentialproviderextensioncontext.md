# ASCredentialProviderExtensionContext

**Framework**: Authentication Services  
**Kind**: class

A mechanism that credential provider extensions use to communicate with the system.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class ASCredentialProviderExtensionContext
```

## Topics

### Configuring the extension
- [func completeExtensionConfigurationRequest()](ascredentialproviderextensioncontext/completeextensionconfigurationrequest.md)
  Completes the request to configure the extension.
### Providing credentials
- [func completeRequest(withSelectedCredential: ASPasswordCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md)
  Provides the user-selected credential.
- [func completeAssertionRequest(using: ASPasskeyAssertionCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md)
  Complete the passkey assertion request by providing the user-selected passkey credential.
- [func completeRegistrationRequest(using: ASPasskeyRegistrationCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeregistrationrequest(using:completionhandler:).md)
  Complete the registration request by providing the newly-created passkey credential.
- [func completeOneTimeCodeRequest(using: ASOneTimeCodeCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeonetimecoderequest(using:completionhandler:).md)
  Provides the user-selected one-time passcode (OTP).
- [class ASPasswordCredential](aspasswordcredential.md)
  A password credential.
- [class ASPasskeyAssertionCredential](aspasskeyassertioncredential.md)
  A passkey assertion credential.
- [class ASPasskeyRegistrationCredential](aspasskeyregistrationcredential.md)
  A passkey registration credential.
- [class ASOneTimeCodeCredential](asonetimecodecredential.md)
  A one-time passcode (OTP) credential.
### Providing text to AutoFill
- [func completeRequest(withTextToInsert: String, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completerequest(withtexttoinsert:completionhandler:).md)
  Provides the user-selected text.
### Canceling
- [func cancelRequest(withError: any Error)](ascredentialproviderextensioncontext/cancelrequest(witherror:).md)
  Cancels the request.
### Instance Methods
- [func completeGeneratePasswordRequest(results: [ASGeneratedPassword], completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completegeneratepasswordrequest(results:completionhandler:).md)
  Return potential passwords for the given request.
- [func completeSavePasswordRequest(completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completesavepasswordrequest(completionhandler:).md)
  Signal that a password request was successfully saved.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/NSExtensionContext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var extensionContext: ASCredentialProviderExtensionContext](ascredentialproviderviewcontroller/extensioncontext.md)
  The context your credential provider extension uses to provide information to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext)*