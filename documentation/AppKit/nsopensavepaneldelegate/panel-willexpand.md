# panel(_:willExpand:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the Save panel is about to expand or collapse because the user clicked the disclosure triangle that displays or hides the file browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, willExpand expanding: Bool)
```

## Parameters

- `sender`: The panel that is about to expand or collapse.
- `expanding`:   specifies that the panel is expanding;   specifies that it is collapsing.

## See Also

- [func panelSelectionDidChange(Any?)](nsopensavepaneldelegate/panelselectiondidchange(_:).md)
  Tells the delegate that the user changed the selection in the specified Save panel.
- [func panel(Any, didChangeToDirectoryURL: URL?)](nsopensavepaneldelegate/panel(_:didchangetodirectoryurl:).md)
  Tells the delegate that the user changed the selected directory to the directory located at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:willexpand:))*