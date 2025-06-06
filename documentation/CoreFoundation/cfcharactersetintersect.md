# CFCharacterSetIntersect(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Forms an intersection of two character sets.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFCharacterSetIntersect(_ theSet: CFMutableCharacterSet!, _ theOtherSet: CFCharacterSet!)
```

## Parameters

- `theSet`: The source character set, modified by intersection with  .
- `theOtherSet`: The character set with which the intersection is formed.

## See Also

- [func CFCharacterSetInvert(CFMutableCharacterSet!)](cfcharactersetinvert(_:).md)
  Inverts the content of a given character set.
- [func CFCharacterSetUnion(CFMutableCharacterSet!, CFCharacterSet!)](cfcharactersetunion(_:_:).md)
  Forms the union of two character sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetintersect(_:_:))*