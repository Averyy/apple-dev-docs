# pairedRawImage

**Framework**: ImageCaptureCore  
**Kind**: property

A sidecar file containing the logical `RAW` compliment of a `JPG` or other two-format image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var pairedRawImage: ICCameraFile? { get }
```

#### Discussion

This value contains a single-item subset of the [`sidecarFiles`](iccamerafile/sidecarfiles.md) array.

## See Also

- [var sidecarFiles: [ICCameraItem]?](iccamerafile/sidecarfiles.md)
  An array of two camera files associated with this file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/pairedrawimage)*