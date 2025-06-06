# LSMTextAddWords(_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Breaks a string into words using the specified locale, and adds the words to the text.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMTextAddWords(_ textref: LSMText, _ words: CFString, _ locale: CFLocale?, _ flags: CFOptionFlags) -> OSStatus
```

## See Also

- [func LSMTextAddToken(LSMText, CFData) -> OSStatus](lsmtextaddtoken(_:_:).md)
  Adds an arbitrary binary token to the text.
- [func LSMTextAddWord(LSMText, CFString) -> OSStatus](lsmtextaddword(_:_:).md)
  Adds a word to the text.
- [Parsing Flags](parsing-flags.md)
  Options for parsing words to add to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmtextaddwords(_:_:_:_:))*