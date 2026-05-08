# withoutMirroring

**Framework**: SwiftUI  
**Kind**: property

Don’t mirror shortcuts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static let withoutMirroring: KeyboardShortcut.Localization
```

#### Discussion

Use this for shortcuts that always have a specific directionality, like aligning something on the right.

Don’t use this option for navigational shortcuts like “Go Back” because navigation is flipped in right-to-left contexts.

## See Also

- [static let automatic: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct/automatic.md)
  Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.
- [static let custom: KeyboardShortcut.Localization](keyboardshortcut/localization-swift.struct/custom.md)
  Don’t use automatic shortcut remapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct/withoutmirroring)*