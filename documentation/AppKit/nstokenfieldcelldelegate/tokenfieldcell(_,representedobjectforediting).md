# tokenFieldCell(_:representedObjectForEditing:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to provide a represented object for the string being edited.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, representedObjectForEditing editingString: String) -> Any?
```

```objc
- (id) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell representedObjectForEditingString:(NSString *) editingString;
```

#### Return Value

A represented object that is displayed rather than the editing string.

#### Discussion

If your application uses some object other than an `NSString` for their represented objects, you should return a new, autoreleased instance of that object from this method.

> **Note**:  In OS X v10.4, `NSTokenField` trims whitespace around tokens but it does not trim whitespace in macOS versions 10.5.0 and 10.5.1. In OS X v10.5.2, you get whitespace-trimming behavior by either linking against the v10.4 binary or linking against the v10.5 binary and *not* implementing the this method. If you do not want the whitespace-trimming behavior, link against the v10.5 binary and implement this method, returning the editing string if you have no represented object.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `editingString`: The edited string representation of a represented object.

## See Also

### Editing a Tokenized Strings
- [func tokenFieldCell(NSTokenFieldCell, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [Any]](./tokenfieldcell%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenFieldCell(NSTokenFieldCell, editingStringForRepresentedObject: Any) -> String?](./tokenfieldcell%28_,editingstringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be edited as a proxy for the represented object.
- [func tokenFieldCell(NSTokenFieldCell, shouldAdd: [Any], at: Int) -> [Any]](./tokenfieldcell%28_,shouldadd,at%29.md)
  Allows the delegate to validate the tokens to be added to the receiver at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:representedobjectforediting:))*