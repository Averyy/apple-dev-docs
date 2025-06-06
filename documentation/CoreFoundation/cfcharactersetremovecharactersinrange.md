# CFCharacterSetRemoveCharactersInRange(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a given range of Unicode characters from a character set.

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
func CFCharacterSetRemoveCharactersInRange(_ theSet: CFMutableCharacterSet!, _ theRange: CFRange)
```

## Parameters

- `theSet`: The character set to modify.
- `theRange`: The range to remove from the character set. The range is specified in 32-bits in UTF-32 format, and must lie within the valid Unicode character range (from   to  ).

## See Also

- [func CFCharacterSetRemoveCharactersInString(CFMutableCharacterSet!, CFString!)](cfcharactersetremovecharactersinstring(_:_:).md)
  Removes the characters in a given string from a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetremovecharactersinrange(_:_:))*