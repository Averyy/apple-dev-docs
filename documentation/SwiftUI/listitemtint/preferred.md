# preferred(_:)

**Framework**: SwiftUI  
**Kind**: method

An explicit tint color that the system can override.

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
static func preferred(_ tint: Color) -> ListItemTint
```

#### Discussion

The system can override this tint effect, like when the system has a custom user accent color on macOS.

## Parameters

- `tint`: The color to use to tint the content.

## See Also

- [static let monochrome: ListItemTint](listitemtint/monochrome.md)
  A standard grayscale tint effect.
- [static func fixed(Color) -> ListItemTint](listitemtint/fixed(_:).md)
  An explicit tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/listitemtint/preferred(_:))*