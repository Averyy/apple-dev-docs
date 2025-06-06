# keyboardShortcut(_:)

**Framework**: SwiftUI  
**Kind**: method

Defines a keyboard shortcut for opening new scene windows.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some Scene
```

#### Return Value

A scene that can be presented with a keyboard shortcut.

#### Discussion

A scene’s keyboard shortcut is bound to the command it adds for creating new windows (in the case of `WindowGroup` and `DocumentGroup`) or bringing a singleton window forward (in the case of `Window` and, on macOS, `Settings` and `UtilityWindow`). Pressing the keyboard shortcut is equivalent to selecting the menu command.

In cases where a command already has a keyboard shortcut, the scene’s keyboard shortcut is used instead. For example, `WindowGroup` normally creates a File > New Window menu command whose keyboard shortcut is `⌘N`. The following code changes it to something based on dynamic state:

```swift
@main
struct Notes: App {
    @State private var newWindowShortcut: KeyboardShortcut? = ...

    var body: some Scene {
        WindowGroup {
            ContentView($newWindowShortcut)
        }
        .keyboardShortcut(newWindowShortcut)
    }
}
```

If `shortcut` is `nil`, the scene’s presentation command will not be associated with a keyboard shortcut, even if SwiftUI normally assigns one automatically.

## Parameters

- `shortcut`: The keyboard shortcut for presenting the scene, or  .

## See Also

- [func commands<Content>(content: () -> Content) -> some Scene](scene/commands(content:).md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](scene/commandsremoved.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](scene/commandsreplaced(content:).md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some Scene](scene/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut for opening new scene windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/keyboardshortcut(_:))*