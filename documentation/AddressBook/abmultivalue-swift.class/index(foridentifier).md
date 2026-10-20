# index(forIdentifier:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the index for the given identifier.

**Availability**:
- macOS

## Declaration

```swift
func index(forIdentifier identifier: String!) -> Int
```

```objc
- (NSUInteger) indexForIdentifier:(NSString *) identifier;
```

#### Discussion

If the identifier is not found, returns `NSNotFound`.

## Parameters

- `identifier`: The identifier whose index will be returned.

## See Also

### Accessing identifiers
- [func identifier(at: Int) -> String!](./identifier%28at%29.md)
  Returns the identifier for the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class/index(foridentifier:))*