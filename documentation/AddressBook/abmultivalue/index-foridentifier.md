# index(forIdentifier:)

**Framework**: Address Book  
**Kind**: method

Returns the index for the given identifier.

**Availability**:
- macOS ?+

## Declaration

```swift
func index(forIdentifier identifier: String!) -> Int
```

#### Discussion

If the identifier is not found, returns `NSNotFound`.

## Parameters

- `identifier`: The identifier whose index will be returned.

## See Also

- [func identifier(at: Int) -> String!](abmultivalue/identifier(at:).md)
  Returns the identifier for the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/index(foridentifier:))*