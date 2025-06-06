# Natural Language

**Framework**: Natural Language  
**Kind**: module

Analyze natural language text and deduce its language-specific metadata.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

#### Overview

The Natural Language framework provides a variety of natural language processing (NLP) functionality with support for many different languages and scripts. Use this framework to segment natural language text into paragraphs, sentences, or words, and tag information about those segments, such as part of speech, lexical class, lemma, script, and language.

![Diagram showing the types of analysis that the Natural Language framework can perform.](https://docs-assets.developer.apple.com/published/991fa70b8c44e03076c487b8b7e7178b/media-3597579%402x.png)

Use this framework to perform tasks like:

- , automatically detecting the language of a piece of text.
- , breaking up a piece of text into linguistic units or tokens.
- , marking up individual words with their part of speech.
- , deducing a word’s stem based on its morphological analysis.
- , identifying tokens as names of people, places, or organizations.

You can also use this framework with Create ML to train and deploy custom natural language models. For more information, see [`Creating a text classifier model`](https://developer.apple.com/documentation/CreateML/creating-a-text-classifier-model) and [`Creating a word tagger model`](creating-a-word-tagger-model.md).

## Topics

### Tokenization
- [Tokenizing natural language text](tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [class NLTokenizer](nltokenizer.md)
  A tokenizer that segments natural language text into semantic units.
### Language identification
- [Identifying the language in text](identifying-the-language-in-text.md)
  Detect the language in a piece of text by using a language recognizer.
- [class NLLanguageRecognizer](nllanguagerecognizer.md)
  The language of a body of text.
- [struct NLLanguage](nllanguage.md)
  The languages that the Natural Language framework supports.
### Linguistic tags
- [Identifying parts of speech](identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying people, places, and organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [class NLTagger](nltagger.md)
  A tagger that analyzes natural language text.
### Text embedding
- [Finding similarities between pieces of text](finding-similarities-between-pieces-of-text.md)
  Calculate the semantic distance between words or sentences.
- [class NLEmbedding](nlembedding.md)
  A map of strings to vectors, which locates neighboring, similar strings.
### Contextual embedding
- [class NLContextualEmbedding](nlcontextualembedding.md)
  A model that computes sequences of embedding vectors for natural language utterances.
- [struct NLContextualEmbeddingKey](nlcontextualembeddingkey.md)
  Contextual embedding keys.
- [struct NLScript](nlscript.md)
  The writing scripts that the Natural Language framework supports.
### Natural language models
- [Creating a text classifier model](../CreateML/creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [Creating a word tagger model](creating-a-word-tagger-model.md)
  Train a machine learning model to tag individual words in natural language text.
- [class NLModel](nlmodel.md)
  A custom model trained to classify or tag natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NaturalLanguage)*