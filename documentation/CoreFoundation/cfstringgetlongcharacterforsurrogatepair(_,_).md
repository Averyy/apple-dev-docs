# CFStringGetLongCharacterForSurrogatePair(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.

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
func CFStringGetLongCharacterForSurrogatePair(_ surrogateHigh: UniChar, _ surrogateLow: UniChar) -> UTF32Char
```

```c
static UTF32Char CFStringGetLongCharacterForSurrogatePair(UniChar surrogateHigh, UniChar surrogateLow);
```

## Return Value

A UTF32Char that corresponds to the combination of `surrogateHigh` and `surrogateLow`.

## Parameters

- `surrogateHigh`: The high surrogate character.
- `surrogateLow`: The low surrogate character.

## See Also

### Managing Surrogates
- [func CFStringGetSurrogatePairForLongCharacter(UTF32Char, UnsafeMutablePointer<UniChar>!) -> Bool](./cfstringgetsurrogatepairforlongcharacter%28_,_%29.md)
  Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [func CFStringIsSurrogateHighCharacter(UniChar) -> Bool](./cfstringissurrogatehighcharacter%28_%29.md)
  Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.
- [func CFStringIsSurrogateLowCharacter(UniChar) -> Bool](./cfstringissurrogatelowcharacter%28_%29.md)
  Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetlongcharacterforsurrogatepair(_:_:))*