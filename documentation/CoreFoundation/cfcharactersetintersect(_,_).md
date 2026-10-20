# CFCharacterSetIntersect(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Forms an intersection of two character sets.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFCharacterSetIntersect(_ theSet: CFMutableCharacterSet!, _ theOtherSet: CFCharacterSet!)
```

```c
extern void CFCharacterSetIntersect(CFMutableCharacterSetRef theSet, CFCharacterSetRef theOtherSet);
```

## Parameters

- `theSet`: The source character set, modified by intersection with `theOtherSet`.
- `theOtherSet`: The character set with which the intersection is formed.

## See Also

### Logical Operations
- [func CFCharacterSetInvert(CFMutableCharacterSet!)](./cfcharactersetinvert%28_%29.md)
  Inverts the content of a given character set.
- [func CFCharacterSetUnion(CFMutableCharacterSet!, CFCharacterSet!)](./cfcharactersetunion%28_,_%29.md)
  Forms the union of two character sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetintersect(_:_:))*