# replaceCharacters(in:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the characters in the given range with the characters of the given string.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func replaceCharacters(in range: NSRange, with str: String)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withString:(NSString *) str;
```

## Discussion

The new characters inherit the attributes of the first replaced character from `range`. Where the length of `range` is 0, the new characters inherit the attributes of the character preceding `range` if it has any, otherwise of the character following `range`.

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: A range specifying the characters to replace.
- `str`: A string specifying the characters to replace those in `range`.

## See Also

### Changing Characters
- [func deleteCharacters(in: NSRange)](./deletecharacters%28in%29.md)
  Deletes the characters in the given range along with their associated attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-6oq9r)*