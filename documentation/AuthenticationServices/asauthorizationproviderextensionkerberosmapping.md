# ASAuthorizationProviderExtensionKerberosMapping

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A set of Kerberos mappings that the system login process uses.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class ASAuthorizationProviderExtensionKerberosMapping
```

```objc
@interface ASAuthorizationProviderExtensionKerberosMapping : NSObject
```

## Mentions

- [Creating a JSON Web Encryption (JWE) login response](./creating-a-json-web-encryption-jwe-login-response.md)

## Overview

This class contains a set of mappings for the sign-on token when importing the Kerberos ticket.

## Topics

### Getting the properties
- [var clientNameKeyName: String?](./asauthorizationproviderextensionkerberosmapping/clientnamekeyname.md)
  The key name of the Kerberos client name string.
- [var encryptionKeyTypeKeyName: String?](./asauthorizationproviderextensionkerberosmapping/encryptionkeytypekeyname.md)
  The key name of the Kerberos session key type number.
- [var messageBufferKeyName: String?](./asauthorizationproviderextensionkerberosmapping/messagebufferkeyname.md)
  The key name of the Base 64-encoded Kerberos AS-REP string.
- [var realmKeyName: String?](./asauthorizationproviderextensionkerberosmapping/realmkeyname.md)
  The key name of the Kerberos realm string.
- [var serviceNameKeyName: String?](./asauthorizationproviderextensionkerberosmapping/servicenamekeyname.md)
  The key name of the Kerberos service name string.
- [var sessionKeyKeyName: String?](./asauthorizationproviderextensionkerberosmapping/sessionkeykeyname.md)
  The key name of the Kerberos session key.
- [var ticketKeyPath: String?](./asauthorizationproviderextensionkerberosmapping/ticketkeypath.md)
  The keypath in the response JSON that uses this set of mappings.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Authentication
- [Authentication process](./authentication-process.md)
  Use a system-supported method to authenticate with an identity provider.
- [Implementing web-based authentication with Platform Single Sign-on](./implementing-web-based-authentication.md)
  Support modern, phishing-resistant, and flexible authentication methods.
- [Using access keys with Platform Single Sign-on](./using-access-keys-with-platform-single-sign-on.md)
  Authenticate users with access keys stored in Apple Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionkerberosmapping)*