# view(atColumn:row:makeIfNecessary:)

**Framework**: AppKit  
**Kind**: method

Returns a view at the specified row and column indexes, creating one if necessary.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func view(atColumn column: Int, row: Int, makeIfNecessary: Bool) -> NSView?
```

#### Return Value

An instance of [`NSView`](nsview.md).

#### Discussion

This method first attempts to return an available view, which is generally in the visible area. If there is no available view, and `makeIfNecessary` is [`true`](https://developer.apple.com/documentation/Swift/true), a prepared temporary view is returned. If `makeIfNecessary` is [`false`](https://developer.apple.com/documentation/Swift/false), and the view is not available, `nil` will be returned.

In general, `makeIfNecessary` should be [`true`](https://developer.apple.com/documentation/Swift/true) if you require a resulting view, and [`false`](https://developer.apple.com/documentation/Swift/false) if you only want to update properties on a view only if it is available (generally this means it is visible).

An exception will be thrown if `row` is not within the [`numberOfRows`](nstableview/numberofrows.md). The returned result should generally not be held onto for longer than the current run loop cycle. Instead they should re-query the table view for the row view.

## Parameters

- `column`: The index of the column in the   array.
- `row`: The row index.
- `makeIfNecessary`:   if a view is required,   if you want to update properties on a view, if one is available.

## See Also

- [func makeView(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSView?](nstableview/makeview(withidentifier:owner:).md)
  Returns a new or existing view with the specified identifier.
- [func rowView(atRow: Int, makeIfNecessary: Bool) -> NSTableRowView?](nstableview/rowview(atrow:makeifnecessary:).md)
  Returns a row view at the specified index, creating one if necessary.
- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/view(atcolumn:row:makeifnecessary:))*