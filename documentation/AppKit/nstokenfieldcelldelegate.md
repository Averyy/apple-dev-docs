# NSTokenFieldCellDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of [`NSTokenFieldCell`](./nstokenfieldcell.md) objects to work with tokenized strings.

**Availability**:
- macOS

## Declaration

```swift
protocol NSTokenFieldCellDelegate : NSObjectProtocol
```

```objc
@protocol NSTokenFieldCellDelegate <NSObject>
```

## Topics

### Displaying Tokenized Strings
- [func tokenFieldCell(NSTokenFieldCell, displayStringForRepresentedObject: Any) -> String?](./nstokenfieldcelldelegate/tokenfieldcell%28_,displaystringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be displayed as a proxy for the represented object.
- [func tokenFieldCell(NSTokenFieldCell, styleForRepresentedObject: Any) -> NSTokenField.TokenStyle](./nstokenfieldcelldelegate/tokenfieldcell%28_,styleforrepresentedobject%29.md)
  Allows the delegate to return the token style for editing the specified represented object.
### Editing a Tokenized Strings
- [func tokenFieldCell(NSTokenFieldCell, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [Any]](./nstokenfieldcelldelegate/tokenfieldcell%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenFieldCell(NSTokenFieldCell, editingStringForRepresentedObject: Any) -> String?](./nstokenfieldcelldelegate/tokenfieldcell%28_,editingstringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be edited as a proxy for the represented object.
- [func tokenFieldCell(NSTokenFieldCell, representedObjectForEditing: String) -> Any?](./nstokenfieldcelldelegate/tokenfieldcell%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the string being edited.
- [func tokenFieldCell(NSTokenFieldCell, shouldAdd: [Any], at: Int) -> [Any]](./nstokenfieldcelldelegate/tokenfieldcell%28_,shouldadd,at%29.md)
  Allows the delegate to validate the tokens to be added to the receiver at a given index.
### Reading To and Writing From the Pasteboard
- [func tokenFieldCell(NSTokenFieldCell, readFrom: NSPasteboard) -> [Any]?](./nstokenfieldcelldelegate/tokenfieldcell%28_,readfrom%29.md)
  Allows the delegate to return an array of objects representing the data read from `pboard`.
- [func tokenFieldCell(NSTokenFieldCell, writeRepresentedObjects: [Any], to: NSPasteboard) -> Bool](./nstokenfieldcelldelegate/tokenfieldcell%28_,writerepresentedobjects,to%29.md)
  Allows the delegate the opportunity to write custom pasteboard types to the pasteboard for the represented objects in `objects`.
### Managing Menus for Represented Objects
- [func tokenFieldCell(NSTokenFieldCell, hasMenuForRepresentedObject: Any) -> Bool](./nstokenfieldcelldelegate/tokenfieldcell%28_,hasmenuforrepresentedobject%29.md)
  Allows the delegate to specify whether the represented object provides a menu.
- [func tokenFieldCell(NSTokenFieldCell, menuForRepresentedObject: Any) -> NSMenu?](./nstokenfieldcelldelegate/tokenfieldcell%28_,menuforrepresentedobject%29.md)
  Allows the delegate to provide a menu for the specified represented object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Cell
- [class NSTokenFieldCell](./nstokenfieldcell.md)
  A text field cell subclass that enables tokenized editing of an array of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate)*