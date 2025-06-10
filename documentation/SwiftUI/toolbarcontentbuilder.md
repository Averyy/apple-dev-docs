# ToolbarContentBuilder

**Framework**: SwiftUI  
**Kind**: struct

Constructs a toolbar item set from multi-expression closures.

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
@resultBuilder
struct ToolbarContentBuilder
```

## Topics

### Building toolbar content
- [static buildBlock(_:)](toolbarcontentbuilder/buildblock(_:).md)
- [static buildBlock(_:_:)](toolbarcontentbuilder/buildblock(_:_:).md)
- [static buildBlock(_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:).md)
- [static buildBlock(_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:).md)
- [static buildBlock(_:_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:_:).md)
- [static buildBlock(_:_:_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:_:_:).md)
- [static buildBlock(_:_:_:_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static buildBlock(_:_:_:_:_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static buildBlock(_:_:_:_:_:_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
- [static buildBlock(_:_:_:_:_:_:_:_:_:_:)](toolbarcontentbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
### Building conditional toolbar content
- [static buildIf(_:)](toolbarcontentbuilder/buildif(_:).md)
- [static buildEither(first:)](toolbarcontentbuilder/buildeither(first:).md)
- [static buildEither(second:)](toolbarcontentbuilder/buildeither(second:).md)
- [static buildExpression(_:)](toolbarcontentbuilder/buildexpression(_:).md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](toolbarcontentbuilder/buildlimitedavailability(_:).md)

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarSpacer](toolbarspacer.md)
  A standard space item in toolbars.
- [struct DefaultToolbarItem](defaulttoolbaritem.md)
  A toolbar item that represents a system component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder)*