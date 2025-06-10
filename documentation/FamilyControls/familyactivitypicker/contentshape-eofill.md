# contentShape(_:_:eoFill:)

**Framework**: FamilyControls  
**Kind**: method

Sets the content shape for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func contentShape<S>(_ kind: ContentShapeKinds, _ shape: S, eoFill: Bool = false) -> some View where S : Shape
```

#### Return Value

A view that uses the given shape for the specified kind.

#### Discussion

The content shape has a variety of uses. You can control the kind of the content shape by specifying one in `kind`. The following example sets the focus ring shape of the view, without affecting its shape for hit-testing:

```swift
MyFocusableView()
    .contentShape(.focusEffect, Circle())
```

You can apply multiple kinds of content shapes to the same view. For example, apply a `ContentShapeKinds/interaction` shape and `ContentShapeKinds/focusEffect` shape together to set both the hit-testing shape and focus ring shape on a view.

#### Context Menu Drag Previews

You can control the preview shown by the system for context menus or drags using the relevant content shape kind, like `ContentShapeKinds/dragPreview` and `ContentShapeKinds/contextMenuPreview`.

The following example creates a `VStack` of an `Image` and `Text` that has a context menu with a custom content shape:

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

When someone activates the context menu with an action like touch and hold in iOS or iPadOS, the system uses the `Image` as the preview for the context menu, applying the requested corner radius.

The content shape also supports applying modifiers such as `InsettableShape/inset(by:)` to add padding.

> **Note**: Similar to `ContentShapeKinds/focusEffect`, the `ContentShapeKinds/contextMenuPreview` and `ContentShapeKinds/dragPreview` content shapes do not impact the hit-testing shape. In this example, someone can touch and hold anywhere on the `VStack` to activate the menu. If you only want the `Image` to activate the menu, apply `View/contextMenu(menuItems:)` to the `Image` instead.

## Parameters

- `kind`: The kinds to apply to this content shape.
- `shape`: The shape to use.
- `eoFill`: A Boolean that indicates whether the shape is interpreted   with the even-odd winding number rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/contentshape(_:_:eofill:))*