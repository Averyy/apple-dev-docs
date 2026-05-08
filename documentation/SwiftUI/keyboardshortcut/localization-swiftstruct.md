# KeyboardShortcut.Localization

**Framework**: SwiftUI  
**Kind**: struct

Options for how a keyboard shortcut participates in automatic localization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct Localization
```

#### Overview

A shortcut’s `key` that is defined on an US-English keyboard layout might not be reachable on international layouts. For example the shortcut `⌘[` works well for the US layout but is hard to reach for German users. On the German keyboard layout, pressing `⌥5` will produce `[`, which causes the shortcut to become `⌥⌘5`. If configured, which is the default behavior, automatic shortcut remapping will convert it to `⌘Ö`.

In addition to that, some keyboard shortcuts carry information about directionality. Right-aligning a block of text or seeking forward in context of music playback are such examples. These kinds of shortcuts benefit from the option [`withoutMirroring`](keyboardshortcut/localization-swift.struct/withoutmirroring.md) to tell the system that they won’t be flipped when running in a right-to-left context.

## Topics

### Getting localization strategies
- [static let automatic: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct/automatic.md)
  Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.
- [static let custom: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct/custom.md)
  Don’t use automatic shortcut remapping.
- [static let withoutMirroring: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct/withoutmirroring.md)
  Don’t mirror shortcuts.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization)](keyboardshortcut/init(_:modifiers:localization:).md)
  Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [var localization: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.property.md)
  The localization strategy to apply to this shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct)*