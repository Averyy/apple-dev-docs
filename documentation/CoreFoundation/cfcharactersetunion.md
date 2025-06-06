# CFCharacterSetUnion(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Forms the union of two character sets.

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
func CFCharacterSetUnion(_ theSet: CFMutableCharacterSet!, _ theOtherSet: CFCharacterSet!)
```

## Parameters

- `theSet`: The source character set, modified by union with  .
- `theOtherSet`: The character set with which the union is formed.

## See Also

- [func CFCharacterSetIntersect(CFMutableCharacterSet!, CFCharacterSet!)](cfcharactersetintersect(_:_:).md)
  Forms an intersection of two character sets.
- [func CFCharacterSetInvert(CFMutableCharacterSet!)](cfcharactersetinvert(_:).md)
  Inverts the content of a given character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetunion(_:_:))*