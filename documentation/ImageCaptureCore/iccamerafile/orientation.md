# orientation

**Framework**: ImageCaptureCore  
**Kind**: property

The orientation to use when downloading the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var orientation: ICEXIFOrientationType { get set }
```

#### Discussion

This property is initially set to [`ICEXIFOrientationType.orientation1`](icexiforientationtype/orientation1.md) If the format of the file supports the `EXIF` orientation tag, then this property updates to match the value of that tag on receipt of the thumbnail or metadata for this file.

## See Also

- [enum ICEXIFOrientationType](icexiforientationtype.md)
  The file’s orientation type.
- [var exifCreationDate: Date?](iccamerafile/exifcreationdate.md)
  The `EXIF` creation date of the file.
- [var exifModificationDate: Date?](iccamerafile/exifmodificationdate.md)
  The `EXIF` modification date of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/orientation)*