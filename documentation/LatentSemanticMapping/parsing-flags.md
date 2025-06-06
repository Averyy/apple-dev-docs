# Parsing Flags

**Framework**: Latent Semantic Mapping

Options for parsing words to add to the text.

#### Overview

Specify these options for [`LSMTextAddWords(_:_:_:_:)`](lsmtextaddwords(_:_:_:_:).md).

## Topics

### Constants
- [var kLSMTextApplySpamHeuristics: Int](klsmtextapplyspamheuristics.md)
  An option that specifies the parser should attempt to find words in hostile text.
- [var kLSMTextPreserveAcronyms: Int](klsmtextpreserveacronyms.md)
  An option that specifies the parser shouldn’t map all-uppercase words to lowercase.
- [var kLSMTextPreserveCase: Int](klsmtextpreservecase.md)
  An option that specifies the parser shouldn’t change any words to lowercase.

## See Also

- [func LSMTextAddToken(LSMText, CFData) -> OSStatus](lsmtextaddtoken(_:_:).md)
  Adds an arbitrary binary token to the text.
- [func LSMTextAddWord(LSMText, CFString) -> OSStatus](lsmtextaddword(_:_:).md)
  Adds a word to the text.
- [func LSMTextAddWords(LSMText, CFString, CFLocale?, CFOptionFlags) -> OSStatus](lsmtextaddwords(_:_:_:_:).md)
  Breaks a string into words using the specified locale, and adds the words to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/parsing-flags)*