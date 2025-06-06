# MTRDeviceAttestationDelegate

**Framework**: Matter  
**Kind**: protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol MTRDeviceAttestationDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func deviceAttestation(MTRDeviceController, completedForDevice: UnsafeMutableRawPointer, attestationDeviceInfo: MTRDeviceAttestationDeviceInfo, error: (any Error)?)](mtrdeviceattestationdelegate/deviceattestation(_:completedfordevice:attestationdeviceinfo:error:).md)
- [func deviceAttestation(MTRDeviceController, failedForDevice: UnsafeMutableRawPointer, error: any Error)](mtrdeviceattestationdelegate/deviceattestation(_:failedfordevice:error:).md)
- [func deviceAttestationCompleted(for: MTRDeviceController, opaqueDeviceHandle: UnsafeMutableRawPointer, attestationDeviceInfo: MTRDeviceAttestationDeviceInfo, error: (any Error)?)](mtrdeviceattestationdelegate/deviceattestationcompleted(for:opaquedevicehandle:attestationdeviceinfo:error:).md)
- [func deviceAttestationFailed(for: MTRDeviceController, opaqueDeviceHandle: UnsafeMutableRawPointer, error: any Error)](mtrdeviceattestationdelegate/deviceattestationfailed(for:opaquedevicehandle:error:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdeviceattestationdelegate)*