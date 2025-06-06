# tokenFieldCell(_:completionsForSubstring:indexOfToken:indexOfSelectedItem:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide an array of appropriate completions for the contents of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, completionsForSubstring substring: String, indexOfToken tokenIndex: Int, indexOfSelectedItem selectedIndex: UnsafeMutablePointer<Int>) -> [Any]
```

#### Return Value

An array of strings that are possible completions.

#### Discussion

If the delegate does not implement this method, no completions are provided.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `substring`: The partial string that is to be completed.
- `tokenIndex`: The index of the token being edited.
- `selectedIndex`: Optionally, you can return by-reference an index into the returned array that specifies which of the completions should be initially selected. If none are to be selected, return by reference  .

## See Also

- [func tokenFieldCell(NSTokenFieldCell, editingStringForRepresentedObject: Any) -> String?](nstokenfieldcelldelegate/tokenfieldcell(_:editingstringforrepresentedobject:).md)
  Allows the delegate to provide a string to be edited as a proxy for the represented object.
- [func tokenFieldCell(NSTokenFieldCell, representedObjectForEditing: String) -> Any?](nstokenfieldcelldelegate/tokenfieldcell(_:representedobjectforediting:).md)
  Allows the delegate to provide a represented object for the string being edited.
- [func tokenFieldCell(NSTokenFieldCell, shouldAdd: [Any], at: Int) -> [Any]](nstokenfieldcelldelegate/tokenfieldcell(_:shouldadd:at:).md)
  Allows the delegate to validate the tokens to be added to the receiver at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:completionsforsubstring:indexoftoken:indexofselecteditem:))*