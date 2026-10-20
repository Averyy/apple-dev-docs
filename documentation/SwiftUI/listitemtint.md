# ListItemTint

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

Use one of these tint values with the [`listItemTint(_:)`](./view/listitemtint%28_%29.md) view modifier. The containing list applies the tint in a platform-specific way. On iOS and macOS, sidebars apply the tint color to [`Label`](./label.md) icons, which otherwise use the app’s accent color by default.

## Topics

### Getting list item tint options
- [static let monochrome: ListItemTint](./listitemtint/monochrome.md)
  A standard grayscale tint effect.
- [static func fixed(Color) -> ListItemTint](./listitemtint/fixed%28_%29.md)
  An explicit tint color.
- [static func preferred(Color) -> ListItemTint](./listitemtint/preferred%28_%29.md)
  An explicit tint color that the system can override.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring rows
- [func listItemTint(_:)](./view/listitemtint%28_%29.md)
  Sets a fixed tint color for content in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/listitemtint)*