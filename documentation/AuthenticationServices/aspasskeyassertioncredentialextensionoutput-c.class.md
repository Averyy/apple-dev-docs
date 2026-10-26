# ASPasskeyAssertionCredentialExtensionOutput

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A class that encapsulates output for various WebAuthn extensions during passkey assertion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@interface ASPasskeyAssertionCredentialExtensionOutput : NSObject
```

## Topics

### Creating an extension output instance
- [- initWithLargeBlobOutput:](./aspasskeyassertioncredentialextensionoutput-c.class/initwithlargebloboutput_.md)
  Creates an extension output instance with the given large binary object output.
### Inspecting properties
- [largeBlobAssertionOutput](./aspasskeyassertioncredentialextensionoutput-c.class/largeblobassertionoutput.md)
  The output for a large binary object operation during passkey assertion.
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](./asauthorizationpublickeycredentiallargeblobassertionoutput-c.class.md)
  A type to represent the output of the requested large binary object operation, which returns in a passkey sign-in response.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Accessing extension output
- [extensionOutput](./aspasskeyassertioncredential/extensionoutput-46ib3.md)
  An output from WebAuthn extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredentialextensionoutput-c.class)*