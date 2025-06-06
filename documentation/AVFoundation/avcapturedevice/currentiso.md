# currentISO

**Framework**: Avfoundation  
**Kind**: property

A constant to indicate not to specify a new ISO value, and instead set it to its current value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class let currentISO: Float
```

#### Discussion

A special value that you may pass as the ISO parameter of the [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) method to indicate that the caller doesn’t specify a value for the ISO property, and to instead set to its current value.

> **Note**:  A device may be adjusting ISO at the time of the call, in which case the value set may differ from the value of thee [`iso`](avcapturedevice/iso.md) property.

## See Also

- [class let currentExposureDuration: CMTime](avcapturedevice/currentexposureduration.md)
  A special constant representing the current exposure duration setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentiso)*