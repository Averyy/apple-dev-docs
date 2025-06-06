# ContentMode.fill

**Framework**: SwiftUI  
**Kind**: case

An option that resizes the content so it occupies all available space, both vertically and horizontally.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case fill
```

## Mentions

- [Fitting images into available space](fitting-images-into-available-space.md)

#### Discussion

This mode preserves the content’s aspect ratio. If the content doesn’t have the same aspect ratio as the available space, the content becomes the same size as the available space on one axis, and larger on the other axis.

## See Also

- [ContentMode.fit](contentmode/fit.md)
  An option that resizes the content so it’s all within the available space, both vertically and horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmode/fill)*