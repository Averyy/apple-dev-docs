# ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A type that represents input for the binary large object extension in passkey assertion requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput : NSObject
```

#### Overview

Use this type during assertion (sign-in) with an existing passkey. An app can specify exactly one operation to perform during the sign-in: Either read the existing saved blob or write a new blob, overwriting the existing one, if applicable. This restriction mirrors the operations available in the WebAuthn specification.

## Topics

### Creating a binary large object input
- [- initWithOperation:](./asauthorizationpublickeycredentiallargeblobassertioninput-c.class/initwithoperation_.md)
  Creates an assertion input with the specified operation.
### Inspecting properties
- [dataToWrite](./asauthorizationpublickeycredentiallargeblobassertioninput-c.class/datatowrite.md)
  The data to write to the assertion’s binary large object.
- [operation](./asauthorizationpublickeycredentiallargeblobassertioninput-c.class/operation.md)
  The operation to perform.
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionOperation](./asauthorizationpublickeycredentiallargeblobassertionoperation.md)
  A type that represents the operation of the large blob assertion.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Inputs
- [largeBlob](./aspasskeyassertioncredentialextensioninput-c.class/largeblob.md)
  Input for the WebAuthn large binary object extension in passkey assertion requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentiallargeblobassertioninput-c.class)*