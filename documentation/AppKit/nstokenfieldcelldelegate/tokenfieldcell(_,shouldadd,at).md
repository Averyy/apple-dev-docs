# tokenFieldCell(_:shouldAdd:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to validate the tokens to be added to the receiver at a given index.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, shouldAdd tokens: [Any], at index: Int) -> [Any]
```

```objc
- (NSArray *) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell shouldAddObjects:(NSArray *) tokens atIndex:(NSUInteger) index;
```

#### Return Value

An array of validated tokens.

#### Discussion

The delegate can return the array unchanged or return a modified array of tokens. To reject the add completely, return an empty array. Returning `nil` causes an error.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `tokens`: An array of tokens to be inserted in the receiver at `index`.
- `index`: The index of the receiver in which the array of tokens to be validated (`tokens`) will be inserted.

## See Also

### Editing a Tokenized Strings
- [func tokenFieldCell(NSTokenFieldCell, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [Any]](./tokenfieldcell%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenFieldCell(NSTokenFieldCell, editingStringForRepresentedObject: Any) -> String?](./tokenfieldcell%28_,editingstringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be edited as a proxy for the represented object.
- [func tokenFieldCell(NSTokenFieldCell, representedObjectForEditing: String) -> Any?](./tokenfieldcell%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the string being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:shouldadd:at:))*