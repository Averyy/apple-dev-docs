# LSMTextAddWord(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Adds a word to the text.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMTextAddWord(_ textref: LSMText, _ word: CFString) -> OSStatus
```

#### Discussion

The order of words is significant if the map uses pairs or triplets, and the count of words is always significant.

## See Also

- [func LSMTextAddToken(LSMText, CFData) -> OSStatus](lsmtextaddtoken(_:_:).md)
  Adds an arbitrary binary token to the text.
- [func LSMTextAddWords(LSMText, CFString, CFLocale?, CFOptionFlags) -> OSStatus](lsmtextaddwords(_:_:_:_:).md)
  Breaks a string into words using the specified locale, and adds the words to the text.
- [Parsing Flags](parsing-flags.md)
  Options for parsing words to add to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmtextaddword(_:_:))*