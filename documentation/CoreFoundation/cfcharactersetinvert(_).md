# CFCharacterSetInvert(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Inverts the content of a given character set.

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
func CFCharacterSetInvert(_ theSet: CFMutableCharacterSet!)
```

```c
extern void CFCharacterSetInvert(CFMutableCharacterSetRef theSet);
```

## Parameters

- `theSet`: The character set to invert.

## See Also

### Logical Operations
- [func CFCharacterSetIntersect(CFMutableCharacterSet!, CFCharacterSet!)](./cfcharactersetintersect%28_,_%29.md)
  Forms an intersection of two character sets.
- [func CFCharacterSetUnion(CFMutableCharacterSet!, CFCharacterSet!)](./cfcharactersetunion%28_,_%29.md)
  Forms the union of two character sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetinvert(_:))*