# tokenField(_:completionsForSubstring:indexOfToken:indexOfSelectedItem:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide an array of appropriate completions for the contents of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, completionsForSubstring substring: String, indexOfToken tokenIndex: Int, indexOfSelectedItem selectedIndex: UnsafeMutablePointer<Int>?) -> [Any]?
```

#### Return Value

An array of strings that are possible completions.

#### Discussion

If the delegate does not implement this method, no completions are provided.

## Parameters

- `tokenField`: The token field where editing is occurring.
- `substring`: The partial string that is to be completed.
- `tokenIndex`: The index of the token being edited.
- `selectedIndex`: Optionally, you can return by-reference an index into the returned array that specifies which of the completions should be initially selected. If none are to be selected, return by reference  .

## See Also

- [func tokenField(NSTokenField, editingStringForRepresentedObject: Any) -> String?](nstokenfielddelegate/tokenfield(_:editingstringforrepresentedobject:).md)
  Allows the delegate to provide a string to be edited as a proxy for a represented object.
- [func tokenField(NSTokenField, representedObjectForEditing: String) -> Any?](nstokenfielddelegate/tokenfield(_:representedobjectforediting:).md)
  Allows the delegate to provide a represented object for the given editing string.
- [func tokenField(NSTokenField, shouldAdd: [Any], at: Int) -> [Any]](nstokenfielddelegate/tokenfield(_:shouldadd:at:).md)
  Allows the delegate to validate the tokens to be added to the receiver at a particular location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:completionsforsubstring:indexoftoken:indexofselecteditem:))*