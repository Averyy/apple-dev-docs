# ASOneTimeCodeCredential

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A one-time passcode (OTP) credential.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class ASOneTimeCodeCredential
```

```objc
@interface ASOneTimeCodeCredential : NSObject
```

## Topics

### Creating an OTP credential
- [init(code: String)](./asonetimecodecredential/init%28code%29.md)
  Creates a one-time passcode (OTP) credential.
### Accessing the OTP
- [var code: String](./asonetimecodecredential/code.md)
  The one-time passcode.
### Initializers
- [init?(coder: NSCoder)](./asonetimecodecredential/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](./asauthorizationcredential.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asonetimecodecredential)*