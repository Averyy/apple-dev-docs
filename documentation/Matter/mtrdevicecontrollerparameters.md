# MTRDeviceControllerParameters

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
class MTRDeviceControllerParameters
```

## Topics

### Instance Properties
- [var certificationDeclarationCertificates: [Data]?](mtrdevicecontrollerparameters/certificationdeclarationcertificates.md)
- [var concurrentSubscriptionEstablishmentsAllowedOnThread: Int](mtrdevicecontrollerparameters/concurrentsubscriptionestablishmentsallowedonthread.md)
- [var productAttestationAuthorityCertificates: [Data]?](mtrdevicecontrollerparameters/productattestationauthoritycertificates.md)
- [var shouldAdvertiseOperational: Bool](mtrdevicecontrollerparameters/shouldadvertiseoperational.md)
- [var storageBehaviorConfiguration: MTRDeviceStorageBehaviorConfiguration?](mtrdevicecontrollerparameters/storagebehaviorconfiguration.md)
  Sets the storage behavior configuration - see MTRDeviceStorageBehaviorConfiguration.h for details
### Instance Methods
- [func setOTAProviderDelegate(any MTROTAProviderDelegate, queue: dispatch_queue_t)](mtrdevicecontrollerparameters/setotaproviderdelegate(_:queue:).md)
- [func setOperationalCertificateIssuer(any MTROperationalCertificateIssuer, queue: dispatch_queue_t)](mtrdevicecontrollerparameters/setoperationalcertificateissuer(_:queue:).md)

## Relationships

### Inherits From
- [MTRDeviceControllerAbstractParameters](mtrdevicecontrollerabstractparameters.md)
### Inherited By
- [MTRDeviceControllerExternalCertificateParameters](mtrdevicecontrollerexternalcertificateparameters.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerparameters)*