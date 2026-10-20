# continueCommissioningDevice(_:ignoreAttestationFailure:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func continueCommissioningDevice(_ opaqueDeviceHandle: UnsafeMutableRawPointer, ignoreAttestationFailure: Bool) throws
```

```objc
- (BOOL) continueCommissioningDevice:(void *) opaqueDeviceHandle ignoreAttestationFailure:(BOOL) ignoreAttestationFailure error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/continuecommissioningdevice(_:ignoreattestationfailure:))*