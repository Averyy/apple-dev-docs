# MLWordEmbedding

**Framework**: Create ML  
**Kind**: struct

A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MLWordEmbedding
```

#### Overview

Use an [`MLWordEmbedding`](mlwordembedding.md) to configure and save a word embedding to a file, which you then add to your project in Xcode. Your project uses that word embedding file at runtime to create an [`NLEmbedding`](https://developer.apple.com/documentation/NaturalLanguage/NLEmbedding) instance, which finds similar strings based on the proximity of their vectors.

You configure a word embedding with a dictionary, keyed by strings which make up the  of the word embedding. The value for each string is an array of doubles, which represents a vector. The length of the arrays is arbitrary but all arrays in a word embedding must be the same length. The length of the arrays determine the number of dimensions in the vector space. For example, the following listing creates a word embedding with four dimensions and a vocabulary of two strings.

```swift
let wordEmbedding = try! MLWordEmbedding(dictionary: [
    "Hello"   : [0.0, 1.2, 5.0, 0.0],
    "Goodbye" : [0.0, 1.3, -6.2, 0.1]
])
```

Once you’ve configured an [`MLWordEmbedding`](mlwordembedding.md), save it to an `.mlmodel` file to include in your app.

```swift
try wordEmbedding.write(toFile: "~/Desktop/WordEmbedding.mlmodel")
```

A word embedding file can efficiently store many strings and their vectors.

## Topics

### Creating a word embedding
- [init(dictionary: [String : [Double]], parameters: MLWordEmbedding.ModelParameters) throws](mlwordembedding/init(dictionary:parameters:).md)
  Creates a word embedding.
- [MLWordEmbedding.ModelParameters](mlwordembedding/modelparameters-swift.struct.md)
  The model configuration parameters.
- [let modelParameters: MLWordEmbedding.ModelParameters](mlwordembedding/modelparameters-swift.property.md)
  The model configuration parameters.
### Testing a word embedding
- [func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]](mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:).md)
  Predicts neighbors.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](mlwordembedding/distance(between:and:distancetype:).md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../NaturalLanguage/NLDistanceType.md)
  The means of calculating a distance between two locations in a text embedding.
- [func contains(String) -> Bool](mlwordembedding/contains(_:).md)
  Returns a Boolean value indicating whether the vocabulary contains the given string.
- [func vector(for: String) -> [Double]?](mlwordembedding/vector(for:).md)
  Accesses the vector associated with the given string in the vocabulary.
### Saving a word embedding
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlwordembedding/write(to:metadata:).md)
  Exports the word embedding as a Core ML model file at the specified URL.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlwordembedding/write(tofile:metadata:).md)
  Exports the word embedding as a Core ML model file at the specified file path.
### Describing a word embedding
- [let dimension: Int](mlwordembedding/dimension.md)
  The number of dimensions in the vocabulary embedding space.
- [let vocabularySize: Int](mlwordembedding/vocabularysize.md)
  The number of strings in the vocabulary.
- [var model: MLModel](mlwordembedding/model.md)
  The word embedding contained within a Core ML model file.
- [var description: String](mlwordembedding/description.md)
  A text representation of the word embedding.
- [var debugDescription: String](mlwordembedding/debugdescription.md)
  A text representation of the word embedding that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordembedding/playgrounddescription.md)
  A description of the word embedding shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordembedding/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordembedding/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordembedding/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [Creating a text classifier model](creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [Creating a word tagger model](creating-a-word-tagger-model.md)
  Train a machine learning model to tag individual words in natural language text.
- [struct MLTextClassifier](mltextclassifier.md)
  A model you train to classify natural language text.
- [struct MLWordTagger](mlwordtagger.md)
  A word-tagging model you train to classify natural language text at the word level.
- [struct MLGazetteer](mlgazetteer.md)
  A collection of terms and their labels, which augments a tagger that analyzes natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding)*