# contentView

**Framework**: AppKit  
**Kind**: property

The view to use for drawing the dock tile contents.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var contentView: NSView? { get set }
```

#### Discussion

The view you specify should be height and width resizable.

Cocoa does not automatically redraw the contents of your dock tile. Instead, your application must explicitly send display messages to the dock tile object whenever the contents of your view change and need to be redrawn. Your dock tile view is responsible for drawing the entire contents of the dock tile. Your view does not need to draw the application or custom string badges.

## See Also

- [func display()](nsdocktile/display.md)
  Redraws the dock tile’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktile/contentview)*