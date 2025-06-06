# ICEXIFOrientationType

**Framework**: ImageCaptureCore  
**Kind**: enum

The file’s orientation type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
enum ICEXIFOrientationType
```

#### Overview

The meaning of this value is defined by the `EXIF` specification. Here is what the letter  would look like if it were tagged correctly and displayed by a program that ignores the orientation tag (thus showing the stored image):

```swift
               1             2             3             4

            8888888       8888888            88       88
            88                 88            88       88
            8888             8888          8888       8888
            88                 88            88       88
            88                 88       8888888       8888888

               5             6             7             8

            8888888888    88                    88    8888888888
            88  88        88  88            88  88        88  88
            88            8888888888    8888888888            88
```

## Topics

### Constants
- [ICEXIFOrientationType.orientation1](icexiforientationtype/orientation1.md)
  Normal
- [ICEXIFOrientationType.orientation2](icexiforientationtype/orientation2.md)
  Flipped horizontally
- [ICEXIFOrientationType.orientation3](icexiforientationtype/orientation3.md)
  Rotated 180°
- [ICEXIFOrientationType.orientation4](icexiforientationtype/orientation4.md)
  Flipped vertically
- [ICEXIFOrientationType.orientation5](icexiforientationtype/orientation5.md)
  Rotated 90° CCW and flipped vertically
- [ICEXIFOrientationType.orientation6](icexiforientationtype/orientation6.md)
  Rotated 90° CCW
- [ICEXIFOrientationType.orientation7](icexiforientationtype/orientation7.md)
  Rotated 90° CW and flipped vertically
- [ICEXIFOrientationType.orientation8](icexiforientationtype/orientation8.md)
  Rotated 90° CW
### Initializers
- [init?(rawValue: UInt)](icexiforientationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var orientation: ICEXIFOrientationType](iccamerafile/orientation.md)
  The orientation to use when downloading the image.
- [var exifCreationDate: Date?](iccamerafile/exifcreationdate.md)
  The `EXIF` creation date of the file.
- [var exifModificationDate: Date?](iccamerafile/exifmodificationdate.md)
  The `EXIF` modification date of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icexiforientationtype)*