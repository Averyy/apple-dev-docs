# scrollBounceBehavior(_:axes:)

**Framework**: PermissionKit  
**Kind**: method

Configures the bounce behavior of scrollable views along the specified axis.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 26.0+ (Beta)
- watchOS 9.4+

## Declaration

```swift
nonisolated
func scrollBounceBehavior(_ behavior: ScrollBounceBehavior, axes: Axis.Set = [.vertical]) -> some View
```

#### Return Value

A view that’s configured with the specified scroll bounce behavior.

#### Discussion

Use this modifier to indicate whether scrollable views bounce when people scroll to the end of the view’s content, taking into account the relative sizes of the view and its content. For example, the following `ScrollView` only enables bounce behavior if its content is large enough to require scrolling:

```None
ScrollView {
    Text("Small")
    Text("Content")
}
.scrollBounceBehavior(.basedOnSize)
```

The modifier passes the scroll bounce mode through the `Environment`, which means that the mode affects any scrollable views in the modified view hierarchy. Provide an axis to the modifier to constrain the kinds of scrollable views that the mode affects. For example, all the scroll views in the following example can access the mode value, but only the two nested scroll views are affected, because only they use horizontal scrolling:

```None
ScrollView { // Defaults to vertical scrolling.
    ScrollView(.horizontal) {
        ShelfContent()
    }
    ScrollView(.horizontal) {
        ShelfContent()
    }
}
.scrollBounceBehavior(.basedOnSize, axes: .horizontal)
```

You can use this modifier to configure any kind of scrollable view, including `ScrollView`, `List`, `Table`, and `TextEditor`:

```None
List {
    Text("Hello")
    Text("World")
}
.scrollBounceBehavior(.basedOnSize)
```

## Parameters

- `behavior`: The bounce behavior to apply to any scrollable views   within the configured view. Use one of the    values.
- `axes`: The set of axes to apply   to. The default is   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/scrollbouncebehavior(_:axes:))*