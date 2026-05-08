# Image.DynamicRange

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct DynamicRange
```

## Topics

### Getting dynamic range values
- [static let standard: Image.DynamicRange](image/dynamicrange/standard.md)
  Restrict the image content dynamic range to the standard range.
- [static let high: Image.DynamicRange](image/dynamicrange/high.md)
  Allow image content to use an unrestricted extended range.
- [static let constrainedHigh: Image.DynamicRange](image/dynamicrange/constrainedhigh.md)
  Allow image content to use some extended range. This is appropriate for placing HDR content next to SDR content.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func allowedDynamicRange(Image.DynamicRange?) -> Image](image/alloweddynamicrange(_:).md)
  Returns a new image configured with the specified allowed dynamic range.
- [var allowedDynamicRange: Image.DynamicRange?](environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/dynamicrange)*