# fullScreenImage()

**Framework**: Assets Library  
**Kind**: method

Returns a CGImage of the representation that is appropriate for displaying full screen.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func fullScreenImage() -> Unmanaged<CGImage>!
```

#### Return Value

A CGImage of the representation that is appropriate for displaying full screen, or `NULL` if a CGImage representation could not be generated.

#### Discussion

The dimensions of the image are dependent on the device your application is running on; the dimensions may not, however, exactly match the dimensions of the screen.

In iOS 5 and later, this method returns a fully cropped, rotated, and adjusted image—exactly as a user would see in Photos or in the image picker.

> **Note**:  In iOS 8 and later, use the Photos framework to access different versions and sizes of a photo asset. See [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager).

## See Also

- [func cgImage(options: [AnyHashable : Any]!) -> Unmanaged<CGImage>!](alassetrepresentation/cgimage(options:).md)
  Returns a full resolution CGImage of the representation.
- [func fullResolutionImage() -> Unmanaged<CGImage>!](alassetrepresentation/fullresolutionimage.md)
  Returns a CGImage representation of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/fullscreenimage())*