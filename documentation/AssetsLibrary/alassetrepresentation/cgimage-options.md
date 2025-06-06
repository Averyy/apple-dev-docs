# cgImage(options:)

**Framework**: Assetslibrary  
**Kind**: method

Returns a full resolution CGImage of the representation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func cgImage(options: [AnyHashable : Any]! = [:]) -> Unmanaged<CGImage>!
```

#### Return Value

A full resolution CGImage of the representation.

#### Discussion

This method provides a convenient way to obtain a CGImage representation of an asset. This method returns the biggest, best representation available.

> **Note**:  In iOS 8 and later, use the Photos framework to access different versions and sizes of a photo asset. See [`PHImageManager`](https://developer.apple.com/documentation/Photos/PHImageManager).

## Parameters

- `options`: A dictionary of options as described for   or  .

## See Also

- [func fullResolutionImage() -> Unmanaged<CGImage>!](alassetrepresentation/fullresolutionimage.md)
  Returns a CGImage representation of the asset.
- [func fullScreenImage() -> Unmanaged<CGImage>!](alassetrepresentation/fullscreenimage.md)
  Returns a CGImage of the representation that is appropriate for displaying full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/cgimage(options:))*