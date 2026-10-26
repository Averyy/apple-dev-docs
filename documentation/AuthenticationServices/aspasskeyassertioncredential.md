# ASPasskeyAssertionCredential

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASPasskeyAssertionCredential : NSObject
```

#### Overview

Create a passkey assertion credential to provide a response to a passkey authentication challenge from your credential provider extension. Call [`completeAssertionRequest(using:completionHandler:)`](./ascredentialproviderextensioncontext/completeassertionrequest%28using,completionhandler%29.md), passing your passkey assertion credential.

## Topics

### Creating a passkey assertion credential
- [init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data)](./aspasskeyassertioncredential/init%28userhandle,relyingparty,signature,clientdatahash,authenticatordata,credentialid%29.md)
  Initializes a passkey assertion credential object.
- [convenience init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data, extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?)](./aspasskeyassertioncredential/init%28userhandle,relyingparty,signature,clientdatahash,authenticatordata,credentialid,extensionoutput%29.md)
  Initializes a passkey assertion credential object, optionally specifying an extension output.
- [+ credentialWithUserHandle:relyingParty:signature:clientDataHash:authenticatorData:credentialID:](./aspasskeyassertioncredential/credentialwithuserhandle_relyingparty_signature_clientdatahash_authenticatordata_credentialid_.md)
  Creates and initializes a new passkey assertion credential.
- [- initWithUserHandle:relyingParty:signature:clientDataHash:authenticatorData:credentialID:extensionOutput:](./aspasskeyassertioncredential/initwithuserhandle_relyingparty_signature_clientdatahash_authenticatordata_credentialid_extensionoutput_.md)
  Initializes a passkey assertion credential object, optionally specifying an extension output.
### Accessing credential information
- [var authenticatorData: Data](./aspasskeyassertioncredential/authenticatordata.md)
  The authenticator data of the application that created this passkey assertion credential.
- [var clientDataHash: Data](./aspasskeyassertioncredential/clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](./aspasskeyassertioncredential/credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](./aspasskeyassertioncredential/relyingparty.md)
  The relying party associated with this passkey.
- [var signature: Data](./aspasskeyassertioncredential/signature.md)
  The cryptographic signature of this credential.
- [var userHandle: Data](./aspasskeyassertioncredential/userhandle.md)
  The user handle of this passkey.
### Accessing extension output
- [var extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?](./aspasskeyassertioncredential/extensionoutput-7t6rn.md)
  An output from WebAuthn extensions.
- [struct ASPasskeyAssertionCredentialExtensionOutput](./aspasskeyassertioncredentialextensionoutput-swift.struct.md)
  A type that encapsulates output for various WebAuthn extensions during passkey assertion.
- [extensionOutput](./aspasskeyassertioncredential/extensionoutput-46ib3.md)
  An output from WebAuthn extensions.
- [ASPasskeyAssertionCredentialExtensionOutput](./aspasskeyassertioncredentialextensionoutput-c.class.md)
  A class that encapsulates output for various WebAuthn extensions during passkey assertion.
### Initializers
- [init?(coder: NSCoder)](./aspasskeyassertioncredential/init%28coder%29.md)

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
- [class ASPasskeyRegistrationCredential](./aspasskeyregistrationcredential.md)
  A passkey registration credential.
- [class ASOneTimeCodeCredential](./asonetimecodecredential.md)
  A one-time passcode (OTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential)*