# isConnected

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether a device is currently connected to the system and available for use.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var isConnected: Bool { get }
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false) for a particular capture device instance, it doesn’t become [`true`](https://developer.apple.com/documentation/swift/true) again. If the same physical device reconnects, the system represents it as a new capture device instance.

You can key-value observe this property value to monitor when a device is no longer available.

## See Also

- [var isSuspended: Bool](avcapturedevice/issuspended.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [var isInUseByAnotherApplication: Bool](avcapturedevice/isinusebyanotherapplication.md)
  A Boolean value that indicates whether another app is using the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isconnected)*