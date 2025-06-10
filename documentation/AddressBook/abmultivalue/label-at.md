# label(at:)

**Framework**: Address Book  
**Kind**: method

Returns the label for the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func label(at index: Int) -> String!
```

#### Discussion

If the `index` argument is out of bounds, this method raises an exception.

## Parameters

- `index`: The index for the label to be returned.

## See Also

- [func value(at: Int) -> Any!](abmultivalue/value(at:).md)
  Returns the value for the given index.
- [func value(forIdentifier: String!) -> Any!](abmultivalue/value(foridentifier:).md)
  Returns the value for the given identifier.
- [func label(forIdentifier: String!) -> Any!](abmultivalue/label(foridentifier:).md)
  Returns the label for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/label(at:))*