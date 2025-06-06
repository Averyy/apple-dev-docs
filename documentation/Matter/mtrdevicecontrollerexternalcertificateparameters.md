# MTRDeviceControllerExternalCertificateParameters

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRDeviceControllerExternalCertificateParameters
```

## Topics

### Initializers
- [init(storageDelegate: any MTRDeviceControllerStorageDelegate, storageDelegateQueue: dispatch_queue_t, uniqueIdentifier: UUID, ipk: Data, vendorID: NSNumber, operationalKeypair: any MTRKeypair, operationalCertificate: Data, intermediateCertificate: Data?, rootCertificate: Data)](mtrdevicecontrollerexternalcertificateparameters/init(storagedelegate:storagedelegatequeue:uniqueidentifier:ipk:vendorid:operationalkeypair:operationalcertificate:intermediatecertificate:rootcertificate:).md)
### Instance Properties
- [var rootCertificate: Data](mtrdevicecontrollerexternalcertificateparameters/rootcertificate.md)
  The root certificate we were initialized with.

## Relationships

### Inherits From
- [MTRDeviceControllerParameters](mtrdevicecontrollerparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerexternalcertificateparameters)*