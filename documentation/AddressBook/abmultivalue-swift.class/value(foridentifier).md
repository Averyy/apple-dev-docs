# value(forIdentifier:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the value for the given identifier.

**Availability**:
- macOS

## Declaration

```swift
func value(forIdentifier identifier: String!) -> Any!
```

```objc
- (id) valueForIdentifier:(NSString *) identifier;
```

## Discussion

If the identifier is not found, returns `nil`.

## Parameters

- `identifier`: The identifier for the value to be returned.

## See Also

### Accessing entries
- [func label(at: Int) -> String!](./label%28at%29.md)
  Returns the label for the given index.
- [func value(at: Int) -> Any!](./value%28at%29.md)
  Returns the value for the given index.
- [func label(forIdentifier: String!) -> Any!](./label%28foridentifier%29.md)
  Returns the label for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class/value(foridentifier:))*