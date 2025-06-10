# IOUSBHostObjectDestroyOptions

**Framework**: IOUSBHost  
**Kind**: struct

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostObjectDestroyOptions
```

#### Overview

```None
         the device will not be reset and drivers will not be re-registered for matching.  This allows for IOUSBHostDevice
         objects that were initialized with <code>IOUSBHostObjectInitOptionsDeviceCapture</code> to honor the
         <code>kUSBHostMessageDeviceIsRequestingClose</code> message.

         This option is only valid for macOS
```

## Topics

### Initializers
- [init(rawValue: UInt)](iousbhostobjectdestroyoptions/init(rawvalue:).md)
### Type Properties
- [static var deviceSurrender: IOUSBHostObjectDestroyOptions](iousbhostobjectdestroyoptions/devicesurrender.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct IOUSBHostCIControllerState](iousbhostcicontrollerstate.md)
- [struct IOUSBHostCIDeviceSpeed](iousbhostcidevicespeed.md)
- [struct IOUSBHostCIDeviceState](iousbhostcidevicestate.md)
- [struct IOUSBHostCIEndpointState](iousbhostciendpointstate.md)
- [struct IOUSBHostCIExceptionType](iousbhostciexceptiontype.md)
- [struct IOUSBHostCILinkState](iousbhostcilinkstate.md)
- [struct IOUSBHostCIMessage](iousbhostcimessage.md)
- [struct IOUSBHostCIMessageStatus](iousbhostcimessagestatus.md)
- [struct IOUSBHostCIMessageType](iousbhostcimessagetype.md)
- [struct IOUSBHostCIPortState](iousbhostciportstate.md)
- [struct IOUSBHostCIUserClientVersion](iousbhostciuserclientversion.md)
- [struct IOUSBHostIsochronousTransaction](iousbhostisochronoustransaction.md)
- [struct IOUSBHostIsochronousTransactionOptions](iousbhostisochronoustransactionoptions.md)
- [struct IOUSBHostIsochronousTransferOptions](iousbhostisochronoustransferoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobjectdestroyoptions)*