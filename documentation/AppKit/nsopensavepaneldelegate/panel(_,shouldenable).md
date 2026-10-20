# panel(_:shouldEnable:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the specified URL should be enabled in the Open panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, shouldEnable url: URL) -> Bool
```

```objc
- (BOOL) panel:(id) sender shouldEnableURL:(NSURL *) url;
```

#### Return Value

[`true`](../../Swift/true.md) if you want the panel to display the item at the specifed URL as enabled, or [`false`](../../Swift/false.md) to display it as disabled.

#### Discussion

Save panels do not call this method; they always disable URLs. Implementations of this method should be fast to avoid stalling the user interface. Use [`panel(_:validate:)`](./panel%28_,validate%29.md) instead if processing will take a long time.

## Parameters

- `sender`: The panel that asks whether the URL should be enabled.
- `url`: The URL for you to check.

## See Also

### Validating the Panel Content
- [func panel(Any, validate: URL) throws](./panel%28_,validate%29.md)
  Asks the delegate to validate the URL for a file that the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:shouldenable:))*