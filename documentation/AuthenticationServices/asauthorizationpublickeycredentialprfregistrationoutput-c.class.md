# ASAuthorizationPublicKeyCredentialPRFRegistrationOutput

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A type to represent outputs of the web authentication PRF extension, when requesting them during a registration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@interface ASAuthorizationPublicKeyCredentialPRFRegistrationOutput : NSObject
```

## Overview

This object represents one or two `SymmetricKey` keys that are available anywhere the passkey is available for use. These are general purpose keys that you can use for application-specific needs, such as encryption of user data.

Don’t store or export these keys. Derive these keys only as the result of an assertion operation, and then discard them when the operation finishes.

## Topics

### Determining PRF support
- [isSupported](./asauthorizationpublickeycredentialprfregistrationoutput-c.class/issupported.md)
  A Boolean value that indicates whether the newly created passkey supports the PRF extension.
### Accessing symmetric keys
- [first](./asauthorizationpublickeycredentialprfregistrationoutput-c.class/first.md)
  A symmetric key that’s unique to the passkey and derives from the first input, if specified.
- [second](./asauthorizationpublickeycredentialprfregistrationoutput-c.class/second.md)
  A second symmetric key that’s unique to the passkey, and derives from the second input, if specified.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationoutput-c.class)*