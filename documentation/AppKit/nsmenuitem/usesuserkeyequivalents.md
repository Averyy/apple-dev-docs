# usesUserKeyEquivalents

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns a Boolean value that indicates whether menu items conform to user preferences for key equivalents.

**Availability**:
- macOS

## Declaration

```swift
class var usesUserKeyEquivalents: Bool { get set }
```

```objc
@property (class) BOOL usesUserKeyEquivalents;
```

## Return Value

[`true`](../../Swift/true.md) if menu items conform to user preferences for key equivalents; otherwise, [`false`](../../Swift/false.md).

## See Also

### Managing user key equivalents
- [var userKeyEquivalent: String](./userkeyequivalent.md)
  The user-assigned key equivalent for the menu item.
- [var allowsAutomaticKeyEquivalentLocalization: Bool](./allowsautomatickeyequivalentlocalization.md)
  A Boolean value that determines whether the system automatically remaps the keyboard shortcut to support localized keyboards.
- [var allowsAutomaticKeyEquivalentMirroring: Bool](./allowsautomatickeyequivalentmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
- [var allowsKeyEquivalentWhenHidden: Bool](./allowskeyequivalentwhenhidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/usesuserkeyequivalents)*