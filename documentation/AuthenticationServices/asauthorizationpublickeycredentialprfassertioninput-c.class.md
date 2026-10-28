# ASAuthorizationPublicKeyCredentialPRFAssertionInput

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A type that represents input for the web authentication PRF extension in passkey assertion requests.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@interface ASAuthorizationPublicKeyCredentialPRFAssertionInput : NSObject
```

## Overview

The PRF extension lets you create general purpose `SymmetricKey` keys from passkeys, which can be useful for tasks like encryption of user data. Using the same input values with the same passkey produces the same `SymmetricKey`.

## Topics

### Instance Properties
- [inputValues](./asauthorizationpublickeycredentialprfassertioninput-c.class/inputvalues.md)
  The input values to use when generating the PRF extension output, if specified.
- [perCredentialInputValues](./asauthorizationpublickeycredentialprfassertioninput-c.class/percredentialinputvalues.md)
  A map of credential identifiers to input values for the PRF extension.
### Instance Methods
- [- initWithInputValues:perCredentialInputValues:](./asauthorizationpublickeycredentialprfassertioninput-c.class/initwithinputvalues_percredentialinputvalues_.md)
  Initializes the inputs for the PRF extension.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Accessing request properties
- [var allowedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]](./asauthorizationplatformpublickeycredentialassertionrequest/allowedcredentials.md)
  The array of allowed credentials.
- [largeBlob](./asauthorizationplatformpublickeycredentialassertionrequest/largeblob-5mg1q.md)
  The request’s binary large object value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-c.class)*