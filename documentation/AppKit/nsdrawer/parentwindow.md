# parentWindow

**Framework**: AppKit  
**Kind**: property

The receiver’s parent window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
unowned(unsafe) var parentWindow: NSWindow? { get set }
```

#### Discussion

Changes in a drawer’s parent window do not take place while the drawer is onscreen; they are delayed until the drawer next closes.

## See Also

- [var contentView: NSView?](nsdrawer/contentview.md)
  The receiver’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/parentwindow)*