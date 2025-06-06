# inspectorColumnWidth(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func inspectorColumnWidth(_ width: CGFloat) -> some View
```

#### Discussion

Apply this modifier on the content of a [`inspector(isPresented:content:)`](view/inspector(ispresented:content:).md) to specify a fixed preferred width for the trailing column. Use [`inspectorColumnWidth(min:ideal:max:)`](view/inspectorcolumnwidth(min:ideal:max:).md) if you need to specify a flexible width.

The following example shows an editor interface with an inspector, which when presented as a trailing-column, has a fixed width of 225 points. The example also uses [`interactiveDismissDisabled(_:)`](view/interactivedismissdisabled(_:).md) to prevent the inspector from being collapsed by user action like dragging a divider.

```swift
MyEditorView()
    .inspector {
        TextTraitsInspectorView()
            .inspectorColumnWidth(225)
            .interactiveDismissDisabled()
    }
```

> **Note**: A fixed width does not prevent the user collapsing the inspector on macOS. See [`interactiveDismissDisabled(_:)`](view/interactivedismissdisabled(_:).md).

A fixed width does not prevent the user collapsing the inspector on macOS. See [`interactiveDismissDisabled(_:)`](view/interactivedismissdisabled(_:).md).

## Parameters

- `width`: The preferred fixed width for the inspector if   presented as a trailing column.

## See Also

- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](view/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/inspectorcolumnwidth(_:))*