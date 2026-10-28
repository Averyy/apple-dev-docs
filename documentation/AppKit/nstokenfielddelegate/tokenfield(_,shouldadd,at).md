# tokenField(_:shouldAdd:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to validate the tokens to be added to the receiver at a particular location.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, shouldAdd tokens: [Any], at index: Int) -> [Any]
```

```objc
- (NSArray *) tokenField:(NSTokenField *) tokenField shouldAddObjects:(NSArray *) tokens atIndex:(NSUInteger) index;
```

## Return Value

An array of validated tokens.

## Discussion

The delegate can return the array unchanged or return a modified array of tokens. To reject the add completely, return an empty array. Returning `nil` causes an error.

## Parameters

- `tokenField`: The token field that sent the message.
- `tokens`: An array of tokens to be inserted in the receiver at `index`.
- `index`: The index of the receiver in which the array of tokens to be validated (`tokens`) will be inserted.

## See Also

### Editing a Tokenized Strings
- [func tokenField(NSTokenField, completionsForSubstring: String, indexOfToken: Int, indexOfSelectedItem: UnsafeMutablePointer<Int>?) -> [Any]?](./tokenfield%28_,completionsforsubstring,indexoftoken,indexofselecteditem%29.md)
  Allows the delegate to provide an array of appropriate completions for the contents of the receiver.
- [func tokenField(NSTokenField, editingStringForRepresentedObject: Any) -> String?](./tokenfield%28_,editingstringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be edited as a proxy for a represented object.
- [func tokenField(NSTokenField, representedObjectForEditing: String) -> Any?](./tokenfield%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the given editing string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:shouldadd:at:))*