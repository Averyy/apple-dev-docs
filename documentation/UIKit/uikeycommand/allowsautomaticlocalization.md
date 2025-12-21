# allowsAutomaticLocalization

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the system automatically remaps keyboard shortcuts based on the keyboard layout.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsAutomaticLocalization: Bool { get set }
```

#### Discussion

A keyboard shortcut you specify in one language might be difficult or impossible to reproduce on a keyboard with a different character set or layout. Localized keyboards sometimes rearrange punctuation marks or replace them altogether to make room for a language’s required characters. The new locations of those keys might make it difficult to use your key command’s current shortcut. To ensure your shortcuts are always usable, the system can automatically remap shortcuts, as needed, to accommodate the connected keyboard.

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system automatically remaps this key command’s shortcut when that shortcut is unreachable on the current keyboard. The system doesn’t remap shortcuts when the input keys have identical positions on both keyboards, or when the shortcut is still easily reachable on the current keyboard. The remapping is transparent to your app.

If you already localize your app’s shortcuts for different languages, or if you allow someone to customize your app’s shortcuts, you can set this property to [`false`](https://developer.apple.com/documentation/Swift/false) to disable the automatic remapping behavior. When you set this property to [`false`](https://developer.apple.com/documentation/Swift/false), the system doesn’t change the shortcut for your key commands. Instead, you’re responsible for making any required changes to support localized keyboards. Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) also disables the automatic mirroring of shortcuts, as described by the [`allowsAutomaticMirroring`](uikeycommand/allowsautomaticmirroring.md) property.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func applicationShouldAutomaticallyLocalizeKeyCommands(UIApplication) -> Bool](uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands(_:).md)
  Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.
- [var allowsAutomaticMirroring: Bool](uikeycommand/allowsautomaticmirroring.md)
  A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/allowsautomaticlocalization)*