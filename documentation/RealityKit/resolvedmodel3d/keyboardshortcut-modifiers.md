# keyboardShortcut(_:modifiers:)

**Framework**: RealityKit  
**Kind**: method

Defines a keyboard shortcut and assigns it to the modified control.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func keyboardShortcut(_ key: KeyEquivalent, modifiers: EventModifiers = .command) -> some View
```

#### Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost window or scene, or anywhere in the macOS main menu, is equivalent to direct interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-first traversal of one or more view hierarchies. On macOS, the system looks in the key window first, then the main window, and then the command groups; on other platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one found is used.

The default localization configuration is set to `KeyboardShortcut/Localization-swift.struct/automatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/keyboardshortcut(_:modifiers:))*