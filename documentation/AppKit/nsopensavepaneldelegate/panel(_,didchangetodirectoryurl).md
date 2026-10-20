# panel(_:didChangeToDirectoryURL:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user changed the selected directory to the directory located at the specified URL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, didChangeToDirectoryURL url: URL?)
```

```objc
- (void) panel:(id) sender didChangeToDirectoryURL:(NSURL *) url;
```

## Parameters

- `sender`: The panel whose directory changed.
- `url`: The URL of the new directory, or `nil` if it can’t be represented by an [`NSURL`](../../Foundation/nsurl.md) object.

## See Also

### Responding to Panel Changes
- [func panelSelectionDidChange(Any?)](./panelselectiondidchange%28_%29.md)
  Tells the delegate that the user changed the selection in the specified Save panel.
- [func panel(Any, willExpand: Bool)](./panel%28_,willexpand%29.md)
  Tells the delegate that the Save panel is about to expand or collapse because the user clicked the disclosure triangle that displays or hides the file browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:didchangetodirectoryurl:))*