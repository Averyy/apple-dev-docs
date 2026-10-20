# physicalInputProfile

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The device’s physical input profile, such as a controller’s extended gamepad.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS 11.0+ - Deprecated in 13.0
- tvOS 14.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the physicalInputProfile property on GCController instead.  For GCKeyboard, use the keyboardInput property.  For GCMouse, use the mouseInput property.

## Declaration

```swift
var physicalInputProfile: GCPhysicalInputProfile { get }
```

```objc
@property (nonatomic, strong, readonly) GCPhysicalInputProfile * physicalInputProfile;
```

## See Also

### Handling input
- [var handlerQueue: dispatch_queue_t](./handlerqueue.md)
  The dispatch queue that the framework uses to call element value change handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevice/physicalinputprofile)*