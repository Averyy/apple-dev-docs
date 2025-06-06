# tokenFieldCell(_:shouldAdd:at:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to validate the tokens to be added to the receiver at a given index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, shouldAdd tokens: [Any], at index: Int) -> [Any]
```

#### Return Value

An array of validated tokens.

#### Discussion

The delegate can return the array unchanged or return a modified array of tokens. To reject the add completely, return an empty array. Returning `nil` causes an error.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `tokens`: An array of tokens to be inserted in the receiver at  .
- `index`: The index of the receiver in which the array of tokens to be validated ( ) will be inserted.

## See Also

- [func tokenFieldCell(NSTokenFieldCell, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [Any]](nstokenfieldcelldelegate/tokenfieldcell(_:completionsforsubstring:indexoftoken:indexofselecteditem:).md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenFieldCell(NSTokenFieldCell, editingStringForRepresentedObject: Any) -> String?](nstokenfieldcelldelegate/tokenfieldcell(_:editingstringforrepresentedobject:).md)
  Allows the delegate to provide a string to be edited as a proxy for the represented object.
- [func tokenFieldCell(NSTokenFieldCell, representedObjectForEditing: String) -> Any?](nstokenfieldcelldelegate/tokenfieldcell(_:representedobjectforediting:).md)
  Allows the delegate to provide a represented object for the string being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:shouldadd:at:))*