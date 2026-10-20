# CFCharacterSetAddCharactersInString(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds the characters in a given string to a character set.

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
func CFCharacterSetAddCharactersInString(_ theSet: CFMutableCharacterSet!, _ theString: CFString!)
```

```c
extern void CFCharacterSetAddCharactersInString(CFMutableCharacterSetRef theSet, CFStringRef theString);
```

## Parameters

- `theSet`: The character set to modify.
- `theString`: A string containing the characters to add to `theSet`.

## See Also

### Adding Characters
- [func CFCharacterSetAddCharactersInRange(CFMutableCharacterSet!, CFRange)](./cfcharactersetaddcharactersinrange%28_,_%29.md)
  Adds a given range to a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetaddcharactersinstring(_:_:))*