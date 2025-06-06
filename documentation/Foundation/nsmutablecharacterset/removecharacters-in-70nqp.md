# removeCharacters(in:)

**Framework**: Foundation  
**Kind**: method

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

## Parameters

- `aRange`: The range of characters to remove.    is the value of the first character to remove;   is the value of the last. If   is  , this method has no effect.

## See Also

- [func addCharacters(in: NSRange)](nsmutablecharacterset/addcharacters(in:)-4ppyw.md)
  Adds to the receiver the characters whose Unicode values are in a given range.
- [func addCharacters(in: String)](nsmutablecharacterset/addcharacters(in:)-7q02.md)
  Adds to the receiver the characters in a given string.
- [func removeCharacters(in: String)](nsmutablecharacterset/removecharacters(in:)-762gt.md)
  Removes from the receiver the characters in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/removecharacters(in:)-70nqp)*