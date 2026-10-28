# AVCaptureDevice.AutoFocusRangeRestriction.near

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The device primarily attempts to focus on subjects near the camera.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
case near
```

```c
AVCaptureAutoFocusRangeRestrictionNear
```

## Discussion

You should use this value if your app uses [`AVCaptureMetadataOutput`](../../avcapturemetadataoutput.md) to recognize machine-readable codes.

## See Also

### Constants
- [AVCaptureDevice.AutoFocusRangeRestriction.none](./none.md)
  The device attempts to focus on objects at any range.
- [AVCaptureDevice.AutoFocusRangeRestriction.far](./far.md)
  The device primarily attempts to focus on subjects far away from the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/near)*