# custom

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Don’t use automatic shortcut remapping.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static let custom: KeyboardShortcut.Localization
```

#### Discussion

When you use this mode, you have to take care of international use-cases separately.

## See Also

### Getting localization strategies
- [static let automatic: KeyboardShortcut.Localization](./automatic.md)
  Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.
- [static let withoutMirroring: KeyboardShortcut.Localization](./withoutmirroring.md)
  Don’t mirror shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct/custom)*