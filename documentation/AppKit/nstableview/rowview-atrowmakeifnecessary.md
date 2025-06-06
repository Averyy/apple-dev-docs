# rowView(atRow:makeIfNecessary:)

**Framework**: AppKit  
**Kind**: method

Returns a row view at the specified index, creating one if necessary.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func rowView(atRow row: Int, makeIfNecessary: Bool) -> NSTableRowView?
```

#### Return Value

An instance, or subclass, of [`NSTableRowView`](nstablerowview.md). Returning `nil` is also valid if `makeIfNecessary` is [`false`](https://developer.apple.com/documentation/swift/false) and the view did not exist.

#### Discussion

This method first attempts to return a currently displayed view in the visible area. If there is no visible view, and `makeIfNecessary` is [`true`](https://developer.apple.com/documentation/swift/true), a prepared temporary view is returned. If `makeIfNecessary` is [`false`](https://developer.apple.com/documentation/swift/false), and the view is not visible, `nil` is returned.

In general, `makeIfNecessary` should be [`true`](https://developer.apple.com/documentation/swift/true) if you require a resulting view, and [`false`](https://developer.apple.com/documentation/swift/false) if you want to update properties on a view only if it is available (generally this means it is visible).

An exception is thrown if `row` falls outside of the number of rows in the table ([`numberOfRows`](nstableview/numberofrows.md)). The returned result should generally not be held onto for longer than the current run loop cycle. It’s better to call [`rowView(atRow:makeIfNecessary:)`](nstableview/rowview(atrow:makeifnecessary:).md) whenever a view is required.

## Parameters

- `row`: The row index.
- `makeIfNecessary`:   if a view is required,   if you want to update properties on a view, if one is available.

## See Also

- [func makeView(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSView?](nstableview/makeview(withidentifier:owner:).md)
  Returns a new or existing view with the specified identifier.
- [func view(atColumn: Int, row: Int, makeIfNecessary: Bool) -> NSView?](nstableview/view(atcolumn:row:makeifnecessary:).md)
  Returns a view at the specified row and column indexes, creating one if necessary.
- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowview(atrow:makeifnecessary:))*