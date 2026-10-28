# tokenField(_:completionsForSubstring:indexOfToken:indexOfSelectedItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to provide an array of appropriate completions for the contents of the receiver.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, completionsForSubstring substring: String, indexOfToken tokenIndex: Int, indexOfSelectedItem selectedIndex: UnsafeMutablePointer<Int>?) -> [Any]?
```

```objc
- (NSArray *) tokenField:(NSTokenField *) tokenField completionsForSubstring:(NSString *) substring indexOfToken:(NSInteger) tokenIndex indexOfSelectedItem:(NSInteger *) selectedIndex;
```

## Return Value

An array of strings that are possible completions.

## Discussion

If the delegate does not implement this method, no completions are provided.

## Parameters

- `tokenField`: The token field where editing is occurring.
- `substring`: The partial string that is to be completed.
- `tokenIndex`: The index of the token being edited.
- `selectedIndex`: Optionally, you can return by-reference an index into the returned array that specifies which of the completions should be initially selected. If none are to be selected, return by reference `-1`.

## See Also

### Editing a Tokenized Strings
- [func tokenField(NSTokenField, editingStringForRepresentedObject: Any) -> String?](./tokenfield%28_,editingstringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be edited as a proxy for a represented object.
- [func tokenField(NSTokenField, representedObjectForEditing: String) -> Any?](./tokenfield%28_,representedobjectforediting%29.md)
  Allows the delegate to provide a represented object for the given editing string.
- [func tokenField(NSTokenField, shouldAdd: [Any], at: Int) -> [Any]](./tokenfield%28_,shouldadd,at%29.md)
  Allows the delegate to validate the tokens to be added to the receiver at a particular location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:completionsforsubstring:indexoftoken:indexofselecteditem:))*