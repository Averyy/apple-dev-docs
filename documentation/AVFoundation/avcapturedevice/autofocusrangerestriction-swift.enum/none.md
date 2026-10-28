# AVCaptureDevice.AutoFocusRangeRestriction.none

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The device attempts to focus on objects at any range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
case none
```

```c
AVCaptureAutoFocusRangeRestrictionNone
```

## Discussion

This value is the default, and the only value allowed on devices that do not support focus range restriction.

## See Also

### Constants
- [AVCaptureDevice.AutoFocusRangeRestriction.near](./near.md)
  The device primarily attempts to focus on subjects near the camera.
- [AVCaptureDevice.AutoFocusRangeRestriction.far](./far.md)
  The device primarily attempts to focus on subjects far away from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/none)*