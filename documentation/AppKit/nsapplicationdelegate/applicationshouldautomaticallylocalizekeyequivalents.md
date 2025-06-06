# applicationShouldAutomaticallyLocalizeKeyEquivalents(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func applicationShouldAutomaticallyLocalizeKeyEquivalents(_ application: NSApplication) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to enable automatic shortcut localization for all app-specific menus, or [`false`](https://developer.apple.com/documentation/swift/false) to handle shortcut localization yourself.

#### Discussion

A keyboard shortcut you specify in one language might be difficult or impossible to reproduce on a keyboard with a different character set or layout. Localized keyboards sometimes rearrange punctuation marks or replace them altogether to make room for a language’s required characters. The new locations of those keys might make it difficult to use your current shortcuts. To ensure your shortcuts are always usable, the system can automatically remap shortcuts, as needed, to accommodate the connected keyboard.

If you don’t implement this method, or if you implement it and return [`true`](https://developer.apple.com/documentation/swift/true), the system automatically remaps all app-specific menu shortcuts that are unreachable on the current keyboard. The system doesn’t remap shortcuts when the input keys have identical positions on both keyboards, or when a shortcut is still easily reachable on the current keyboard. The remapping is transparent to your app.

If you already localize your app’s shortcuts for different languages, or if you allow someone to customize your app’s shortcuts, you can return [`false`](https://developer.apple.com/documentation/swift/false) to disable the automatic remapping behavior. When you return [`false`](https://developer.apple.com/documentation/swift/false), the system doesn’t change your app’s shortcuts. Instead, you are responsible to make any required changes to support localized keyboards.

During the final activation of your app at launch time, the app object’s [`finishLaunching()`](nsapplication/finishlaunching().md) method calls this method once to record your app’s response.

## Parameters

- `application`: The app object associated with the delegate.

## See Also

- [var allowsAutomaticKeyEquivalentLocalization: Bool](nsmenuitem/allowsautomatickeyequivalentlocalization.md)
  A Boolean value that determines whether the system automatically remaps the keyboard shortcut to support localized keyboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldautomaticallylocalizekeyequivalents(_:))*