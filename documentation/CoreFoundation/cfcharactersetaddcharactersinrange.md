# CFCharacterSetAddCharactersInRange(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a given range to a character set.

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
func CFCharacterSetAddCharactersInRange(_ theSet: CFMutableCharacterSet!, _ theRange: CFRange)
```

## Parameters

- `theSet`: The character set to modify.
- `theRange`: The range to add to the character set. The range is specified in 32-bits in UTF-32 format, and must lie within the valid Unicode character range (from   to  ).

## See Also

- [func CFCharacterSetAddCharactersInString(CFMutableCharacterSet!, CFString!)](cfcharactersetaddcharactersinstring(_:_:).md)
  Adds the characters in a given string to a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetaddcharactersinrange(_:_:))*