# NLContextualEmbedding

**Framework**: Natural Language  
**Kind**: class

A model that computes sequences of embedding vectors for natural language utterances.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class NLContextualEmbedding
```

#### Overview

Starting in iOS 17 and macOS 14, the framework supports 27 languages across three models:

- Latin — including Croatian, Czech, Danish, Dutch, English, Finnish, French, German, Hungarian, Indonesian, Italian, Norwegian, Polish, Portuguese, Romanian, Slovak, Swedish, Spanish, Turkish, and Vietnamese
- Cyrillic — including Bulgarian, Kazakh, Russian, and Ukrainian
- Chinese, Japanese, and Korean

In iOS 18 and macOS 15, the framework expands language support to include three additional models:

- Arabic
- Thai
- Indic — including Hindi, Marathi, Bangla, Urdu, Punjabi, Gujarati, Tamil, Telugu, Kannada, and Malayalam

## Topics

### Creating a contextual embedding
- [convenience init?(modelIdentifier: String)](nlcontextualembedding/init(modelidentifier:).md)
  Creates a contextual embedding from a model identifier.
- [init?(language: NLLanguage)](nlcontextualembedding/init(language:).md)
  Creates a contextual embedding from a language.
- [init?(script: NLScript)](nlcontextualembedding/init(script:).md)
  Creates a contextual embedding from a script.
### Inspecting the contextual embedding
- [var dimension: Int](nlcontextualembedding/dimension.md)
  The number of dimensions in the script’s vector space.
- [var hasAvailableAssets: Bool](nlcontextualembedding/hasavailableassets.md)
  A Boolean value that indicates whether assets are available to load.
- [var languages: [NLLanguage]](nlcontextualembedding/languages.md)
  The languages of the text in the contextual embedding.
- [var maximumSequenceLength: Int](nlcontextualembedding/maximumsequencelength.md)
  The maximum number of embedding vectors the model generates, in sequence.
- [var modelIdentifier: String](nlcontextualembedding/modelidentifier.md)
  The model identifier.
- [var revision: Int](nlcontextualembedding/revision.md)
  The revision of the contextual embedding.
- [var scripts: [NLScript]](nlcontextualembedding/scripts.md)
  The scripts of the text in the contextual embedding.
### Requesting assets
- [func requestAssets(completionHandler: (NLContextualEmbedding.AssetsResult, (any Error)?) -> Void)](nlcontextualembedding/requestassets(completionhandler:).md)
  Requests assets for an embedding, if available.
- [NLContextualEmbedding.AssetsResult](nlcontextualembedding/assetsresult.md)
  The status of an asset request.
### Loading and unloading assets
- [func load() throws](nlcontextualembedding/load.md)
  Loads the embedding model.
- [func unload()](nlcontextualembedding/unload.md)
  Unloads the embedding model.
### Applying an embedding
- [func embeddingResult(for: String, language: NLLanguage?) throws -> NLContextualEmbeddingResult](nlcontextualembedding/embeddingresult(for:language:).md)
  Applies an embedding to a string and obtains the resulting embedding vectors.
- [class NLContextualEmbeddingResult](nlcontextualembeddingresult.md)
  An object that represents the embedding vector result from applying a contextual embedding to a string.
### Type Methods
- [class func contextualEmbeddings(forValues: [NLContextualEmbeddingKey : Any]) -> [NLContextualEmbedding]](nlcontextualembedding/contextualembeddings(forvalues:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct NLContextualEmbeddingKey](nlcontextualembeddingkey.md)
  Contextual embedding keys.
- [struct NLScript](nlscript.md)
  The writing scripts that the Natural Language framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding)*