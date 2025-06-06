# init(style:title:handler:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a new table view row action object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
convenience init(style: NSTableViewRowAction.Style, title: String, handler: @escaping (NSTableViewRowAction, Int) -> Void)
```

#### Return Value

A new table row action object that you can return from your table view’s delegate method.

#### Discussion

The style and handler block you specify cannot be changed later. You can change the title of the action button. You can also configure other appearance-related properties of the button using the properties of this class.

You can assign the same row action object to multiple rows of your table.

## Parameters

- `style`: The style characteristics to apply to the button. Use this value to apply default appearance characteristics to the button. These characteristics visually communicate, such as by color, information about what the button does. For example, specify a style of   to indicate an action is destructive to the underlying data. For a list of possible style values, see  .
- `title`: The string to display in the button. Specify a string localized for the user’s current language.
- `handler`: The block to execute when the user clicks the button associated with this action. AppKit makes a copy of the block you provide. When the user selects the action represented by this object, AppKit executes your   block on the app’s main thread. This parameter must not be  . This block has no return value and takes the following parameters:

## See Also

- [NSTableViewRowAction.Style](nstableviewrowaction/style-swift.enum.md)
  Constants that help define the appearance and behavior of action buttons.
- [func tableView(NSTableView, rowActionsForRow: Int, edge: NSTableView.RowActionEdge) -> [NSTableViewRowAction]](nstableviewdelegate/tableview(_:rowactionsforrow:edge:).md)
  Asks the delegate to provide an array of row actions to be attached to the specified edge of a table row and displayed when the user swipes horizontally across the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction/init(style:title:handler:))*