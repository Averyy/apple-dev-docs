# view

**Framework**: AppKit  
**Kind**: property

The custom view the status item displays at its position in the status bar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var view: NSView? { get set }
```

#### Discussion

Setting a custom view overrides the appearance and behavior settings that [`NSStatusItem`](nsstatusitem.md) defines. The custom view is responsible for drawing itself and providing its own behaviors, such as processing mouse clicks and sending action messages.

## See Also

- [var isVisible: Bool](nsstatusitem/isvisible.md)
  A Boolean value indicating if the menu bar currently displays the status item.
- [var length: CGFloat](nsstatusitem/length.md)
  The amount of space in the status bar that should be allocated to the status item.
- [class let squareLength: CGFloat](nsstatusitem/squarelength.md)
  A status item length that is equal to the status bar’s thickness.
- [class let variableLength: CGFloat](nsstatusitem/variablelength.md)
  A status item length that dynamically adjusts to the width of its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/view)*