# value(at:)

**Framework**: Address Book  
**Kind**: method

Returns the value for the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func value(at index: Int) -> Any!
```

#### Discussion

If the `index` argument is out of bounds, this method raises an exception.

## Parameters

- `index`: The index for the value to be returned.

## See Also

- [func label(at: Int) -> String!](abmultivalue/label(at:).md)
  Returns the label for the given index.
- [func value(forIdentifier: String!) -> Any!](abmultivalue/value(foridentifier:).md)
  Returns the value for the given identifier.
- [func label(forIdentifier: String!) -> Any!](abmultivalue/label(foridentifier:).md)
  Returns the label for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/value(at:))*