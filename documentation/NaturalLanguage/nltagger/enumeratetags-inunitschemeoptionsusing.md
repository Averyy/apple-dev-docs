# enumerateTags(in:unit:scheme:options:using:)

**Framework**: Natural Language  
**Kind**: method

Enumerates a block over the tagger’s string, given a range, token unit, and tag scheme.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
func enumerateTags(in range: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options = [], using block: (NLTag?, Range<String.Index>) -> Bool)
```

#### Discussion

Use this method to iterate your block over the given range of a string. The method divides up the string with the given [`NLTokenUnit`](nltokenunit.md) and [`NLTagScheme`](nltagscheme.md) and then calls your block. For example, use the [`lexicalClass`](nltagscheme/lexicalclass.md) tag scheme to identify which tokens are parts of speech, types of whitespace, or types of punctuation. Use the [`lemma`](nltagscheme/lemma.md) tag scheme to identify the stem form of each word token, if known.

> ❗ **Important**:  This method enumerates over the ranges of all tokens that intersect the specified range.

## Parameters

- `range`: The range of the string you want the tagger to analyze.
- `unit`: The linguistic unit of scale you’re interested in, such as  ,  ,  , or  .
- `scheme`: The tag scheme the tagger uses to tag the string, such as   or  . This scheme determines which types of   the method passes to your block. For other tag schemes, see  .
- `options`: The set of linguistic tagger options to use, such as  . For all available options, see  .
- `block`: The block this method uses to iterate over the tagger’s   property. The block has the following parameters:

## See Also

- [NLTagger.Options](nltagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.
- [struct NLTag](nltag.md)
  A token type, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/enumeratetags(in:unit:scheme:options:using:))*