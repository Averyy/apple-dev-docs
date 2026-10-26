# setAttributedString(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the receiver’s entire contents with the characters and attributes of the given attributed string.

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
func setAttributedString(_ attrString: NSAttributedString)
```

```objc
- (void) setAttributedString:(NSAttributedString *) attrString;
```

## Parameters

- `attrString`: The attributed string whose characters and attributes replace those in the receiver.

## See Also

### Changing Characters and Attributes
- [func append(NSAttributedString)](./append%28_%29.md)
  Adds the characters and attributes of a given attributed string to the end of the receiver.
- [func insert(NSAttributedString, at: Int)](./insert%28_,at%29.md)
  Inserts the characters and attributes of the given attributed string into the receiver at the given index.
- [func replaceCharacters(in: NSRange, with: NSAttributedString)](./replacecharacters%28in,with%29-1uaw7.md)
  Replaces the characters and attributes in a given range with the characters and attributes of the given attributed string.
- [- appendLocalizedFormat:](./appendlocalizedformat_.md)
  Formats the specified string and arguments with the current locale, then appends the result to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/setattributedstring(_:))*