# MTRDeviceControllerStartupParams

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
class MTRDeviceControllerStartupParams
```

## Mentions

- [Onboarding a Matter device](onboarding-a-matter-device.md)

## Topics

### Initializers
- [init(ipk: Data, fabricID: NSNumber, nocSigner: any MTRKeypair)](mtrdevicecontrollerstartupparams/init(ipk:fabricid:nocsigner:)-810ix.md)
- [init(ipk: Data, operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data)](mtrdevicecontrollerstartupparams/init(ipk:operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:)-3l4qp.md)
- [init(operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data, ipk: Data)](mtrdevicecontrollerstartupparams/init(operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:ipk:).md)
- [init(signingKeypair: any MTRKeypair, fabricId: UInt64, ipk: Data)](mtrdevicecontrollerstartupparams/init(signingkeypair:fabricid:ipk:).md)
- [init(IPK: Data, fabricID: NSNumber, nocSigner: any MTRKeypair)](mtrdevicecontrollerstartupparams/init(ipk:fabricid:nocsigner:)-6tfo5.md)
- [init(IPK: Data, operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data)](mtrdevicecontrollerstartupparams/init(ipk:operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:)-3k8x7.md)
- [init(signing: any MTRKeypair, fabricId: UInt64, ipk: Data)](mtrdevicecontrollerstartupparams/init(signing:fabricid:ipk:).md)
### Instance Properties
- [var caseAuthenticatedTags: Set<NSNumber>?](mtrdevicecontrollerstartupparams/caseauthenticatedtags.md)
- [var fabricID: NSNumber](mtrdevicecontrollerstartupparams/fabricid-1cm6z.md)
- [var fabricId: UInt64](mtrdevicecontrollerstartupparams/fabricid-1cm7v.md)
- [var intermediateCertificate: Data?](mtrdevicecontrollerstartupparams/intermediatecertificate.md)
- [var ipk: Data](mtrdevicecontrollerstartupparams/ipk.md)
- [var nocSigner: (any MTRKeypair)?](mtrdevicecontrollerstartupparams/nocsigner.md)
- [var nodeID: NSNumber?](mtrdevicecontrollerstartupparams/nodeid-9iwwv.md)
  Node id for this controller.
- [var nodeId: NSNumber?](mtrdevicecontrollerstartupparams/nodeid-9iwxr.md)
- [var operationalCertificate: Data?](mtrdevicecontrollerstartupparams/operationalcertificate.md)
- [var operationalCertificateIssuer: (any MTROperationalCertificateIssuer)?](mtrdevicecontrollerstartupparams/operationalcertificateissuer.md)
- [var operationalCertificateIssuerQueue: dispatch_queue_t?](mtrdevicecontrollerstartupparams/operationalcertificateissuerqueue.md)
- [var operationalKeypair: (any MTRKeypair)?](mtrdevicecontrollerstartupparams/operationalkeypair.md)
- [var rootCertificate: Data?](mtrdevicecontrollerstartupparams/rootcertificate.md)
- [var vendorID: NSNumber?](mtrdevicecontrollerstartupparams/vendorid-8ru1s.md)
- [var vendorId: NSNumber?](mtrdevicecontrollerstartupparams/vendorid-8ru0w.md)
### Default Implementations
- [MTRDeviceControllerStartupParams Implementations](mtrdevicecontrollerstartupparams/mtrdevicecontrollerstartupparams-implementations.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstartupparams)*