# setDelegate(_:queue:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 18.0
- iPadOS 16.1+ - Deprecated in 18.0
- Mac Catalyst 16.1+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.1+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.1+ - Deprecated in 11.0

> **Deprecated**: Please use addDelegate:queue:interestedPaths:

## Declaration

```swift
func setDelegate(_ delegate: any MTRDeviceDelegate, queue: dispatch_queue_t)
```

```objc
- (void) setDelegate:(id<MTRDeviceDelegate>) delegate queue:(dispatch_queue_t) queue;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/setdelegate(_:queue:))*