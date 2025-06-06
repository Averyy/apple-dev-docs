# fixed(_:)

**Framework**: SwiftUI  
**Kind**: method

An explicit tint color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static func fixed(_ tint: Color) -> ListItemTint
```

#### Discussion

The system doesn’t override this tint effect.

## Parameters

- `tint`: The color to use to tint the content.

## See Also

- [static let monochrome: ListItemTint](listitemtint/monochrome.md)
  A standard grayscale tint effect.
- [static func preferred(Color) -> ListItemTint](listitemtint/preferred(_:).md)
  An explicit tint color that the system can override.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/listitemtint/fixed(_:))*