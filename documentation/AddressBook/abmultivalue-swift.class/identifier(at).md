# identifier(at:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the identifier for the given index.

**Availability**:
- macOS

## Declaration

```swift
func identifier(at index: Int) -> String!
```

```objc
- (NSString *) identifierAtIndex:(NSUInteger) index;
```

## Discussion

If the `index` argument is out of bounds, this method raises an exception.

## Parameters

- `index`: The index of the identifier to be returned.

## See Also

### Accessing identifiers
- [func index(forIdentifier: String!) -> Int](./index%28foridentifier%29.md)
  Returns the index for the given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class/identifier(at:))*