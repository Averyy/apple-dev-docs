# CFCharacterSetRemoveCharactersInString(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes the characters in a given string from a character set.

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
func CFCharacterSetRemoveCharactersInString(_ theSet: CFMutableCharacterSet!, _ theString: CFString!)
```

```c
extern void CFCharacterSetRemoveCharactersInString(CFMutableCharacterSetRef theSet, CFStringRef theString);
```

## Parameters

- `theSet`: The character set to modify.
- `theString`: A string containing the characters to remove from `theSet`.

## See Also

### Removing Characters
- [func CFCharacterSetRemoveCharactersInRange(CFMutableCharacterSet!, CFRange)](./cfcharactersetremovecharactersinrange%28_,_%29.md)
  Removes a given range of Unicode characters from a character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharactersetremovecharactersinstring(_:_:))*