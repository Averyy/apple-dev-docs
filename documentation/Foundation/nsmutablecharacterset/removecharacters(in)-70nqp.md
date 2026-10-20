# removeCharacters(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes from the receiver the characters whose Unicode values are in a given range.

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
func removeCharacters(in aRange: NSRange)
```

```objc
- (void) removeCharactersInRange:(NSRange) aRange;
```

## Parameters

- `aRange`: The range of characters to remove. `aRange.location` is the value of the first character to remove; `aRange.location + aRange.length – 1` is the value of the last. If `aRange.length` is `0`, this method has no effect.

## See Also

### Adding and Removing Characters
- [func addCharacters(in: NSRange)](./addcharacters%28in%29-4ppyw.md)
  Adds to the receiver the characters whose Unicode values are in a given range.
- [func addCharacters(in: String)](./addcharacters%28in%29-7q02.md)
  Adds to the receiver the characters in a given string.
- [func removeCharacters(in: String)](./removecharacters%28in%29-762gt.md)
  Removes from the receiver the characters in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/removecharacters(in:)-70nqp)*