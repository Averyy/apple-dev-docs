# ASCredentialProviderExtensionContext

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASCredentialProviderExtensionContext : NSExtensionContext
```

## Topics

### Configuring the extension
- [func completeExtensionConfigurationRequest()](./ascredentialproviderextensioncontext/completeextensionconfigurationrequest%28%29.md)
  Completes the request to configure the extension.
### Providing credentials
- [func completeRequest(withSelectedCredential: ASPasswordCredential, completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completerequest%28withselectedcredential,completionhandler%29.md)
  Provides the user-selected credential.
- [func completeAssertionRequest(using: ASPasskeyAssertionCredential, completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completeassertionrequest%28using,completionhandler%29.md)
  Complete the passkey assertion request by providing the user-selected passkey credential.
- [func completeRegistrationRequest(using: ASPasskeyRegistrationCredential, completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completeregistrationrequest%28using,completionhandler%29.md)
  Complete the registration request by providing the newly-created passkey credential.
- [func completeOneTimeCodeRequest(using: ASOneTimeCodeCredential, completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completeonetimecoderequest%28using,completionhandler%29.md)
  Provides the user-selected one-time passcode (OTP).
- [class ASPasswordCredential](./aspasswordcredential.md)
  A password credential.
- [class ASPasskeyAssertionCredential](./aspasskeyassertioncredential.md)
  A passkey assertion credential.
- [class ASPasskeyRegistrationCredential](./aspasskeyregistrationcredential.md)
  A passkey registration credential.
- [class ASOneTimeCodeCredential](./asonetimecodecredential.md)
  A one-time passcode (OTP) credential.
### Providing text to AutoFill
- [func completeRequest(withTextToInsert: String, completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completerequest%28withtexttoinsert,completionhandler%29.md)
  Provides the user-selected text.
### Canceling
- [func cancelRequest(withError: any Error)](./ascredentialproviderextensioncontext/cancelrequest%28witherror%29.md)
  Cancels the request.
### Instance Methods
- [func completeGeneratePasswordRequest(results: [ASGeneratedPassword], completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completegeneratepasswordrequest%28results,completionhandler%29.md)
  Return potential passwords for the given request.
- [func completeSavePasswordRequest(completionHandler: ((Bool) -> Void)?)](./ascredentialproviderextensioncontext/completesavepasswordrequest%28completionhandler%29.md)
  Signal that a password request was successfully saved.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the extension context
- [var extensionContext: ASCredentialProviderExtensionContext](./ascredentialproviderviewcontroller/extensioncontext.md)
  The context your credential provider extension uses to provide information to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext)*