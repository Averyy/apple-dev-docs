# deleteCharacters(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Deletes the characters in the given range along with their associated attributes.

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
func deleteCharacters(in range: NSRange)
```

```objc
- (void) deleteCharactersInRange:(NSRange) range;
```

## Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: A range specifying the characters to delete.

## See Also

### Related Documentation
- [func replaceCharacters(in: NSRange, with: NSAttributedString)](./replacecharacters%28in,with%29-1uaw7.md)
  Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.
### Changing Characters
- [func replaceCharacters(in: NSRange, with: String)](./replacecharacters%28in,with%29-6oq9r.md)
  Replaces the characters in the given range with the characters of the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/deletecharacters(in:))*