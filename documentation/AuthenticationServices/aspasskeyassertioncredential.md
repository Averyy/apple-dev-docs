# ASPasskeyAssertionCredential

**Framework**: Authentication Services  
**Kind**: class

A passkey assertion credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASPasskeyAssertionCredential
```

#### Overview

Create a passkey assertion credential to provide a response to a passkey authentication challenge from your credential provider extension. Call [`completeAssertionRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md), passing your passkey assertion credential.

## Topics

### Creating a passkey assertion credential
- [init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data)](aspasskeyassertioncredential/init(userhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:).md)
  Initializes a passkey assertion credential object.
- [convenience init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data, extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?)](aspasskeyassertioncredential/init(userhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:extensionoutput:).md)
  Initializes a passkey assertion credential object, optionally specifying an extension output.
### Accessing credential information
- [var authenticatorData: Data](aspasskeyassertioncredential/authenticatordata.md)
  The authenticator data of the application that created this passkey assertion credential.
- [var clientDataHash: Data](aspasskeyassertioncredential/clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](aspasskeyassertioncredential/credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](aspasskeyassertioncredential/relyingparty.md)
  The relying party associated with this passkey.
- [var signature: Data](aspasskeyassertioncredential/signature.md)
  The cryptographic signature of this credential.
- [var userHandle: Data](aspasskeyassertioncredential/userhandle.md)
  The user handle of this passkey.
### Accessing extension output
- [var extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?](aspasskeyassertioncredential/extensionoutput-7t6rn.md)
  An output from WebAuthn extensions.
- [struct ASPasskeyAssertionCredentialExtensionOutput](aspasskeyassertioncredentialextensionoutput-swift.struct.md)
  A type that encapsulates output for various WebAuthn extensions during passkey assertion.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationCredential](asauthorizationcredential.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

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
- [class ASPasskeyRegistrationCredential](aspasskeyregistrationcredential.md)
  A passkey registration credential.
- [class ASOneTimeCodeCredential](asonetimecodecredential.md)
  A one-time passcode (OTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential)*