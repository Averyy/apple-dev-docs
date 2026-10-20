# CFCharacterSetRemoveCharactersInRange(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a given range of Unicode characters from a character set.

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
func CFCharacterSetRemoveCharactersInRange(_ theSet: CFMutableCharacterSet!, _ theRange: CFRange)
```

```c
extern void CFCharacterSetRemoveCharactersInRange(CFMutableCharacterSetRef theSet, CFRange theRange);
```

## Parameters

- `theSet`: The character set to modify.
- `theRange`: The range to remove from the character set. The range is specified in 32-bits in UTF-32 format, and must lie within the valid Unicode character range (from `0x00000` to `0x10FFFF`).

## See Also

### Removing Characters
- [func CFCharacterSetRemoveCharactersInString(CFMutableCharacterSet!, CFString!)](./cfcharactersetremovecharactersinstring%28_,_%29.md)
  Removes the characters in a given string from a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetremovecharactersinrange(_:_:))*