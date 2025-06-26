# focusedObject(_:)

**Framework**: FamilyControls  
**Kind**: method

Creates a new view that exposes the provided object to other views whose state depends on the focused view hierarchy.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func focusedObject<T>(_ object: T?) -> some View where T : ObservableObject
```

#### Return Value

A view that supplies an observable object when in focus.

#### Discussion

Use this method instead of `View/focusedSceneObject(_:)` when your scene includes multiple focusable views with their own associated data, and you need an app- or scene-scoped element like a command or toolbar item that operates on the data associated with whichever view currently has focus. Each focusable view can supply its own object:

```swift
struct MessageView: View {
    @StateObject private var message = Message(...)

    var body: some View {
        TextField(...)
            .focusedObject(message)
    }
}
```

Interested views can then use the `FocusedObject` property wrapper to observe and update the focused view’s object. In this example, an app command updates the focused view’s data, and is automatically disabled when focus is in an unrelated part of the scene:

```swift
struct MessageCommands: Commands {
    @FocusedObject private var message: Message?

    var body: some Commands {
        CommandGroup(after: .pasteboard) {
            Button("Add Duck to Message") {
                message?.text.append(" 🦆")
            }
            .keyboardShortcut("d")
            .disabled(message == nil)
        }
    }
}
```

## Parameters

- `object`: The observable object to associate with focus, or   if   no object is currently available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/focusedobject(_:)-63qwt)*