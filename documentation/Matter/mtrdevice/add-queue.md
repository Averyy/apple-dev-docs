# add(_:queue:)

**Framework**: Matter  
**Kind**: method

Adds a delegate to receive asynchronous callbacks about the device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func add(_ delegate: any MTRDeviceDelegate, queue: dispatch_queue_t)
```

#### Discussion

The delegate will be called on the provided queue, for attribute reports, event reports, and device state changes.

MTRDevice holds a weak reference to the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/add(_:queue:))*