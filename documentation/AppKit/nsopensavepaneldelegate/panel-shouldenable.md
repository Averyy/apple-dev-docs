# panel(_:shouldEnable:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether the specified URL should be enabled in the Open panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, shouldEnable url: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you want the panel to display the item at the specifed URL as enabled, or [`false`](https://developer.apple.com/documentation/swift/false) to display it as disabled.

#### Discussion

Save panels do not call this method; they always disable URLs. Implementations of this method should be fast to avoid stalling the user interface. Use [`panel(_:validate:)`](nsopensavepaneldelegate/panel(_:validate:).md) instead if processing will take a long time.

## Parameters

- `sender`: The panel that asks whether the URL should be enabled.
- `url`: The URL for you to check.

## See Also

- [Sheet Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sheets/Sheets.html#//apple_ref/doc/uid/10000002i)
- [func panel(Any, validate: URL) throws](nsopensavepaneldelegate/panel(_:validate:).md)
  Asks the delegate to validate the URL for a file that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:shouldenable:))*