# NLEmbedding

**Framework**: Natural Language  
**Kind**: class  
**Role**: Class

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

```objc
@interface NLEmbedding : NSObject
```

## Mentions

- [Finding similarities between pieces of text](./finding-similarities-between-pieces-of-text.md)

## Overview

Use an [`NLEmbedding`](./nlembedding.md) to find similar strings based on the proximity of their vectors.

The *vocabulary* is the entire set of strings in an embedding. Each string in the vocabulary has a vector, which is an array of doubles, and each double corresponds to a dimension in the embedding. An [`NLEmbedding`](./nlembedding.md) uses these vectors to determine the distance between two strings, or to find the nearest neighbors of a string in the vocabulary. The higher the similarity of any two strings, the smaller the distance is between them.

[Natural Language](./NaturalLanguage.md) provides built-in word embeddings that you can retrieve by using the [`wordEmbedding(for:)`](./nlembedding/wordembedding%28for%29.md) method. You can also compile your own custom embedding into an efficient, searchable, on-disk representation. Typically, you compile an embedding by using Create ML’s [`MLWordEmbedding`](../CreateML/mlwordembedding.md) and save it as a file for your Xcode project at development time. Alternatively, you can compile an embedding at runtime by using Natural Language’s [`writeEmbeddingForDictionary:language:revision:toURL:error:`](./nlembedding/writeembeddingfordictionary_language_revision_tourl_error_.md) method.

Your custom embedding can use any kind of string that’s useful to your app, such as phrases, brand names, serial numbers, and so on. For example, you could make an embedding of movie titles. Each movie title could have a vector that places similar movies close together in the embedding.

> ❗ **Important**: A single [`NLEmbedding`](./nlembedding.md) instance isn’t safe for concurrent use. Although its query methods, like [`vector(for:)`](./nlembedding/vector%28for%29.md), look like read-only lookups, calling them on one instance from multiple threads or tasks at the same time can crash your app. Serialize access to a shared instance, or give each thread or task its own instance.

## Topics

### Creating a word embedding
- [class func wordEmbedding(for: NLLanguage) -> NLEmbedding?](./nlembedding/wordembedding%28for%29.md)
  Retrieves a word embedding for a given language.
- [class func wordEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](./nlembedding/wordembedding%28for,revision%29.md)
  Retrieves a word embedding for a given language and revision.
- [convenience init(contentsOf: URL) throws](./nlembedding/init%28contentsof%29.md)
  Creates a word embedding from a model file.
### Creating a sentence embedding
- [class func sentenceEmbedding(for: NLLanguage) -> NLEmbedding?](./nlembedding/sentenceembedding%28for%29.md)
  Retrieves a sentence embedding for a given language.
- [class func sentenceEmbedding(for: NLLanguage, revision: Int) -> NLEmbedding?](./nlembedding/sentenceembedding%28for,revision%29.md)
  Retrieves a sentence embedding for a given language and revision.
