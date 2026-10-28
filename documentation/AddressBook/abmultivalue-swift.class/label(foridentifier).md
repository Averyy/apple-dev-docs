# label(forIdentifier:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the label for the given identifier.

**Availability**:
- macOS

## Declaration

```swift
func label(forIdentifier identifier: String!) -> Any!
```

```objc
- (id) labelForIdentifier:(NSString *) identifier;
```

## Discussion

If the identifier is not found, this method returns `nil`.

## Parameters

- `identifier`: The identifier for the label to be returned.

## See Also

### Accessing entries
- [func label(at: Int) -> String!](./label%28at%29.md)
  Returns the label for the given index.
- [func value(at: Int) -> Any!](./value%28at%29.md)
  Returns the value for the given index.
- [func value(forIdentifier: String!) -> Any!](./value%28foridentifier%29.md)
  Returns the value for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class/label(foridentifier:))*