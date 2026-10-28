# tokenFieldCell(_:editingStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to provide a string to be edited as a proxy for the represented object.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, editingStringForRepresentedObject representedObject: Any) -> String?
```

```objc
- (NSString *) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell editingStringForRepresentedObject:(id) representedObject;
```

## Return Value

A string that’s an editable proxy of the represented object, or `nil` if the token should not be editable.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

### Editing a Tokenized Strings
- [func tokenFieldCell(NSTokenFieldCell, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [Any]](./tokenfieldcell%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenFieldCell(NSTokenFieldCell, representedObjectForEditing: String) -> Any?](./tokenfieldcell%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the string being edited.
- [func tokenFieldCell(NSTokenFieldCell, shouldAdd: [Any], at: Int) -> [Any]](./tokenfieldcell%28_,shouldadd,at%29.md)
  Allows the delegate to validate the tokens to be added to the receiver at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:editingstringforrepresentedobject:))*