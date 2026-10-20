# addCharacters(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds to the receiver the characters in a given string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addCharacters(in aString: String)
```

```objc
- (void) addCharactersInString:(NSString *) aString;
```

#### Discussion

This method has no effect if `aString` is empty.

## Parameters

- `aString`: The characters to add to the receiver.

## See Also

### Adding and Removing Characters
- [func addCharacters(in: NSRange)](./addcharacters%28in%29-4ppyw.md)
  Adds to the receiver the characters whose Unicode values are in a given range.
- [func removeCharacters(in: NSRange)](./removecharacters%28in%29-70nqp.md)
  Removes from the receiver the characters whose Unicode values are in a given range.
- [func removeCharacters(in: String)](./removecharacters%28in%29-762gt.md)
  Removes from the receiver the characters in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/addcharacters(in:)-7q02)*