# CFStringIsSurrogateLowCharacter(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.

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
func CFStringIsSurrogateLowCharacter(_ character: UniChar) -> Bool
```

```c
static Boolean CFStringIsSurrogateLowCharacter(UniChar character);
```

#### Return Value

`true` if `character` is a low character in a surrogate pair, otherwise `false`.

## Parameters

- `character`: A UTF-16 character.

## See Also

### Managing Surrogates
- [func CFStringGetLongCharacterForSurrogatePair(UniChar, UniChar) -> UTF32Char](./cfstringgetlongcharacterforsurrogatepair%28_,_%29.md)
  Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [func CFStringGetSurrogatePairForLongCharacter(UTF32Char, UnsafeMutablePointer<UniChar>!) -> Bool](./cfstringgetsurrogatepairforlongcharacter%28_,_%29.md)
  Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [func CFStringIsSurrogateHighCharacter(UniChar) -> Bool](./cfstringissurrogatehighcharacter%28_%29.md)
  Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringissurrogatelowcharacter(_:))*