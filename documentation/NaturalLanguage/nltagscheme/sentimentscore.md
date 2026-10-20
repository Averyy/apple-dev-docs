# sentimentScore

**Framework**: Natural Language  
**Kind**: property  
**Role**: Type Property

A scheme that scores text as positive, negative, or neutral based on its sentiment polarity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let sentimentScore: NLTagScheme
```

```c
extern NLTagScheme const NLTagSchemeSentimentScore;
```

#### Discussion

The range of a sentiment score is `[-1.0, 1.0]`. A score of `1.0` is the most positive, a score of `-1.0` is the most negative, and a score of `0.0` is neutral.

```swift
let text = "It's pretty good."

let tagger = NLTagger(tagSchemes: [.tokenType, .sentimentScore])
tagger.string = text

tagger.enumerateTags(in: text.startIndex..<text.endIndex, unit: .paragraph, 
                     scheme: .sentimentScore, options: []) { sentiment, _ in
    
    if let sentimentScore = sentiment {
        print(sentimentScore.rawValue)
    }
    
    return true
}
```

## See Also

### Schemes
- [static let tokenType: NLTagScheme](./tokentype.md)
  A scheme that classifies tokens according to their broad type: word, punctuation, or whitespace.
- [static let lexicalClass: NLTagScheme](./lexicalclass.md)
  A scheme that classifies tokens according to class: part of speech, type of punctuation, or whitespace.
- [static let nameType: NLTagScheme](./nametype.md)
  A scheme that classifies tokens according to whether they are part of a named entity.
- [static let nameTypeOrLexicalClass: NLTagScheme](./nametypeorlexicalclass.md)
  A scheme that classifies tokens corresponding to names according to [`nameType`](./nametype.md), and classifies all other tokens according to [`lexicalClass`](./lexicalclass.md).
- [static let lemma: NLTagScheme](./lemma.md)
  A scheme that supplies a stem form of a word token, if known.
- [static let language: NLTagScheme](./language.md)
  A scheme that supplies the language for a token, if it can determine one.
- [static let script: NLTagScheme](./script.md)
  A scheme that supplies the script for a token, if it can determine one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagscheme/sentimentscore)*