# CFStringTokenizer

**Framework**: Core Foundation  
**Kind**: class

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
class CFStringTokenizer
```

#### Overview

CFStringTokenizer allows you to tokenize strings into words, sentences or paragraphs in a language-neutral way. It supports languages such as Japanese and Chinese that do not delimit words by spaces, as well as de-compounding German compounds. You can obtain Latin transcription for tokens. It also provides language identification API.

You can use a CFStringTokenizer to break a string into tokens (sub-strings) on the basis of words, sentences, or paragraphs. When you create a tokenizer, you can supply options to further modify the tokenization—see [`Tokenization Modifiers`](1588024-tokenization-modifiers.md).

In addition, with CFStringTokenizer:

- You can de-compound German compounds
- You can identify the language used in a string (using [`CFStringTokenizerCopyBestStringLanguage(_:_:)`](cfstringtokenizercopybeststringlanguage(_:_:).md))
- You can obtain Latin transcription for tokens

To find a token that includes the character specified by character index and set it as the current token, you call [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](cfstringtokenizergototokenatindex(_:_:).md). To advance to the next token and set it as the current token, you call [`CFStringTokenizerAdvanceToNextToken(_:)`](cfstringtokenizeradvancetonexttoken(_:).md). To get the range of current token, you call [`CFStringTokenizerGetCurrentTokenRange(_:)`](cfstringtokenizergetcurrenttokenrange(_:).md). You can use         [`CFStringTokenizerCopyCurrentTokenAttribute(_:_:)`](cfstringtokenizercopycurrenttokenattribute(_:_:).md) to get the attribute of the current token. If the current token is a compound, you can call [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](cfstringtokenizergetcurrentsubtokens(_:_:_:_:).md) to retrieve the subtokens or derived subtokens contained in the compound token. To guess the language of a string, you call [`CFStringTokenizerCopyBestStringLanguage(_:_:)`](cfstringtokenizercopybeststringlanguage(_:_:).md).

## Topics

### Creating a Tokenizer
- [func CFStringTokenizerCreate(CFAllocator!, CFString!, CFRange, CFOptionFlags, CFLocale!) -> CFStringTokenizer!](cfstringtokenizercreate(_:_:_:_:_:).md)
  Returns a tokenizer for a given string.
### Setting the String
- [func CFStringTokenizerSetString(CFStringTokenizer!, CFString!, CFRange)](cfstringtokenizersetstring(_:_:_:).md)
  Sets the string for a tokenizer.
### Changing the Location
- [func CFStringTokenizerAdvanceToNextToken(CFStringTokenizer!) -> CFStringTokenizerTokenType](cfstringtokenizeradvancetonexttoken(_:).md)
  Advances the tokenizer to the next token and sets that as the current token.
- [func CFStringTokenizerGoToTokenAtIndex(CFStringTokenizer!, CFIndex) -> CFStringTokenizerTokenType](cfstringtokenizergototokenatindex(_:_:).md)
  Finds a token that includes the character at a given index, and set it as the current token.
### Getting Information About the Current Token
- [func CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> CFTypeRef!](cfstringtokenizercopycurrenttokenattribute(_:_:).md)
  Returns a given attribute of the current token.
- [func CFStringTokenizerGetCurrentTokenRange(CFStringTokenizer!) -> CFRange](cfstringtokenizergetcurrenttokenrange(_:).md)
  Returns the range of the current token.
- [func CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>!, CFIndex, CFMutableArray!) -> CFIndex](cfstringtokenizergetcurrentsubtokens(_:_:_:_:).md)
  Retrieves the subtokens or derived subtokens contained in the compound token.
### Identifying a Language
- [func CFStringTokenizerCopyBestStringLanguage(CFString!, CFRange) -> CFString!](cfstringtokenizercopybeststringlanguage(_:_:).md)
  Guesses a language of a given string and returns the guess as a BCP 47 string.
### Getting the CFStringTokenizer Type ID
- [func CFStringTokenizerGetTypeID() -> CFTypeID](cfstringtokenizergettypeid().md)
  Returns the type ID for CFStringTokenizer.
### Constants
- [Tokenization Modifiers](1588024-tokenization-modifiers.md)
  Tokenization options are used with [`CFStringTokenizerCreate(_:_:_:_:_:)`](cfstringtokenizercreate(_:_:_:_:_:).md) to specify how the string should be tokenized
- [struct CFStringTokenizerTokenType](cfstringtokenizertokentype.md)
  Token types returned by [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](cfstringtokenizergototokenatindex(_:_:).md) and [`CFStringTokenizerAdvanceToNextToken(_:)`](cfstringtokenizeradvancetonexttoken(_:).md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [String Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizer)*