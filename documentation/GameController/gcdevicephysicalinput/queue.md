# queue

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The dispatch queue that the system uses for callbacks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var queue: dispatch_queue_t? { get set }
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Discussion

Objects that conform to the [`GCDevicePhysicalInput`](gcdevicephysicalinput.md) protocol dispatch callbacks on the device’s [`handlerQueue`](gcdevice/handlerqueue.md) property by default. If you want to use a different dispatch queue, set this property to the preferred queue before you set callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/queue)*