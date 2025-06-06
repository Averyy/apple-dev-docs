# CFStringIsSurrogateHighCharacter(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.

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
func CFStringIsSurrogateHighCharacter(_ character: UniChar) -> Bool
```

#### Return Value

`true` if `character` is a high character in a surrogate pair, otherwise `false`.

## Parameters

- `character`: A UTF-16 character.

## See Also

- [func CFStringGetLongCharacterForSurrogatePair(UniChar, UniChar) -> UTF32Char](cfstringgetlongcharacterforsurrogatepair(_:_:).md)
  Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [func CFStringGetSurrogatePairForLongCharacter(UTF32Char, UnsafeMutablePointer<UniChar>!) -> Bool](cfstringgetsurrogatepairforlongcharacter(_:_:).md)
  Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [func CFStringIsSurrogateLowCharacter(UniChar) -> Bool](cfstringissurrogatelowcharacter(_:).md)
  Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringissurrogatehighcharacter(_:))*