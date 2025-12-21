# ASPasskeyRegistrationCredential

**Framework**: Authentication Services  
**Kind**: class

A passkey registration credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASPasskeyRegistrationCredential
```

#### Overview

Create a passkey registration credential to provide a response to a passkey registration request from your credential provider extension. Call [`completeRegistrationRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeregistrationrequest(using:completionhandler:).md), passing your passkey registration credential.

## Topics

### Creating a passkey registration credential
- [init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data)](aspasskeyregistrationcredential/init(relyingparty:clientdatahash:credentialid:attestationobject:).md)
  Initializes a passkey registration credential object.
- [convenience init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data, extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?)](aspasskeyregistrationcredential/init(relyingparty:clientdatahash:credentialid:attestationobject:extensionoutput:).md)
  Initializes a passkey registration credential object.
### Accessing credential information
- [var attestationObject: Data](aspasskeyregistrationcredential/attestationobject.md)
  The attestation object for this passkey.
- [var clientDataHash: Data](aspasskeyregistrationcredential/clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](aspasskeyregistrationcredential/credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](aspasskeyregistrationcredential/relyingparty.md)
  The relying party associated with this passkey.
### Accessing extension output
- [var extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?](aspasskeyregistrationcredential/extensionoutput-2lf9m.md)
  An output from WebAuthn extensions.
- [struct ASPasskeyRegistrationCredentialExtensionOutput](aspasskeyregistrationcredentialextensionoutput-swift.struct.md)
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
- [class ASPasskeyAssertionCredential](aspasskeyassertioncredential.md)
  A passkey assertion credential.
- [class ASOneTimeCodeCredential](asonetimecodecredential.md)
  A one-time passcode (OTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential)*