# tokenFieldCell(_:editingStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide a string to be edited as a proxy for the represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, editingStringForRepresentedObject representedObject: Any) -> String?
```

#### Return Value

A string that’s an editable proxy of the represented object, or `nil` if the token should not be editable.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenFieldCell(NSTokenFieldCell, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [Any]](nstokenfieldcelldelegate/tokenfieldcell(_:completionsforsubstring:indexoftoken:indexofselecteditem:).md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenFieldCell(NSTokenFieldCell, representedObjectForEditing: String) -> Any?](nstokenfieldcelldelegate/tokenfieldcell(_:representedobjectforediting:).md)
  Allows the delegate to provide a represented object for the string being edited.
- [func tokenFieldCell(NSTokenFieldCell, shouldAdd: [Any], at: Int) -> [Any]](nstokenfieldcelldelegate/tokenfieldcell(_:shouldadd:at:).md)
  Allows the delegate to validate the tokens to be added to the receiver at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:editingstringforrepresentedobject:))*