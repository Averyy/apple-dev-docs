# rowView(atRow:makeIfNecessary:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a row view at the specified index, creating one if necessary.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func rowView(atRow row: Int, makeIfNecessary: Bool) -> NSTableRowView?
```

```objc
- (NSTableRowView *) rowViewAtRow:(NSInteger) row makeIfNecessary:(BOOL) makeIfNecessary;
```

#### Return Value

An instance, or subclass, of [`NSTableRowView`](../nstablerowview.md). Returning `nil` is also valid if `makeIfNecessary` is [`false`](../../Swift/false.md) and the view did not exist.

#### Discussion

This method first attempts to return a currently displayed view in the visible area. If there is no visible view, and `makeIfNecessary` is [`true`](../../Swift/true.md), a prepared temporary view is returned. If `makeIfNecessary` is [`false`](../../Swift/false.md), and the view is not visible, `nil` is returned.

In general, `makeIfNecessary` should be [`true`](../../Swift/true.md) if you require a resulting view, and [`false`](../../Swift/false.md) if you want to update properties on a view only if it is available (generally this means it is visible).

An exception is thrown if `row` falls outside of the number of rows in the table ([`numberOfRows`](./numberofrows.md)). The returned result should generally not be held onto for longer than the current run loop cycle. It’s better to call [`rowView(atRow:makeIfNecessary:)`](./rowview%28atrow,makeifnecessary%29.md) whenever a view is required.

## Parameters

- `row`: The row index.
- `makeIfNecessary`: [`true`](../../Swift/true.md) if a view is required, [`false`](../../Swift/false.md) if you want to update properties on a view, if one is available.

## See Also

### Creating Views to Display
- [func makeView(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSView?](./makeview%28withidentifier,owner%29.md)
  Returns a new or existing view with the specified identifier.
- [func view(atColumn: Int, row: Int, makeIfNecessary: Bool) -> NSView?](./view%28atcolumn,row,makeifnecessary%29.md)
  Returns a view at the specified row and column indexes, creating one if necessary.
- [struct NSUserInterfaceItemIdentifier](../nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowview(atrow:makeifnecessary:))*