# fullResolutionImage()

**Framework**: Assets Library  
**Kind**: method

Returns a CGImage representation of the asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func fullResolutionImage() -> Unmanaged<CGImage>!
```

#### Return Value

A `CGImage` representation of the asset, or `NULL` if a CGImage representation could not be generated.

#### Discussion

This method returns the biggest, best representation available.

To create a correctly-rotated UIImage object from the CGImage, you use [`imageWithCGImage:scale:orientation:`](https://developer.apple.com/documentation/uikit/uiimage/1624124-imagewithcgimage) or [`init(cgImage:scale:orientation:)`](https://developer.apple.com/documentation/UIKit/UIImage/init(cgImage:scale:orientation:)), passing the values of [`orientation()`](alassetrepresentation/orientation().md) and [`scale()`](alassetrepresentation/scale().md).

> **Note**:  In iOS 8 and later, use the Photos framework to access different versions and sizes of a photo asset. See [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager).

## See Also

- [func cgImage(options: [AnyHashable : Any]!) -> Unmanaged<CGImage>!](alassetrepresentation/cgimage(options:).md)
  Returns a full resolution CGImage of the representation.
- [func fullScreenImage() -> Unmanaged<CGImage>!](alassetrepresentation/fullscreenimage.md)
  Returns a CGImage of the representation that is appropriate for displaying full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/fullresolutionimage())*