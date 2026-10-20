# getBaseDevice(_:queue:completionHandler:)

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

> **Deprecated**: Please use [MTRBaseDevice deviceWithNodeID:controller:]

## Declaration

```swift
func getBaseDevice(_ deviceID: UInt64, queue: dispatch_queue_t, completionHandler: @escaping MTRDeviceConnectionCallback) -> Bool
```

```objc
- (BOOL) getBaseDevice:(uint64_t) deviceID queue:(dispatch_queue_t) queue completionHandler:(MTRDeviceConnectionCallback) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/getbasedevice(_:queue:completionhandler:))*