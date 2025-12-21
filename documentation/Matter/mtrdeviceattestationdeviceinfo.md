# MTRDeviceAttestationDeviceInfo

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRDeviceAttestationDeviceInfo
```

## Topics

### Instance Properties
- [var basicInformationProductID: NSNumber](mtrdeviceattestationdeviceinfo/basicinformationproductid.md)
- [var basicInformationVendorID: NSNumber](mtrdeviceattestationdeviceinfo/basicinformationvendorid.md)
- [var certificateDeclaration: Data?](mtrdeviceattestationdeviceinfo/certificatedeclaration.md)
- [var dacCertificate: Data](mtrdeviceattestationdeviceinfo/daccertificate.md)
- [var dacPAICertificate: Data](mtrdeviceattestationdeviceinfo/dacpaicertificate.md)
- [var productID: NSNumber?](mtrdeviceattestationdeviceinfo/productid.md)
- [var vendorID: NSNumber?](mtrdeviceattestationdeviceinfo/vendorid.md)
- [var attestationChallenge: Data](mtrdeviceattestationdeviceinfo/attestationchallenge.md)
  The attestation challenge from the secure session.
- [var attestationNonce: Data](mtrdeviceattestationdeviceinfo/attestationnonce.md)
  The attestation nonce from the AttestationRequest command.
- [var certificationDeclaration: Data?](mtrdeviceattestationdeviceinfo/certificationdeclaration.md)
  The certification declaration of the device, if available.  This is a DER-encoded string representing a CMS-formatted certification declaration.  May be nil only if attestation verification failed.
- [var elementsSignature: Data](mtrdeviceattestationdeviceinfo/elementssignature.md)
  A signature, using the device attestation private key of the device that sent the attestation information, over the concatenation of elementsTLV and attestationChallenge.
- [var elementsTLV: Data](mtrdeviceattestationdeviceinfo/elementstlv.md)
  The TLV-encoded attestation_elements_message that was used to find the certificationDeclaration (possibly unsuccessfully).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdeviceattestationdeviceinfo)*