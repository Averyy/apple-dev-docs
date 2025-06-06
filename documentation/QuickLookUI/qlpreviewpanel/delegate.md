# delegate

**Framework**: Quick Look UI  
**Kind**: property

The delegate object that controls the preview panel’s behavior.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
unowned(unsafe) var delegate: AnyObject! { get set }
```

#### Discussion

The class assigned as the delegate should conform to the [`QLPreviewPanelDelegate`](qlpreviewpaneldelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/delegate)*