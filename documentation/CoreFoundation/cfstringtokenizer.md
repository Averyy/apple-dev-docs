# CFStringTokenizer

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

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
class CFStringTokenizer
```

```c
typedef struct __CFStringTokenizer * CFStringTokenizerRef;
```

## Overview

CFStringTokenizer allows you to tokenize strings into words, sentences or paragraphs in a language-neutral way. It supports languages such as Japanese and Chinese that do not delimit words by spaces, as well as de-compounding German compounds. You can obtain Latin transcription for tokens. It also provides language identification API.

You can use a CFStringTokenizer to break a string into tokens (sub-strings) on the basis of words, sentences, or paragraphs. When you create a tokenizer, you can supply options to further modify the tokenization—see [Tokenization Modifiers](./api-1588024-tokenization-modifiers.md).

In addition, with CFStringTokenizer:

- You can de-compound German compounds
- You can identify the language used in a string (using [`CFStringTokenizerCopyBestStringLanguage(_:_:)`](./cfstringtokenizercopybeststringlanguage%28_,_%29.md))
- You can obtain Latin transcription for tokens

To find a token that includes the character specified by character index and set it as the current token, you call [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](./cfstringtokenizergototokenatindex%28_,_%29.md). To advance to the next token and set it as the current token, you call [`CFStringTokenizerAdvanceToNextToken(_:)`](./cfstringtokenizeradvancetonexttoken%28_%29.md). To get the range of current token, you call [`CFStringTokenizerGetCurrentTokenRange(_:)`](./cfstringtokenizergetcurrenttokenrange%28_%29.md). You can use         [`CFStringTokenizerCopyCurrentTokenAttribute(_:_:)`](./cfstringtokenizercopycurrenttokenattribute%28_,_%29.md) to get the attribute of the current token. If the current token is a compound, you can call [`CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)`](./cfstringtokenizergetcurrentsubtokens%28_,_,_,_%29.md) to retrieve the subtokens or derived subtokens contained in the compound token. To guess the language of a string, you call [`CFStringTokenizerCopyBestStringLanguage(_:_:)`](./cfstringtokenizercopybeststringlanguage%28_,_%29.md).

## Topics

### Creating a Tokenizer
- [func CFStringTokenizerCreate(CFAllocator!, CFString!, CFRange, CFOptionFlags, CFLocale!) -> CFStringTokenizer!](./cfstringtokenizercreate%28_,_,_,_,_%29.md)
  Returns a tokenizer for a given string.
### Setting the String
- [func CFStringTokenizerSetString(CFStringTokenizer!, CFString!, CFRange)](./cfstringtokenizersetstring%28_,_,_%29.md)
  Sets the string for a tokenizer.
### Changing the Location
- [func CFStringTokenizerAdvanceToNextToken(CFStringTokenizer!) -> CFStringTokenizerTokenType](./cfstringtokenizeradvancetonexttoken%28_%29.md)
  Advances the tokenizer to the next token and sets that as the current token.
- [func CFStringTokenizerGoToTokenAtIndex(CFStringTokenizer!, CFIndex) -> CFStringTokenizerTokenType](./cfstringtokenizergototokenatindex%28_,_%29.md)
  Finds a token that includes the character at a given index, and set it as the current token.
### Getting Information About the Current Token
- [func CFStringTokenizerCopyCurrentTokenAttribute(CFStringTokenizer!, CFOptionFlags) -> CFTypeRef!](./cfstringtokenizercopycurrenttokenattribute%28_,_%29.md)
  Returns a given attribute of the current token.
- [func CFStringTokenizerGetCurrentTokenRange(CFStringTokenizer!) -> CFRange](./cfstringtokenizergetcurrenttokenrange%28_%29.md)
  Returns the range of the current token.
- [func CFStringTokenizerGetCurrentSubTokens(CFStringTokenizer!, UnsafeMutablePointer<CFRange>!, CFIndex, CFMutableArray!) -> CFIndex](./cfstringtokenizergetcurrentsubtokens%28_,_,_,_%29.md)
  Retrieves the subtokens or derived subtokens contained in the compound token.
### Identifying a Language
- [func CFStringTokenizerCopyBestStringLanguage(CFString!, CFRange) -> CFString!](./cfstringtokenizercopybeststringlanguage%28_,_%29.md)
  Guesses a language of a given string and returns the guess as a BCP 47 string.
### Getting the CFStringTokenizer Type ID
- [func CFStringTokenizerGetTypeID() -> CFTypeID](./cfstringtokenizergettypeid%28%29.md)
  Returns the type ID for CFStringTokenizer.
### Constants
- [Tokenization Modifiers](./api-1588024-tokenization-modifiers.md)
  Tokenization options are used with [`CFStringTokenizerCreate(_:_:_:_:_:)`](./cfstringtokenizercreate%28_,_,_,_,_%29.md) to specify how the string should be tokenized
- [struct CFStringTokenizerTokenType](./cfstringtokenizertokentype.md)
  Token types returned by [`CFStringTokenizerGoToTokenAtIndex(_:_:)`](./cfstringtokenizergototokenatindex%28_,_%29.md) and [`CFStringTokenizerAdvanceToNextToken(_:)`](./cfstringtokenizeradvancetonexttoken%28_%29.md).

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizer)*