# identifier(at:)

**Framework**: Address Book  
**Kind**: method

Returns the identifier for the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func identifier(at index: Int) -> String!
```

#### Discussion

If the `index` argument is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the identifier to be returned.

## See Also

- [func index(forIdentifier: String!) -> Int](abmultivalue/index(foridentifier:).md)
  Returns the index for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/identifier(at:))*