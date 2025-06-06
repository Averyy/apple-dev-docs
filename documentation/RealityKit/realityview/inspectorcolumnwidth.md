# inspectorColumnWidth(_:)

**Framework**: Realitykit  
**Kind**: method

Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+

## Declaration

```swift
nonisolated
func inspectorColumnWidth(_ width: CGFloat) -> some View
```

#### Discussion

Apply this modifier on the content of a `View/inspector(isPresented:content:)` to specify a fixed preferred width for the trailing column. Use `View/inspectorColumnWidth(min:ideal:max:)` if you need to specify a flexible width.

The following example shows an editor interface with an inspector, which when presented as a trailing-column, has a fixed width of 225 points. The example also uses `View/interactiveDismissDisabled(_:)` to prevent the inspector from being collapsed by user action like dragging a divider.

```None
MyEditorView()
    .inspector {
        TextTraitsInspectorView()
            .inspectorColumnWidth(225)
            .interactiveDismissDisabled()
    }
```

> **Note**: A fixed width does not prevent the user collapsing the inspector on macOS. See `View/interactiveDismissDisabled(_:)`.

## Parameters

- `width`: The preferred fixed width for the inspector if   presented as a trailing column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/inspectorcolumnwidth(_:))*