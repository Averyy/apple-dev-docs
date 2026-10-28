# Parsing Flags

**Framework**: Latent Semantic Mapping  
**Role**: API Collection

Options for parsing words to add to the text.

## Overview

Specify these options for [`LSMTextAddWords(_:_:_:_:)`](./lsmtextaddwords%28_,_,_,_%29.md).

## Topics

### Constants
- [var kLSMTextApplySpamHeuristics: Int](./klsmtextapplyspamheuristics.md)
  An option that specifies the parser should attempt to find words in hostile text.
- [var kLSMTextPreserveAcronyms: Int](./klsmtextpreserveacronyms.md)
  An option that specifies the parser shouldn’t map all-uppercase words to lowercase.
- [var kLSMTextPreserveCase: Int](./klsmtextpreservecase.md)
  An option that specifies the parser shouldn’t change any words to lowercase.

## See Also

### Adding to the Text
- [func LSMTextAddToken(LSMText, CFData) -> OSStatus](./lsmtextaddtoken%28_,_%29.md)
  Adds an arbitrary binary token to the text.
- [func LSMTextAddWord(LSMText, CFString) -> OSStatus](./lsmtextaddword%28_,_%29.md)
  Adds a word to the text.
- [func LSMTextAddWords(LSMText, CFString, CFLocale?, CFOptionFlags) -> OSStatus](./lsmtextaddwords%28_,_,_,_%29.md)
  Breaks a string into words using the specified locale, and adds the words to the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/parsing-flags)*