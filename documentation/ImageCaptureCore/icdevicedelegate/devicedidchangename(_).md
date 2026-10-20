# deviceDidChangeName(_:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the name of a device changes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func deviceDidChangeName(_ device: ICDevice)
```

```objc
- (void) deviceDidChangeName:(ICDevice *) device;
```

#### Discussion

This happens if the device module overrides the default name of the device reported by the device’s transport layer, or if the name of the filesystem volume mounted by the device is changed by the user.

Execution of the delegate callback occurs on the main thread.

## See Also

### Responding to Device Changes
- [func deviceDidChangeSharingState(ICDevice)](./devicedidchangesharingstate%28_%29.md)
  Tells the delegate when the sharing state of a device changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicedelegate/devicedidchangename(_:))*