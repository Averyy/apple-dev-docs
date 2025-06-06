# replaceCharacters(in:with:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

The new characters inherit the attributes of the first replaced character from `range`. Where the length of `range` is 0, the new characters inherit the attributes of the character preceding `range` if it has any, otherwise of the character following `range`.

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: A range specifying the characters to replace.
- `str`: A string specifying the characters to replace those in  .

## See Also

- [func deleteCharacters(in: NSRange)](nsmutableattributedstring/deletecharacters(in:).md)
  Deletes the characters in the given range along with their associated attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-6oq9r)*