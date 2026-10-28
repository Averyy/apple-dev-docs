# value(at:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the value for the given index.

**Availability**:
- macOS

## Declaration

```swift
func value(at index: Int) -> Any!
```

```objc
- (id) valueAtIndex:(NSUInteger) index;
```

## Discussion

If the `index` argument is out of bounds, this method raises an exception.

## Parameters

- `index`: The index for the value to be returned.

## See Also

### Accessing entries
- [func label(at: Int) -> String!](./label%28at%29.md)
  Returns the label for the given index.
- [func value(forIdentifier: String!) -> Any!](./value%28foridentifier%29.md)
  Returns the value for the given identifier.
- [func label(forIdentifier: String!) -> Any!](./label%28foridentifier%29.md)
  Returns the label for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class/value(at:))*