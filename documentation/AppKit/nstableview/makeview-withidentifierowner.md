# makeView(withIdentifier:owner:)

**Framework**: AppKit  
**Kind**: method

Returns a new or existing view with the specified identifier.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func makeView(withIdentifier identifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSView?
```

#### Return Value

A view for the row.

#### Discussion

Typically, `identifier` is associated with a cell view that’s contained in a table’s Nib file. When this method is called, the table view automatically instantiates the cell view with the specified owner, which is usually the table view’s delegate. (The owner is useful in setting up outlets and target/actions from the view.) Note that a cell view’s identifier must be the same as its table column’s identifier for bindings to work. If you’re using bindings, it’s recommended that you use the Automatic identifier setting in Interface Builder.

This method may also return a reused view with the same `identifier` that is no longer available on screen. If a view with the specified identifier can’t be instantiated from the nib file or found in the reuse queue, this method returns `nil`.

This method is usually called by the delegate in [`tableView(_:viewFor:row:)`](nstableviewdelegate/tableview(_:viewfor:row:).md), but it can also be overridden to provide custom views for the `identifier`. Note that [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) is called each time this method is called, which means that `awakeFromNib` is also called on `owner`, even though the owner is already awake.

## Parameters

- `identifier`: The view identifier. Must not be  .
- `owner`: The owner of the NIB that may be loaded and instantiated to create a new view with the specified identifier.

## See Also

- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [Table View](table-view.md)
  Display custom data in rows and columns.
- [class NSNib](nsnib.md)
  An object wrapper, or container, for an Interface Builder nib file.
- [func rowView(atRow: Int, makeIfNecessary: Bool) -> NSTableRowView?](nstableview/rowview(atrow:makeifnecessary:).md)
  Returns a row view at the specified index, creating one if necessary.
- [func view(atColumn: Int, row: Int, makeIfNecessary: Bool) -> NSView?](nstableview/view(atcolumn:row:makeifnecessary:).md)
  Returns a view at the specified row and column indexes, creating one if necessary.
- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/makeview(withidentifier:owner:))*