# value(forIdentifier:)

**Framework**: Address Book  
**Kind**: method

Returns the value for the given identifier.

**Availability**:
- macOS ?+

## Declaration

```swift
func value(forIdentifier identifier: String!) -> Any!
```

#### Discussion

If the identifier is not found, returns `nil`.

## Parameters

- `identifier`: The identifier for the value to be returned.

## See Also

- [func label(at: Int) -> String!](abmultivalue/label(at:).md)
  Returns the label for the given index.
- [func value(at: Int) -> Any!](abmultivalue/value(at:).md)
  Returns the value for the given index.
- [func label(forIdentifier: String!) -> Any!](abmultivalue/label(foridentifier:).md)
  Returns the label for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/value(foridentifier:))*