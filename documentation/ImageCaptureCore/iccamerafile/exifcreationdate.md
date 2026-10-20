# exifCreationDate

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The `EXIF` creation date of the file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var exifCreationDate: Date? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDate * exifCreationDate;
```

## See Also

### Inspecting a File’s EXIF Data
- [var orientation: ICEXIFOrientationType](./orientation.md)
  The orientation to use when downloading the image.
- [enum ICEXIFOrientationType](../icexiforientationtype.md)
  The file’s orientation type.
- [var exifModificationDate: Date?](./exifmodificationdate.md)
  The `EXIF` modification date of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/exifcreationdate)*