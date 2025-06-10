# SearchToolbarBehavior

**Framework**: SwiftUI  
**Kind**: struct

The behavior of a search field in a toolbar.

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
struct SearchToolbarBehavior
```

#### Overview

Use this type in combination with the [`searchToolbarBehavior(_:)`](view/searchtoolbarbehavior(_:).md) modifier.

## Topics

### Type Properties
- [static var automatic: SearchToolbarBehavior](searchtoolbarbehavior/automatic.md)
  The automatic behavior.
- [static var minimize: SearchToolbarBehavior](searchtoolbarbehavior/minimize.md)
  A search toolbar behavior that prefers rendering a search field as a button-like control.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [protocol CustomizableToolbarContent](customizabletoolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [struct ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md)
  The customization behavior of customizable toolbar content.
- [struct ToolbarCustomizationOptions](toolbarcustomizationoptions.md)
  Options that influence the default customization behavior of customizable toolbar content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/searchtoolbarbehavior)*