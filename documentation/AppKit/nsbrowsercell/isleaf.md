# isLeaf

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the browser cell is a leaf or a branch cell.

**Availability**:
- macOS

## Declaration

```swift
var isLeaf: Bool { get set }
```

```objc
@property (getter=isLeaf) BOOL leaf;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the browser cell is a leaf cell.

A branch `NSBrowserCell` has an image near its right edge indicating that more, hierarchically related information is available; when the user selects the cell, the `NSBrowser` displays a new column of `NSBrowserCell` objects. A leaf `NSBrowserCell` has no image, indicating that the user has reached a terminal piece of information; it doesn’t point to additional information.

## See Also

### Managing Browser Cell State
- [func reset()](./reset%28%29.md)
  Unhighlights the receiver and unsets its state.
- [func set()](./set%28%29.md)
  Highlights the receiver and sets its state.
- [var isLoaded: Bool](./isloaded.md)
  A Boolean that indicates whether the cell is ready to display.
- [func highlightColor(in: NSView) -> NSColor?](./highlightcolor%28in%29.md)
  Returns the highlight color that the receiver wants to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/isleaf)*