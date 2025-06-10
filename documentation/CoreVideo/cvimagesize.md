# CVImageSize

**Framework**: Core Video  
**Kind**: struct

Size of image buffer expressed as pixel count.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct CVImageSize
```

#### Overview

This should be used when the sizes must be specified as exact integer width & height. Otherwise, prefer `CGSize` as it is more widely used.

## Topics

### Initializers
- [init(CGSize, rounded: FloatingPointRoundingRule)](cvimagesize/init(_:rounded:).md)
  Convert `CGSize` to [`CVImageSize`](cvimagesize.md) using the given rounding rule.
- [init(width: Int, height: Int)](cvimagesize/init(width:height:).md)
  Create an instance with given width and height
### Instance Properties
- [var height: Int](cvimagesize/height.md)
  Image height in pixels
- [var width: Int](cvimagesize/width.md)
  Image width in pixels
### Type Properties
- [static let zero: CVImageSize](cvimagesize/zero.md)
  Size with zero width and height

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagesize)*