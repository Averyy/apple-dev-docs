# replaceCharacters(in:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.

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
func replaceCharacters(in range: NSRange, with attrString: NSAttributedString)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withAttributedString:(NSAttributedString *) attrString;
```

#### Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `range`: The range of characters and attributes replaced.
- `attrString`: The attributed string whose characters and attributes replace those in the specified range.

## See Also

### Changing Characters and Attributes
- [func append(NSAttributedString)](./append%28_%29.md)
  Adds the characters and attributes of a given attributed string to the end of the receiver.
- [func insert(NSAttributedString, at: Int)](./insert%28_,at%29.md)
  Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [func setAttributedString(NSAttributedString)](./setattributedstring%28_%29.md)
  Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.
- [- appendLocalizedFormat:](./appendlocalizedformat_.md)
  Formats the specified string and arguments with the current locale, then appends the result to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/replacecharacters(in:with:)-1uaw7)*