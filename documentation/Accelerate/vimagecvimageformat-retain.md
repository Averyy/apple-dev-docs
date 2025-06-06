# vImageCVImageFormat_Retain

**Framework**: Accelerate  
**Kind**: func

Retains a Core Video image format.

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
void vImageCVImageFormat_Retain(vImageCVImageFormatRef fmt);
```

#### Discussion

This function increments the Core Video image format’s reference count.

## Parameters

- `fmt`: The Core Video image format to retain.

## See Also

- [vImageCVImageFormat_Release](vimagecvimageformat_release.md)
  Releases a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_retain)*