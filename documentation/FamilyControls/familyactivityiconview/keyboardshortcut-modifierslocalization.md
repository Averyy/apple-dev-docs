# keyboardShortcut(_:modifiers:localization:)

**Framework**: FamilyControls  
**Kind**: method

Defines a keyboard shortcut and assigns it to the modified control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func keyboardShortcut(_ key: KeyEquivalent, modifiers: EventModifiers = .command, localization: KeyboardShortcut.Localization) -> some View
```

#### Discussion

Pressing the control’s shortcut while the control is anywhere in the frontmost window or scene, or anywhere in the macOS main menu, is equivalent to direct interaction with the control to perform its primary action.

The target of a keyboard shortcut is resolved in a leading-to-trailing, depth-first traversal of one or more view hierarchies. On macOS, the system looks in the key window first, then the main window, and then the command groups; on other platforms, the system looks in the active scene, and then the command groups.

If multiple controls are associated with the same shortcut, the first one found is used.

##### Localization

Provide a `localization` value to specify how this shortcut should be localized. Given that `key` is always defined in relation to the US-English keyboard layout, it might be hard to reach on different international layouts. For example the shortcut `⌘[` works well for the US layout but is hard to reach for German users, where `[` is available by pressing `⌥5`, making users type `⌥⌘5`. The automatic keyboard shortcut remapping re-assigns the shortcut to an appropriate replacement, `⌘Ö` in this case.

Certain shortcuts carry information about directionality. For instance, `⌘[` can reveal a previous view. Following the layout direction of the UI, this shortcut will be automatically mirrored to `⌘]`. However, this does not apply to items such as “Align Left `⌘{`”, which will be “left” independently of the layout direction. When the shortcut shouldn’t follow the directionality of the UI, but rather be the same in both right-to-left and left-to-right directions, using `KeyboardShortcut/Localization-swift.struct/withoutMirroring` will prevent the system from flipping it.

```swift
var body: some Commands {
    CommandMenu("Card") {
        Button("Align Left") { ... }
            .keyboardShortcut("{",
                 modifiers: .option,
                 localization: .withoutMirroring)
        Button("Align Right") { ... }
            .keyboardShortcut("}",
                 modifiers: .option,
                 localization: .withoutMirroring)
    }
}
```

Lastly, providing the option `KeyboardShortcut/Localization-swift.struct/custom` disables the automatic localization for this shortcut to tell the system that internationalization is taken care of in a different way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/keyboardshortcut(_:modifiers:localization:))*