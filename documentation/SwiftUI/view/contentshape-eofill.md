# contentShape(_:_:eoFill:)

**Framework**: SwiftUI  
**Kind**: method

Sets the content shape for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func contentShape<S>(_ kind: ContentShapeKinds, _ shape: S, eoFill: Bool = false) -> some View where S : Shape
```

## Mentions

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

#### Return Value

A view that uses the given shape for the specified kind.

#### Discussion

The content shape has a variety of uses. You can control the kind of the content shape by specifying one in `kind`. The following example sets the focus ring shape of the view, without affecting its shape for hit-testing:

```swift
MyFocusableView()
    .contentShape(.focusEffect, Circle())
```

You can apply multiple kinds of content shapes to the same view. For example, apply a [`interaction`](contentshapekinds/interaction.md) shape and [`focusEffect`](contentshapekinds/focuseffect.md) shape together to set both the hit-testing shape and focus ring shape on a view.

#### Context Menu Drag Previews

You can control the preview shown by the system for context menus or drags using the relevant content shape kind, like [`dragPreview`](contentshapekinds/dragpreview.md) and [`contextMenuPreview`](contentshapekinds/contextmenupreview.md).

The following example creates a [`VStack`](vstack.md) of an [`Image`](image.md) and [`Text`](text.md) that has a context menu with a custom content shape:

```swift
VStack {
    Image("turtlerock")
        .contentShape(.contextMenuPreview,
                      RoundedRectangle(cornerRadius: 10))
    Text("Turtle Rock")
}
.contextMenu {
    Button {
        // Add this item to a list of favorites.
    } label: {
        Label("Add to Favorites", systemImage: "heart")
    }
}
```

When someone activates the context menu with an action like touch and hold in iOS or iPadOS, the system uses the [`Image`](image.md) as the preview for the context menu, applying the requested corner radius.

The content shape also supports applying modifiers such as [`inset(by:)`](insettableshape/inset(by:).md) to add padding.

> **Note**: Similar to [`focusEffect`](contentshapekinds/focuseffect.md), the [`contextMenuPreview`](contentshapekinds/contextmenupreview.md) and [`dragPreview`](contentshapekinds/dragpreview.md) content shapes do not impact the hit-testing shape. In this example, someone can touch and hold anywhere on the [`VStack`](vstack.md) to activate the menu. If you only want the [`Image`](image.md) to activate the menu, apply [`contextMenu(menuItems:)`](view/contextmenu(menuitems:).md) to the [`Image`](image.md) instead.

Similar to [`focusEffect`](contentshapekinds/focuseffect.md), the [`contextMenuPreview`](contentshapekinds/contextmenupreview.md) and [`dragPreview`](contentshapekinds/dragpreview.md) content shapes do not impact the hit-testing shape. In this example, someone can touch and hold anywhere on the [`VStack`](vstack.md) to activate the menu. If you only want the [`Image`](image.md) to activate the menu, apply [`contextMenu(menuItems:)`](view/contextmenu(menuitems:).md) to the [`Image`](image.md) instead.

## Parameters

- `kind`: The kinds to apply to this content shape.
- `shape`: The shape to use.
- `eoFill`: A Boolean that indicates whether the shape is interpreted   with the even-odd winding number rule.

## See Also

- [func allowsTightening(Bool) -> some View](view/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func contentShape<S>(S, eoFill: Bool) -> some View](view/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [struct ContentShapeKinds](contentshapekinds.md)
  A kind for the content shape of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contentshape(_:_:eofill:))*