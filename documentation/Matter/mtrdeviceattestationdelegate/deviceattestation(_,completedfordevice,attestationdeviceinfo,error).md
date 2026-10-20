# deviceAttestation(_:completedForDevice:attestationDeviceInfo:error:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please implement deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:

## Declaration

```swift
optional func deviceAttestation(_ controller: MTRDeviceController, completedForDevice device: UnsafeMutableRawPointer, attestationDeviceInfo: MTRDeviceAttestationDeviceInfo, error: (any Error)?)
```

```objc
- (void) deviceAttestation:(MTRDeviceController *) controller completedForDevice:(void *) device attestationDeviceInfo:(MTRDeviceAttestationDeviceInfo *) attestationDeviceInfo error:(NSError *) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdeviceattestationdelegate/deviceattestation(_:completedfordevice:attestationdeviceinfo:error:))*