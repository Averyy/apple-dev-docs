# userKeyEquivalent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The user-assigned key equivalent for the menu item.

**Availability**:
- macOS

## Declaration

```swift
var userKeyEquivalent: String { get }
```

```objc
@property (copy, readonly) NSString * userKeyEquivalent;
```

## See Also

### Related Documentation
- [var keyEquivalent: String](./keyequivalent.md)
  The menu item’s unmodified key equivalent.
### Managing user key equivalents
- [class var usesUserKeyEquivalents: Bool](./usesuserkeyequivalents.md)
  Returns a Boolean value that indicates whether menu items conform to user preferences for key equivalents.
- [var allowsAutomaticKeyEquivalentLocalization: Bool](./allowsautomatickeyequivalentlocalization.md)
  A Boolean value that determines whether the system automatically remaps the keyboard shortcut to support localized keyboards.
- [var allowsAutomaticKeyEquivalentMirroring: Bool](./allowsautomatickeyequivalentmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
- [var allowsKeyEquivalentWhenHidden: Bool](./allowskeyequivalentwhenhidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/userkeyequivalent)*