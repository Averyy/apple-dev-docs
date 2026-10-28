# keyboardShortcut(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Assigns an optional keyboard shortcut to the modified control.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func keyboardShortcut(_ shortcut: KeyboardShortcut?) -> some View
```

**Other overloads**:

```swift
nonisolated
func keyboardShortcut(_ shortcut: KeyboardShortcut) -> some View
```

## Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost window or scene, or anywhere in the macOS main menu, is equivalent to direct interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing traversal of one or more view hierarchies. On macOS, the system looks in the key window first, then the main window, and then the command groups; on other platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one found is used. If the provided shortcut is `nil`, the modifier will have no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/keyboardshortcut(_:)-3vjx6)*