### Finding strings and their distances in an embedding
- [func neighbors(for: String, maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](./nlembedding/neighbors%28for,maximumcount,distancetype%29-8f1jc.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [func neighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](./nlembedding/neighbors%28for,maximumcount,distancetype%29-8lp4z.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [func enumerateNeighbors(for: String, maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](./nlembedding/enumerateneighbors%28for,maximumcount,distancetype,using%29-72jda.md)
  Passes the nearest strings of a string in the vocabulary to a closure.
- [func enumerateNeighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](./nlembedding/enumerateneighbors%28for,maximumcount,distancetype,using%29-6dy4x.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> NLDistance](./nlembedding/distance%28between,and,distancetype%29.md)
  Calculates the distance between two strings in the vocabulary space.
- [typealias NLDistance](./nldistance.md)
  The distance between two strings in a text embedding.
- [- neighborsForString:maximumCount:distanceType:](./nlembedding/neighborsforstring_maximumcount_distancetype_.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [- neighborsForString:maximumCount:maximumDistance:distanceType:](./nlembedding/neighborsforstring_maximumcount_maximumdistance_distancetype_.md)
  Retrieves a limited number of strings, within a radius of a string, in the vocabulary.
- [- neighborsForVector:maximumCount:distanceType:](./nlembedding/neighborsforvector_maximumcount_distancetype_.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [- neighborsForVector:maximumCount:maximumDistance:distanceType:](./nlembedding/neighborsforvector_maximumcount_maximumdistance_distancetype_.md)
  Retrieves a limited number of strings within a radius of a location in the vocabulary space.
- [- enumerateNeighborsForString:maximumCount:distanceType:usingBlock:](./nlembedding/enumerateneighborsforstring_maximumcount_distancetype_usingblock_.md)
  Passes the nearest strings of a string in the vocabulary to a block.
- [- enumerateNeighborsForString:maximumCount:maximumDistance:distanceType:usingBlock:](./nlembedding/enumerateneighborsforstring_maximumcount_maximumdistance_distancetype_usingblock_.md)
  Passes the nearest strings, within a radius of a string in the vocabulary, to a block.
- [- enumerateNeighborsForVector:maximumCount:distanceType:usingBlock:](./nlembedding/enumerateneighborsforvector_maximumcount_distancetype_usingblock_.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [- enumerateNeighborsForVector:maximumCount:maximumDistance:distanceType:usingBlock:](./nlembedding/enumerateneighborsforvector_maximumcount_maximumdistance_distancetype_usingblock_.md)
  Passes the nearest strings, within a radius of a location in the vocabulary space, to a block.
- [- distanceBetweenString:andString:distanceType:](./nlembedding/distancebetweenstring_andstring_distancetype_.md)
  Calculates the distance between two strings in the vocabulary space.
### Inspecting the vocabulary of an embedding
- [var dimension: Int](./nlembedding/dimension.md)
  The number of dimensions in the vocabulary’s vector space.
- [var vocabularySize: Int](./nlembedding/vocabularysize.md)
  The number of words in the vocabulary.
- [var language: NLLanguage?](./nlembedding/language.md)
  The language of the text in the word embedding.
- [func contains(String) -> Bool](./nlembedding/contains%28_%29.md)
  Requests a Boolean value that indicates whether the term is in the vocabulary.
- [func vector(for: String) -> [Double]?](./nlembedding/vector%28for%29.md)
  Requests the vector for the given term.
- [var revision: Int](./nlembedding/revision.md)
  The revision of the word embedding.
- [- vectorForString:](./nlembedding/vectorforstring_.md)
  Requests the vector for the given term.
- [- getVector:forString:](./nlembedding/getvector_forstring_.md)
  Copies a vector into the given a pointer to a float array.
### Saving an embedding
- [class func write([String : [Double]], language: NLLanguage?, revision: Int, to: URL) throws](./nlembedding/write%28_,language,revision,to%29.md)
  Exports the word embedding contained within a Core ML model file at the given URL.
- [+ writeEmbeddingForDictionary:language:revision:toURL:error:](./nlembedding/writeembeddingfordictionary_language_revision_tourl_error_.md)
  Exports the word embedding contained within a Core ML model file at the given URL.
### Checking for Natural Language support
- [class func currentRevision(for: NLLanguage) -> Int](./nlembedding/currentrevision%28for%29.md)
  Retrieves the current version of a word embedding for the given language.
- [class func supportedRevisions(for: NLLanguage) -> IndexSet](./nlembedding/supportedrevisions%28for%29.md)
  Retrieves all version numbers of a word embedding for the given language.
- [class func currentSentenceEmbeddingRevision(for: NLLanguage) -> Int](./nlembedding/currentsentenceembeddingrevision%28for%29.md)
  Retrieves the current version of a sentence embedding for the given language.
- [class func supportedSentenceEmbeddingRevisions(for: NLLanguage) -> IndexSet](./nlembedding/supportedsentenceembeddingrevisions%28for%29.md)
  Retrieves all version numbers of a sentence embedding for the given language.
### Initializers
- [convenience init(contentsOfURL: URL) throws](./nlembedding/init%28contentsofurl%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text embedding
- [Finding similarities between pieces of text](./finding-similarities-between-pieces-of-text.md)
  Calculate the semantic distance between words or sentences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding)*