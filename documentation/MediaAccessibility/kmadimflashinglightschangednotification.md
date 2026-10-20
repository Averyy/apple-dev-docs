# kMADimFlashingLightsChangedNotification

**Framework**: Media Accessibility  
**Kind**: var  
**Role**: Global Variable

A notification that posts when a person changes the flashing lights setting on the device.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
let kMADimFlashingLightsChangedNotification: CFString
```

```c
extern CFStringRef const kMADimFlashingLightsChangedNotification;
```

## See Also

### Dim flashing lights
- [Responding to changes in the flashing lights setting](./responding-to-changes-in-the-flashing-lights-setting.md)
  Adjust your UI when a person chooses to dim flashing lights on their Apple device.
- [func MADimFlashingLightsEnabled() -> Bool](./madimflashinglightsenabled%28%29.md)
  Returns a Boolean value that indicates whether the flashing lights setting is enabled on the device.
- [class MAFlashingLightsProcessor](./maflashinglightsprocessor.md)
  A class that processes a framebuffer object to detect and dim sequences of flashing lights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/kmadimflashinglightschangednotification)*