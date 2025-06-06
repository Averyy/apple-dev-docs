# dominantLanguage

**Framework**: Natural Language  
**Kind**: property

The dominant language of the string set for the linguistic tagger.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var dominantLanguage: NLLanguage? { get }
```

#### Discussion

If you want to know the dominant language of a string that you’re analyzing with a linguistic tagger (for example, identifying part of speech for each word), specify the [`language`](nltagscheme/language.md) tag scheme in the initializer. After you set the [`string`](nltagger/string.md) property of the linguistic tagger, the dominant language can be determined with the [`dominantLanguage`](nltagger/dominantlanguage.md) property, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
let tagger = NLTagger(tagSchemes: [.language], options: 0)
tagger.string = text
tagger.dominantLanguage // NLLanguage.german
```

In the example, [`german`](nllanguage/german.md) is the dominant language, indicating that the text is in German.

## See Also

- [func setLanguage(NLLanguage, range: Range<String.Index>)](nltagger/setlanguage(_:range:).md)
  Sets the language for a range of text within the tagger’s string.
- [func setOrthography(NSOrthography, range: Range<String.Index>)](nltagger/setorthography(_:range:).md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/dominantlanguage)*