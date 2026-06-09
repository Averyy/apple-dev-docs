# closest(to:)

**Framework**: Image Playground  
**Kind**: method

Creates a new instance of this structure with a size value that best matches the specified size.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func closest(to size: CGSize) -> ImagePlaygroundOptions.SizeSpecification
```

#### Return Value

A structure with a supported size that most closely matches the requested value in `size`.

#### Discussion

This method finds the supported image size that’s closest to the value in the `size` parameter. The method considers both the resolution and aspect ratio of the requested size when choosing the output size.

## Parameters

- `size`: The image size you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/sizespecification-swift.struct/closest(to:))*