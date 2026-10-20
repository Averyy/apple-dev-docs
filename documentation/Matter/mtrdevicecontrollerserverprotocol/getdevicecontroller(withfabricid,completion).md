# getDeviceController(withFabricId:completion:)

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

> **Deprecated**: This never called.

## Declaration

```swift
optional func getDeviceController(withFabricId fabricId: UInt64, completion: @escaping @Sendable (Any?, (any Error)?) -> Void)
```

```swift
optional func deviceController(withFabricId fabricId: UInt64) async throws -> Any
```

```objc
- (void) getDeviceControllerWithFabricId:(uint64_t) fabricId completion:(MTRDeviceControllerGetterHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/getdevicecontroller(withfabricid:completion:))*