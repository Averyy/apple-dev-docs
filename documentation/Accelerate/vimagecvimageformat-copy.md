# vImageCVImageFormat_Copy(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a mutable copy of an immutable Core Video image format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCVImageFormat_Copy(_ format: vImageConstCVImageFormat) -> Unmanaged<vImageCVImageFormat>!
```

#### Return Value

A [`vImageCVImageFormat`](vimagecvimageformat.md) instance.

#### Discussion

This function doesn’t copy the image format’s user data or the release callback.

## Parameters

- `format`: The Core Video image format to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_copy(_:))*