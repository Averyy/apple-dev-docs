# ToolbarCustomizationOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Options that influence the default customization behavior of customizable toolbar content.

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
struct ToolbarCustomizationOptions
```

#### Overview

Use this type in conjunction with the [`defaultCustomization(_:options:)`](./customizabletoolbarcontent/defaultcustomization%28_,options%29.md) modifier.

## Topics

### Getting customization options
- [static var alwaysAvailable: ToolbarCustomizationOptions](./toolbarcustomizationoptions/alwaysavailable.md)
  Configures default customizable toolbar content to always be present in the toolbar.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Populating a customizable toolbar
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](./view/toolbar%28id,content%29.md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbarItemHidden(Bool) -> some View](./view/toolbaritemhidden%28_%29.md)
  Hides an individual view within a control group toolbar item.
- [protocol CustomizableToolbarContent](./customizabletoolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [struct ToolbarCustomizationBehavior](./toolbarcustomizationbehavior.md)
  The customization behavior of customizable toolbar content.
- [struct SearchToolbarBehavior](./searchtoolbarbehavior.md)
  The behavior of a search field in a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcustomizationoptions)*