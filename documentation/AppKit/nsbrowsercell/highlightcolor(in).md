# highlightColor(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the highlight color that the receiver wants to display.

**Availability**:
- macOS

## Declaration

```swift
func highlightColor(in controlView: NSView) -> NSColor?
```

```objc
- (NSColor *) highlightColorInView:(NSView *) controlView;
```

#### Return Value

The highlight color.

## Parameters

- `controlView`: The view for which to return the highlight color.

## See Also

### Managing Browser Cell State
- [func reset()](./reset%28%29.md)
  Unhighlights the receiver and unsets its state.
- [func set()](./set%28%29.md)
  Highlights the receiver and sets its state.
- [var isLeaf: Bool](./isleaf.md)
  A Boolean that indicates whether the browser cell is a leaf or a branch cell.
- [var isLoaded: Bool](./isloaded.md)
  A Boolean that indicates whether the cell is ready to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/highlightcolor(in:))*