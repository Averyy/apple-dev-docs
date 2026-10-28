# CFStringGetSurrogatePairForLongCharacter(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.

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
func CFStringGetSurrogatePairForLongCharacter(_ character: UTF32Char, _ surrogates: UnsafeMutablePointer<UniChar>!) -> Bool
```

```c
static Boolean CFStringGetSurrogatePairForLongCharacter(UTF32Char character, UniChar *surrogates);
```

## Return Value

`true` if `character` is mapped to a surrogate pair, otherwise `false`.

## Parameters

- `character`: A UTF-32 character.
- `surrogates`: A buffer to contain the returned surrogate pair.

  The buffer must have space for at least 2 UTF-16 characters.

## See Also

### Managing Surrogates
- [func CFStringGetLongCharacterForSurrogatePair(UniChar, UniChar) -> UTF32Char](./cfstringgetlongcharacterforsurrogatepair%28_,_%29.md)
  Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [func CFStringIsSurrogateHighCharacter(UniChar) -> Bool](./cfstringissurrogatehighcharacter%28_%29.md)
  Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.
- [func CFStringIsSurrogateLowCharacter(UniChar) -> Bool](./cfstringissurrogatelowcharacter%28_%29.md)
  Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetsurrogatepairforlongcharacter(_:_:))*