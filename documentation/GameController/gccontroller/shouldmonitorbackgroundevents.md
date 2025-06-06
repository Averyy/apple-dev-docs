# shouldMonitorBackgroundEvents

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the app needs to respond to controller events when it isn’t the frontmost app.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
class var shouldMonitorBackgroundEvents: Bool { get set }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false), and the app isn’t in the foreground, the framework doesn’t forward any input from the game controller until the app becomes the frontmost.

> **Note**:  In macOS 11.3 and later, the default value for this property is [`false`](https://developer.apple.com/documentation/swift/false). Prior to macOS 11.3, the default value is [`true`](https://developer.apple.com/documentation/swift/true). In iOS and tvOS, the framework ignores this property.

 In macOS 11.3 and later, the default value for this property is [`false`](https://developer.apple.com/documentation/swift/false). Prior to macOS 11.3, the default value is [`true`](https://developer.apple.com/documentation/swift/true). In iOS and tvOS, the framework ignores this property.

## See Also

- [var isAttachedToDevice: Bool](gccontroller/isattachedtodevice.md)
  A Boolean value that indicates whether the controller closely integrates with the device.
- [class func supportsHIDDevice(IOHIDDevice) -> Bool](gccontroller/supportshiddevice(_:).md)
  Returns a Boolean value that indicates whether the framework supports the specified human interface device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/shouldmonitorbackgroundevents)*