# NSTokenFieldDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of [`NSTokenField`](./nstokenfield.md) objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSTokenFieldDelegate : NSTextFieldDelegate
```

```objc
@protocol NSTokenFieldDelegate <NSTextFieldDelegate>
```

## Topics

### Displaying Tokenized Strings
- [func tokenField(NSTokenField, displayStringForRepresentedObject: Any) -> String?](./nstokenfielddelegate/tokenfield%28_,displaystringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be displayed as a proxy for the given represented object.
- [func tokenField(NSTokenField, styleForRepresentedObject: Any) -> NSTokenField.TokenStyle](./nstokenfielddelegate/tokenfield%28_,styleforrepresentedobject%29.md)
  Allows the delegate to return the token style for editing the specified represented object.
### Editing a Tokenized Strings
- [func tokenField(NSTokenField, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>?) -> [Any]?](./nstokenfielddelegate/tokenfield%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenField(NSTokenField, editingStringForRepresentedObject: Any) -> String?](./nstokenfielddelegate/tokenfield%28_,editingstringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be edited as a proxy for a represented object.
- [func tokenField(NSTokenField, representedObjectForEditing: String) -> Any?](./nstokenfielddelegate/tokenfield%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the given editing string.
- [func tokenField(NSTokenField, shouldAdd: [Any], at: Int) -> [Any]](./nstokenfielddelegate/tokenfield%28_,shouldadd,at%29.md)
  Allows the delegate to validate the tokens to be added to the receiver at a particular location.
### Reading To and Writing From the Pasteboard
- [func tokenField(NSTokenField, readFrom: NSPasteboard) -> [Any]?](./nstokenfielddelegate/tokenfield%28_,readfrom%29.md)
  Allows the delegate to return an array of objects representing the data read from the specified pasteboard.
- [func tokenField(NSTokenField, writeRepresentedObjects: [Any], to: NSPasteboard) -> Bool](./nstokenfielddelegate/tokenfield%28_,writerepresentedobjects,to%29.md)
  Sent so the delegate can write represented objects to the pasteboard corresponding to a given array of display strings.
### Managing Menus for Represented Objects
- [func tokenField(NSTokenField, hasMenuForRepresentedObject: Any) -> Bool](./nstokenfielddelegate/tokenfield%28_,hasmenuforrepresentedobject%29.md)
  Allows the delegate to specify whether the given represented object provides a menu.
- [func tokenField(NSTokenField, menuForRepresentedObject: Any) -> NSMenu?](./nstokenfielddelegate/tokenfield%28_,menuforrepresentedobject%29.md)
  Allows the delegate to provide a menu for the specified represented object.

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](./nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTextFieldDelegate](./nstextfielddelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate)*