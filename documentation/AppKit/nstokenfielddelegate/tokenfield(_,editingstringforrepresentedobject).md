# tokenField(_:editingStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to provide a string to be edited as a proxy for a represented object.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, editingStringForRepresentedObject representedObject: Any) -> String?
```

```objc
- (NSString *) tokenField:(NSTokenField *) tokenField editingStringForRepresentedObject:(id) representedObject;
```

#### Return Value

A string that’s an editable proxy of the represented object, or `nil` if the token should not be editable.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

### Editing a Tokenized Strings
- [func tokenField(NSTokenField, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>?) -> [Any]?](./tokenfield%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenField(NSTokenField, representedObjectForEditing: String) -> Any?](./tokenfield%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the given editing string.
- [func tokenField(NSTokenField, shouldAdd: [Any], at: Int) -> [Any]](./tokenfield%28_,shouldadd,at%29.md)
  Allows the delegate to validate the tokens to be added to the receiver at a particular location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:editingstringforrepresentedobject:))*