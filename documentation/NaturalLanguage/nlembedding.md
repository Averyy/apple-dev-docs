# NLEmbedding

**Framework**: Natural Language  
**Kind**: class

A map of strings to vectors, which locates neighboring, similar strings.

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
class NLEmbedding
```

## Mentions

- [Finding similarities between pieces of text](finding-similarities-between-pieces-of-text.md)

#### Overview

Use an [`NLEmbedding`](nlembedding.md) to find similar strings based on the proximity of their vectors. The  is the entire set of strings in an embedding. Each string in the vocabulary has a vector, which is an array of doubles, and each double corresponds to a dimension in the embedding. An [`NLEmbedding`](nlembedding.md) uses these vectors to determine the distance between two strings, or to find the nearest neighbors of a string in the vocabulary. The higher the similarity of any two strings, the smaller the distance is between them.

[`Natural Language`](NaturalLanguage.md) provides built-in word embeddings that you can retrieve by using the [`wordEmbedding(for:)`](nlembedding/wordembedding(for:).md) method. You can also compile your own custom embedding into an efficient, searchable, on-disk representation. Typically, you compile an embedding by using Create ML’s [`MLWordEmbedding`](https://developer.apple.com/documentation/CreateML/MLWordEmbedding) and save it as a file for your Xcode project at development time. Alternatively, you can compile an embedding at runtime by using Natural Language’s [`writeEmbeddingForDictionary:language:revision:toURL:error:`](nlembedding/writeembeddingfordictionary:language:revision:tourl:error:.md) method.

Your custom embedding can use any kind of string that’s useful to your app, such as phrases, brand names, serial numbers, and so on. For example, you could make an embedding of movie titles. Each movie title could have a vector that places similar movies close together in the embedding.

## Topics

### Creating a word embedding
- [class func wordEmbedding(for: NLLanguage) -> NLEmbedding?](nlembedding/wordembedding(for:).md)
  Retrieves a word embedding for a given language.
- [class func wordEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](nlembedding/wordembedding(for:revision:).md)
  Retrieves a word embedding for a given language and revision.
- [convenience init(contentsOf: URL) throws](nlembedding/init(contentsof:).md)
  Creates a word embedding from a model file.
### Creating a sentence embedding
- [class func sentenceEmbedding(for: NLLanguage) -> NLEmbedding?](nlembedding/sentenceembedding(for:).md)
  Retrieves a sentence embedding for a given language.
- [class func sentenceEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](nlembedding/sentenceembedding(for:revision:).md)
  Retrieves a sentence embedding for a given language and revision.
### Finding strings and their distances in an embedding
- [func neighbors(for: String, maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](nlembedding/neighbors(for:maximumcount:distancetype:)-8f1jc.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [func neighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](nlembedding/neighbors(for:maximumcount:distancetype:)-8lp4z.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [func enumerateNeighbors(for: String, maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](nlembedding/enumerateneighbors(for:maximumcount:distancetype:using:)-72jda.md)
  Passes the nearest strings of a string in the vocabulary to a closure.
- [func enumerateNeighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](nlembedding/enumerateneighbors(for:maximumcount:distancetype:using:)-6dy4x.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> NLDistance](nlembedding/distance(between:and:distancetype:).md)
  Calculates the distance between two strings in the vocabulary space.
- [typealias NLDistance](nldistance.md)
  The distance between two strings in a text embedding.
### Inspecting the vocabulary of an embedding
- [var dimension: Int](nlembedding/dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](nlembedding/vocabularysize.md)
  The number of words in the vocabulary.
- [var language: NLLanguage?](nlembedding/language.md)
  The language of the text in the word embedding.
- [func contains(String) -> Bool](nlembedding/contains(_:).md)
  Requests a Boolean value that indicates whether the term is in the vocabulary.
- [func vector(for: String) -> [Double]?](nlembedding/vector(for:).md)
  Requests the vector for the given term.
- [var revision: Int](nlembedding/revision.md)
  The revision of the word embedding.
### Saving an embedding
- [class func write([String : [Double]], language: NLLanguage?, revision: Int, to: URL) throws](nlembedding/write(_:language:revision:to:).md)
  Exports the word embedding contained within a Core ML model file at the given URL.
### Checking for Natural Language support
- [class func currentRevision(for: NLLanguage) -> Int](nlembedding/currentrevision(for:).md)
  Retrieves the current version of a word embedding for the given language.
- [class func supportedRevisions(for: NLLanguage) -> IndexSet](nlembedding/supportedrevisions(for:).md)
  Retrieves all version numbers of a word embedding for the given language.
- [class func currentSentenceEmbeddingRevision(for: NLLanguage) -> Int](nlembedding/currentsentenceembeddingrevision(for:).md)
  Retrieves the current version of a sentence embedding for the given language.
- [class func supportedSentenceEmbeddingRevisions(for: NLLanguage) -> IndexSet](nlembedding/supportedsentenceembeddingrevisions(for:).md)
  Retrieves all version numbers of a sentence embedding for the given language.

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

- [Finding similarities between pieces of text](finding-similarities-between-pieces-of-text.md)
  Calculate the semantic distance between words or sentences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding)*