# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom view the status item displays at its position in the status bar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var view: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * view;
```

#### Discussion

Setting a custom view overrides the appearance and behavior settings that [`NSStatusItem`](../nsstatusitem.md) defines. The custom view is responsible for drawing itself and providing its own behaviors, such as processing mouse clicks and sending action messages.

## See Also

### Configuring the status item’s appearance
- [var isVisible: Bool](./isvisible.md)
  A Boolean value indicating if the menu bar currently displays the status item.
- [var length: CGFloat](./length.md)
  The amount of space in the status bar that should be allocated to the status item.
- [class let squareLength: CGFloat](./squarelength.md)
  A status item length that is equal to the status bar’s thickness.
- [class let variableLength: CGFloat](./variablelength.md)
  A status item length that dynamically adjusts to the width of its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/view)*