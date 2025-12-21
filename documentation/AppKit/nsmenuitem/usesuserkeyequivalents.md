# usesUserKeyEquivalents

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value that indicates whether menu items conform to user preferences for key equivalents.

**Availability**:
- macOS ?+

## Declaration

```swift
class var usesUserKeyEquivalents: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if menu items conform to user preferences for key equivalents; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var userKeyEquivalent: String](nsmenuitem/userkeyequivalent.md)
  The user-assigned key equivalent for the menu item.
- [var allowsAutomaticKeyEquivalentLocalization: Bool](nsmenuitem/allowsautomatickeyequivalentlocalization.md)
  A Boolean value that determines whether the system automatically remaps the keyboard shortcut to support localized keyboards.
- [var allowsAutomaticKeyEquivalentMirroring: Bool](nsmenuitem/allowsautomatickeyequivalentmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
- [var allowsKeyEquivalentWhenHidden: Bool](nsmenuitem/allowskeyequivalentwhenhidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/usesuserkeyequivalents)*