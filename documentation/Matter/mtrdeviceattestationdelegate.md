# MTRDeviceAttestationDelegate

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTRDeviceAttestationDelegate <NSObject>
```

## Topics

### Instance Methods
- [func deviceAttestation(MTRDeviceController, completedForDevice: UnsafeMutableRawPointer, attestationDeviceInfo: MTRDeviceAttestationDeviceInfo, error: (any Error)?)](./mtrdeviceattestationdelegate/deviceattestation%28_,completedfordevice,attestationdeviceinfo,error%29.md)
- [func deviceAttestation(MTRDeviceController, failedForDevice: UnsafeMutableRawPointer, error: any Error)](./mtrdeviceattestationdelegate/deviceattestation%28_,failedfordevice,error%29.md)
- [func deviceAttestationCompleted(for: MTRDeviceController, opaqueDeviceHandle: UnsafeMutableRawPointer, attestationDeviceInfo: MTRDeviceAttestationDeviceInfo, error: (any Error)?)](./mtrdeviceattestationdelegate/deviceattestationcompleted%28for,opaquedevicehandle,attestationdeviceinfo,error%29.md)
- [func deviceAttestationFailed(for: MTRDeviceController, opaqueDeviceHandle: UnsafeMutableRawPointer, error: any Error)](./mtrdeviceattestationdelegate/deviceattestationfailed%28for,opaquedevicehandle,error%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdeviceattestationdelegate)*