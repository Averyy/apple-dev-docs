# ListItemTint

**Framework**: SwiftUI  
**Kind**: struct

A tint effect configuration that you can apply to content in a list.

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
struct ListItemTint
```

#### Overview

Use one of these tint values with the [`listItemTint(_:)`](view/listitemtint(_:).md) view modifier. The containing list applies the tint in a platform-specific way.

## Topics

### Getting list item tint options
- [static let monochrome: ListItemTint](listitemtint/monochrome.md)
  A standard grayscale tint effect.
- [static func fixed(Color) -> ListItemTint](listitemtint/fixed(_:).md)
  An explicit tint color.
- [static func preferred(Color) -> ListItemTint](listitemtint/preferred(_:).md)
  An explicit tint color that the system can override.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func listItemTint(_:)](view/listitemtint(_:).md)
  Sets a fixed tint color for content in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/listitemtint)*