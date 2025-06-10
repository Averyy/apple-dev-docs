# inspector(isPresented:content:)

**Framework**: FamilyControls  
**Kind**: method

Inserts an inspector at the applied position in the view hierarchy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func inspector<V>(isPresented: Binding<Bool>, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Discussion

Apply this modifier to declare an inspector with a context-dependent presentation. For example, an inspector can present as a trailing column in a horizontally regular size class, but adapt to a sheet in a horizontally compact size class.

```swift
struct ShapeEditor: View {
    @State var presented: Bool = false
    var body: some View {
        MyEditorView()
            .inspector(isPresented: $presented) {
                TextTraitsInspectorView()
            }
    }
}
```

> **Note**: Trailing column inspectors have their presentation state restored by the framework.

> **Note**: `InspectorCommands` for including the default inspector commands and keyboard shortcuts.

## Parameters

- `isPresented`: A binding to   controlling the presented state.
- `content`: The inspector content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/inspector(ispresented:content:))*