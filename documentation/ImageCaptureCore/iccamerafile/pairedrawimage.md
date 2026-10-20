# pairedRawImage

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) ICCameraFile * pairedRawImage;
```

#### Discussion

This value contains a single-item subset of the [`sidecarFiles`](./sidecarfiles.md) array.

## See Also

### Identifying Related Files
- [var sidecarFiles: [ICCameraItem]?](./sidecarfiles.md)
  An array of two camera files associated with this file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/pairedrawimage)*