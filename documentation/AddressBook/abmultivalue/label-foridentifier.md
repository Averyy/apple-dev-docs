# label(forIdentifier:)

**Framework**: Address Book  
**Kind**: method

Returns the label for the given identifier.

**Availability**:
- macOS ?+

## Declaration

```swift
func label(forIdentifier identifier: String!) -> Any!
```

#### Discussion

If the identifier is not found, this method returns `nil`.

## Parameters

- `identifier`: The identifier for the label to be returned.

## See Also

- [func label(at: Int) -> String!](abmultivalue/label(at:).md)
  Returns the label for the given index.
- [func value(at: Int) -> Any!](abmultivalue/value(at:).md)
  Returns the value for the given index.
- [func value(forIdentifier: String!) -> Any!](abmultivalue/value(foridentifier:).md)
  Returns the value for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue/label(foridentifier:))*