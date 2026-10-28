# ASAuthorizationPublicKeyCredentialPRFAssertionInputValues

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

The values to use as inputs to the salts for deriving the symmetric key.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@interface ASAuthorizationPublicKeyCredentialPRFAssertionInputValues : NSObject
```

## Overview

This type is analogous to `AuthenticationExtensionsPRFValues` in the WebAuthn specification.

## Topics

### Creating an input values instance
- [- initWithSaltInput1:saltInput2:](./asauthorizationpublickeycredentialprfassertioninputvalues/initwithsaltinput1_saltinput2_.md)
  Initializes an input values object with the given salts.
### Accessing salt inputs
- [saltInput1](./asauthorizationpublickeycredentialprfassertioninputvalues/saltinput1.md)
  A salt for the hashing function.
- [saltInput2](./asauthorizationpublickeycredentialprfassertioninputvalues/saltinput2.md)
  An optional second salt for the hashing function.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninputvalues)*