# isAttachedToDevice

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the controller closely integrates with the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isAttachedToDevice: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the controller may be formfitting or otherwise closely attach to the device so that the player can interact simultaneously with the controller and the device. If [`false`](https://developer.apple.com/documentation/Swift/false), the controller doesn’t have an attachment to the device.

## See Also

- [class func supportsHIDDevice(IOHIDDevice) -> Bool](gccontroller/supportshiddevice(_:).md)
  Returns a Boolean value that indicates whether the framework supports the specified human interface device.
- [class var shouldMonitorBackgroundEvents: Bool](gccontroller/shouldmonitorbackgroundevents.md)
  A Boolean value that indicates whether the app needs to respond to controller events when it isn’t the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/isattachedtodevice)*