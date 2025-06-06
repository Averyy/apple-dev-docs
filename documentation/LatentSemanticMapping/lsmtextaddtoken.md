# LSMTextAddToken(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Adds an arbitrary binary token to the text.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMTextAddToken(_ textref: LSMText, _ token: CFData) -> OSStatus
```

#### Discussion

The order of tokens is significant if the map uses pairs or triplets, and the count of tokens is always significant.

## See Also

- [func LSMTextAddWord(LSMText, CFString) -> OSStatus](lsmtextaddword(_:_:).md)
  Adds a word to the text.
- [func LSMTextAddWords(LSMText, CFString, CFLocale?, CFOptionFlags) -> OSStatus](lsmtextaddwords(_:_:_:_:).md)
  Breaks a string into words using the specified locale, and adds the words to the text.
- [Parsing Flags](parsing-flags.md)
  Options for parsing words to add to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmtextaddtoken(_:_:))*