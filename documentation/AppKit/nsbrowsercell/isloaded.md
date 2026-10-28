# isLoaded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the cell is ready to display.

**Availability**:
- macOS

## Declaration

```swift
var isLoaded: Bool { get set }
```

```objc
@property (getter=isLoaded) BOOL loaded;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the browser cell’s state has been set and the cell is ready to display.

## See Also

### Managing Browser Cell State
- [func reset()](./reset%28%29.md)
  Unhighlights the receiver and unsets its state.
- [func set()](./set%28%29.md)
  Highlights the receiver and sets its state.
- [var isLeaf: Bool](./isleaf.md)
  A Boolean that indicates whether the browser cell is a leaf or a branch cell.
- [func highlightColor(in: NSView) -> NSColor?](./highlightcolor%28in%29.md)
  Returns the highlight color that the receiver wants to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/isloaded)*