# ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A type to represent the output of the requested large binary object operation, which returns in a passkey sign-in response.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput : NSObject
```

#### Overview

For a read operation, this type contains the saved blob, if one is present and the read succeeds. For a write operation, this type indicates whether the write succeeds.

## Topics

### Inspecting the result
- [didWrite](./asauthorizationpublickeycredentiallargeblobassertionoutput-c.class/didwrite.md)
  A Boolean value that indicates whether a write operation for a large binary object succeeds.
- [readData](./asauthorizationpublickeycredentiallargeblobassertionoutput-c.class/readdata.md)
  Data the system reads from the large binary object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Inspecting properties
- [largeBlobAssertionOutput](./aspasskeyassertioncredentialextensionoutput-c.class/largeblobassertionoutput.md)
  The output for a large binary object operation during passkey assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentiallargeblobassertionoutput-c.class)*