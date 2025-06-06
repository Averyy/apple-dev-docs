# ToolbarContent

**Framework**: SwiftUI  
**Kind**: protocol

Conforming types represent items that can be placed in various locations in a toolbar.

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
@MainActor
@preconcurrency protocol ToolbarContent
```

#### Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Implementing toolbar content
- [var body: Self.Body](toolbarcontent/body-swift.property.md)
  The composition of content that comprise the toolbar content.
- [associatedtype Body : ToolbarContent](toolbarcontent/body-swift.associatedtype.md)
  The type of content representing the body of this toolbar content.
### Instance Methods
- [func hidden(Bool) -> some ToolbarContent](toolbarcontent/hidden(_:).md)
  Hides a toolbar item within its toolbar.

## Relationships

### Inherited By
- [CustomizableToolbarContent](customizabletoolbarcontent.md)
### Conforming Types
- [Group](group.md)
- [ToolbarItem](toolbaritem.md)
- [ToolbarItemGroup](toolbaritemgroup.md)
- [ToolbarTitleMenu](toolbartitlemenu.md)

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent)*