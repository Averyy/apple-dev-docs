# ToolbarCustomizationBehavior

**Framework**: SwiftUI  
**Kind**: struct

The customization behavior of customizable toolbar content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ToolbarCustomizationBehavior
```

#### Overview

Customizable toolbar content support different types of customization behaviors. For example, some customizable content may not be removed by the user. Some content may be placed in a toolbar that supports customization overall, but not for that particular content.

Use this type in conjunction with the [`customizationBehavior(_:)`](customizabletoolbarcontent/customizationbehavior(_:).md) modifier.

## Topics

### Getting customization behaviors
- [static var `default`: ToolbarCustomizationBehavior](toolbarcustomizationbehavior/default.md)
  The default customization behavior.
- [static var disabled: ToolbarCustomizationBehavior](toolbarcustomizationbehavior/disabled.md)
  The disabled customization behavior.
- [static var reorderable: ToolbarCustomizationBehavior](toolbarcustomizationbehavior/reorderable.md)
  The reorderable customization behavior.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [protocol CustomizableToolbarContent](customizabletoolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [struct ToolbarCustomizationOptions](toolbarcustomizationoptions.md)
  Options that influence the default customization behavior of customizable toolbar content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcustomizationbehavior)*