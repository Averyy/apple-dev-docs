# Finding similarities between pieces of text

**Framework**: Natural Language

Calculate the semantic distance between words or sentences.

#### Overview

Finding semantic similarities between words or sentences can help you create a better user experience for your app. For example, you might enhance the experience of searching for specific photos by knowing that the search term “cloud” is related to the word “sky,” and expanding the search query to return more relevant results.

To find similarities between pieces of natural language text, you use text embeddings. An  is a map from strings—words or sentences—into a vector space. Strings that are semantically similar have similar vectors, which means they’re closer together in vector space.

![Diagram of a 3-dimensional coordinate system (X, Y, Z) with six words in the space. Three of the words — food, pizza, and burger — are located near one another along the Y-axis. The other three words — automobile, car, and bus — are located near one another along the X-axis. The clusters of words are separated by a good amount of space because they contain unrelated words.](https://docs-assets.developer.apple.com/published/47e8240baf2ac0b4a5c8d3c3763f7f62/media-3687947%402x.png)

You use embeddings for tasks like:

- Searching for the nearest neighbors to a given term—for example, to expand a search query.
- Calculating the distance between terms, as a measure of semantic similarity.
- Using the vectors as an input layer for a model.

In Natural Language, [`NLEmbedding`](nlembedding.md) represents an embedding, stored in a space- and time-efficient format. [`NLEmbedding`](nlembedding.md) provides pretrained word embeddings for a number of languages, trained on large bodies of general text.

##### Find Similar Words

To calculate the distance between individual words, use a word embedding.

1. Create an instance of [`NLEmbedding`](nlembedding.md) with [`wordEmbedding(for:)`](nlembedding/wordembedding(for:).md), specifying the language for which to generate a word embedding.
2. Call the [`vector(for:)`](nlembedding/vector(for:).md) method of the embedding with a specific input word to see the vector generated for that word.
3. To find the distance between your input word and another word, use `distance(between:and:distanceType:)`.
4. To find the nearest neighbors to your input word, enumerate over the word’s neighbors by calling the [`enumerateNeighborsForString:maximumCount:distanceType:usingBlock:`](nlembedding/enumerateneighborsforstring:maximumcount:distancetype:usingblock:.md) method, specifying the maximum number of nearest neighbors to look at.

```swift
if let embedding = NLEmbedding.wordEmbedding(for: .english) {
    let word = "bicycle"
    
    if let vector = embedding.vector(for: word) {
        print(vector)
    }
    
    let specificDistance = embedding.distance(between: word, and: "motorcycle")
    print(specificDistance.description)
    
    embedding.enumerateNeighbors(for: word, maximumCount: 5) { neighbor, distance in
        print("\(neighbor): \(distance.description)")
        return true
    }
}
```

##### Find Similar Sentences

To calculate the distance between phrases, use a sentence embedding. You might use it to measure similarity between sentences for tasks like text retrieval, or for detecting paraphrases. For example, if a user searches a food-delivery app using the text, “Where is my order?” you could use a sentence embedding to suggest a result from the FAQ with the similar title, “How do I check the status of my order?”

1. Create an instance of [`NLEmbedding`](nlembedding.md) with [`sentenceEmbedding(for:)`](nlembedding/sentenceembedding(for:).md), specifying the language for which to generate a sentence embedding.
2. Call the [`vector(for:)`](nlembedding/vector(for:).md) method of the embedding with a specific input sentence to see the vector generated for that sentence.
3. To find the distance between your input sentence and another sentence, use [`distanceBetweenString:andString:distanceType:`](nlembedding/distancebetweenstring:andstring:distancetype:.md).

```swift
if let sentenceEmbedding = NLEmbedding.sentenceEmbedding(for: .english) {
    let sentence = "This is a sentence."

    if let vector = sentenceEmbedding.vector(for: sentence) {
        print(vector)
    }
    
    let distance = sentenceEmbedding.distance(between: sentence, and: "That is a sentence.")
    print(distance.description)
}
```

Sentence embeddings are dynamic. They don’t have a fixed vocabulary, and they can return results for arbitrary sentences. Nearest-neighbor search therefore doesn’t apply to sentence embeddings.

## See Also

- [class NLEmbedding](nlembedding.md)
  A map of strings to vectors, which locates neighboring, similar strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/finding-similarities-between-pieces-of-text)*