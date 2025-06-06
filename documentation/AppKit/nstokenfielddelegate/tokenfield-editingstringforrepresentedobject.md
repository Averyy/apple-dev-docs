# tokenField(_:editingStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide a string to be edited as a proxy for a represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, editingStringForRepresentedObject representedObject: Any) -> String?
```

#### Return Value

A string that’s an editable proxy of the represented object, or `nil` if the token should not be editable.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenField(NSTokenField, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>?) -> [Any]?](nstokenfielddelegate/tokenfield(_:completionsforsubstring:indexoftoken:indexofselecteditem:).md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenField(NSTokenField, representedObjectForEditing: String) -> Any?](nstokenfielddelegate/tokenfield(_:representedobjectforediting:).md)
  Allows the delegate to provide a represented object for the given editing string.
- [func tokenField(NSTokenField, shouldAdd: [Any], at: Int) -> [Any]](nstokenfielddelegate/tokenfield(_:shouldadd:at:).md)
  Allows the delegate to validate the tokens to be added to the receiver at a particular location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:editingstringforrepresentedobject:))*