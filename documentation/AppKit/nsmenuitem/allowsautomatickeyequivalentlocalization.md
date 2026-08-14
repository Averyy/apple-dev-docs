# allowsAutomaticKeyEquivalentLocalization

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the system automatically remaps the keyboard shortcut to support localized keyboards.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var allowsAutomaticKeyEquivalentLocalization: Bool { get set }
```

#### Discussion

A keyboard shortcut you specify in one language might be difficult or impossible to reproduce on a keyboard with a different character set or layout. Localized keyboards sometimes rearrange punctuation marks or replace them altogether to make room for a language’s required characters. The new locations of those keys might make it difficult to use your menu item’s current shortcut. To ensure your shortcuts are always usable, the system can automatically remap shortcuts, as needed, to accommodate the connected keyboard.

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the system automatically remaps this menu item’s shortcut when that shortcut is unreachable on the current keyboard. The system doesn’t remap shortcuts when the input keys have identical positions on both keyboards, or when the shortcut is still easily reachable on the current keyboard. The remapping is transparent to your app.

If you already localize your app’s shortcuts for different languages, or if you permit someone to customize your app’s shortcuts, you can set this property to [`false`](https://developer.apple.com/documentation/swift/false) to disable the automatic remapping behavior. When you set this property to [`false`](https://developer.apple.com/documentation/swift/false), the system doesn’t change the shortcut for your menu items. Instead, you are responsible for making any required changes to support localized keyboards. Setting this property to [`false`](https://developer.apple.com/documentation/swift/false) also disables the automatic mirroring of shortcuts, as described by the [`allowsAutomaticKeyEquivalentMirroring`](nsmenuitem/allowsautomatickeyequivalentmirroring.md) property.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func applicationShouldAutomaticallyLocalizeKeyEquivalents(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldautomaticallylocalizekeyequivalents(_:).md)
  Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.
- [class var usesUserKeyEquivalents: Bool](nsmenuitem/usesuserkeyequivalents.md)
  Returns a Boolean value that indicates whether menu items conform to user preferences for key equivalents.
- [var userKeyEquivalent: String](nsmenuitem/userkeyequivalent.md)
  The user-assigned key equivalent for the menu item.
- [var allowsAutomaticKeyEquivalentMirroring: Bool](nsmenuitem/allowsautomatickeyequivalentmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
- [var allowsKeyEquivalentWhenHidden: Bool](nsmenuitem/allowskeyequivalentwhenhidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/allowsautomatickeyequivalentlocalization)*