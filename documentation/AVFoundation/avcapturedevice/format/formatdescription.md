# formatDescription

**Framework**: AVFoundation  
**Kind**: property

An object describing the capture format.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var formatDescription: CMFormatDescription { get }
```

#### Discussion

Calling this method doesn’t assume ownership of the returned [`CMFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription).

## See Also

- [var mediaType: AVMediaType](avcapturedevice/format/mediatype.md)
  A constant describing the media type of an `AVCaptureDevice` active or supported format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/formatdescription)*