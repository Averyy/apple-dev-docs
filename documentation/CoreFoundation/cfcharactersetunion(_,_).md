# CFCharacterSetUnion(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Forms the union of two character sets.

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
func CFCharacterSetUnion(_ theSet: CFMutableCharacterSet!, _ theOtherSet: CFCharacterSet!)
```

```c
extern void CFCharacterSetUnion(CFMutableCharacterSetRef theSet, CFCharacterSetRef theOtherSet);
```

## Parameters

- `theSet`: The source character set, modified by union with `theOtherSet`.
- `theOtherSet`: The character set with which the union is formed.

## See Also

### Logical Operations
- [func CFCharacterSetIntersect(CFMutableCharacterSet!, CFCharacterSet!)](./cfcharactersetintersect%28_,_%29.md)
  Forms an intersection of two character sets.
- [func CFCharacterSetInvert(CFMutableCharacterSet!)](./cfcharactersetinvert%28_%29.md)
  Inverts the content of a given character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetunion(_:_:))*