# LSMTextAddWords(_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Breaks a string into words using the specified locale, and adds the words to the text.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMTextAddWords(_ textref: LSMText, _ words: CFString, _ locale: CFLocale?, _ flags: CFOptionFlags) -> OSStatus
```

```c
OSStatus LSMTextAddWords(LSMTextRef textref, CFStringRef words, CFLocaleRef locale, CFOptionFlags flags);
```

## See Also

### Adding to the Text
- [func LSMTextAddToken(LSMText, CFData) -> OSStatus](./lsmtextaddtoken%28_,_%29.md)
  Adds an arbitrary binary token to the text.
- [func LSMTextAddWord(LSMText, CFString) -> OSStatus](./lsmtextaddword%28_,_%29.md)
  Adds a word to the text.
- [Parsing Flags](./parsing-flags.md)
  Options for parsing words to add to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmtextaddwords(_:_:_:_:))*