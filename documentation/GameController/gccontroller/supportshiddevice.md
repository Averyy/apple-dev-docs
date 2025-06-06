# supportsHIDDevice(_:)

**Framework**: Game Controller  
**Kind**: method

Returns a Boolean value that indicates whether the framework supports the specified human interface device.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func supportsHIDDevice(_ device: IOHIDDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the framework supports the device; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the Game Controller framework supports the input device, you can use the Game Controller APIs to interact with the device instead of the IOKit APIs.

## Parameters

- `device`: A human interface input device.

## See Also

- [var isAttachedToDevice: Bool](gccontroller/isattachedtodevice.md)
  A Boolean value that indicates whether the controller closely integrates with the device.
- [class var shouldMonitorBackgroundEvents: Bool](gccontroller/shouldmonitorbackgroundevents.md)
  A Boolean value that indicates whether the app needs to respond to controller events when it isn’t the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/supportshiddevice(_:))*