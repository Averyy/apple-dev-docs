# LSMText

**Framework**: Latent Semantic Mapping  
**Kind**: class

An input text.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
class LSMText
```

#### Overview

An [`LSMText`](lsmtext.md) is a mutable, opaque Core Foundation type that represents an input text.

## Topics

### Creating a Text Object
- [func LSMTextCreate(CFAllocator?, LSMMap) -> Unmanaged<LSMText>](lsmtextcreate(_:_:).md)
  Creates a new text.
### Adding to the Text
- [func LSMTextAddToken(LSMText, CFData) -> OSStatus](lsmtextaddtoken(_:_:).md)
  Adds an arbitrary binary token to the text.
- [func LSMTextAddWord(LSMText, CFString) -> OSStatus](lsmtextaddword(_:_:).md)
  Adds a word to the text.
- [func LSMTextAddWords(LSMText, CFString, CFLocale?, CFOptionFlags) -> OSStatus](lsmtextaddwords(_:_:_:_:).md)
  Breaks a string into words using the specified locale, and adds the words to the text.
- [Parsing Flags](parsing-flags.md)
  Options for parsing words to add to the text.
### Getting the Type Identifier
- [func LSMTextGetTypeID() -> CFTypeID](lsmtextgettypeid().md)
  Returns the Core Foundation type identifier for Latent Semantic Mapping texts.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class LSMMap](lsmmap.md)
  A map between a set of categories and related text.
- [class LSMResult](lsmresult.md)
  A result of a lookup in a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmtext)*