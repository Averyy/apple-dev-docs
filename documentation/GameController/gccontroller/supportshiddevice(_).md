# supportsHIDDevice(_:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the framework supports the specified human interface device.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func supportsHIDDevice(_ device: IOHIDDevice) -> Bool
```

```objc
+ (BOOL) supportsHIDDevice:(IOHIDDeviceRef) device;
```

## Return Value

[`true`](../../Swift/true.md) if the framework supports the device; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the Game Controller framework supports the input device, you can use the Game Controller APIs to interact with the device instead of the IOKit APIs.

## Parameters

- `device`: A human interface input device.

## See Also

### Inspecting a controller
- [var isAttachedToDevice: Bool](./isattachedtodevice.md)
  A Boolean value that indicates whether the controller closely integrates with the device.
- [class var shouldMonitorBackgroundEvents: Bool](./shouldmonitorbackgroundevents.md)
  A Boolean value that indicates whether the app needs to respond to controller events when it isn’t the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/supportshiddevice(_:))*