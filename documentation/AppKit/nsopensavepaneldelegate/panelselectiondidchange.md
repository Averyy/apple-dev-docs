# panelSelectionDidChange(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the user changed the selection in the specified Save panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func panelSelectionDidChange(_ sender: Any?)
```

## Parameters

- `sender`: The panel whose selection changed.

## See Also

- [func panel(Any, didChangeToDirectoryURL: URL?)](nsopensavepaneldelegate/panel(_:didchangetodirectoryurl:).md)
  Tells the delegate that the user changed the selected directory to the directory located at the specified URL.
- [func panel(Any, willExpand: Bool)](nsopensavepaneldelegate/panel(_:willexpand:).md)
  Tells the delegate that the Save panel is about to expand or collapse because the user clicked the disclosure triangle that displays or hides the file browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panelselectiondidchange(_:))*