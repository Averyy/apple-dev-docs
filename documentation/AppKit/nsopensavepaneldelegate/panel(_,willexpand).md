# panel(_:willExpand:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the Save panel is about to expand or collapse because the user clicked the disclosure triangle that displays or hides the file browser.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, willExpand expanding: Bool)
```

```objc
- (void) panel:(id) sender willExpand:(BOOL) expanding;
```

## Parameters

- `sender`: The panel that is about to expand or collapse.
- `expanding`: [`true`](../../Swift/true.md) specifies that the panel is expanding; [`false`](../../Swift/false.md) specifies that it is collapsing.

## See Also

### Responding to Panel Changes
- [func panelSelectionDidChange(Any?)](./panelselectiondidchange%28_%29.md)
  Tells the delegate that the user changed the selection in the specified Save panel.
- [func panel(Any, didChangeToDirectoryURL: URL?)](./panel%28_,didchangetodirectoryurl%29.md)
  Tells the delegate that the user changed the selected directory to the directory located at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:willexpand:))*