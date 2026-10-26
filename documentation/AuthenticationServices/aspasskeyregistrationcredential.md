# ASPasskeyRegistrationCredential

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASPasskeyRegistrationCredential : NSObject
```

#### Overview

Create a passkey registration credential to provide a response to a passkey registration request from your credential provider extension. Call [`completeRegistrationRequest(using:completionHandler:)`](./ascredentialproviderextensioncontext/completeregistrationrequest%28using,completionhandler%29.md), passing your passkey registration credential.

## Topics

### Creating a passkey registration credential
- [init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data)](./aspasskeyregistrationcredential/init%28relyingparty,clientdatahash,credentialid,attestationobject%29.md)
  Initializes a passkey registration credential object.
- [convenience init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data, extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?)](./aspasskeyregistrationcredential/init%28relyingparty,clientdatahash,credentialid,attestationobject,extensionoutput%29.md)
  Initializes a passkey registration credential object.
- [+ credentialWithRelyingParty:clientDataHash:credentialID:attestationObject:](./aspasskeyregistrationcredential/credentialwithrelyingparty_clientdatahash_credentialid_attestationobject_.md)
  Creates and initializes a new passkey registration credential.
- [- initWithRelyingParty:clientDataHash:credentialID:attestationObject:extensionOutput:](./aspasskeyregistrationcredential/initwithrelyingparty_clientdatahash_credentialid_attestationobject_extensionoutput_.md)
  Initializes a passkey registration credential object.
### Accessing credential information
- [var attestationObject: Data](./aspasskeyregistrationcredential/attestationobject.md)
  The attestation object for this passkey.
- [var clientDataHash: Data](./aspasskeyregistrationcredential/clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](./aspasskeyregistrationcredential/credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](./aspasskeyregistrationcredential/relyingparty.md)
  The relying party associated with this passkey.
### Accessing extension output
- [var extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?](./aspasskeyregistrationcredential/extensionoutput-2lf9m.md)
  An output from WebAuthn extensions.
- [struct ASPasskeyRegistrationCredentialExtensionOutput](./aspasskeyregistrationcredentialextensionoutput-swift.struct.md)
  A type that encapsulates output for various WebAuthn extensions during passkey assertion.
- [extensionOutput](./aspasskeyregistrationcredential/extensionoutput-95gvu.md)
  An output from WebAuthn extensions.
- [ASPasskeyRegistrationCredentialExtensionOutput](./aspasskeyregistrationcredentialextensionoutput-c.class.md)
  A class that encapsulates output for various WebAuthn extensions during passkey registration.
### Initializers
- [init?(coder: NSCoder)](./aspasskeyregistrationcredential/init%28coder%29.md)

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
- [class ASPasskeyAssertionCredential](./aspasskeyassertioncredential.md)
  A passkey assertion credential.
- [class ASOneTimeCodeCredential](./asonetimecodecredential.md)
  A one-time passcode (OTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential)*