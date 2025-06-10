# Identifying parts of speech

**Framework**: Natural Language

Classify nouns, verbs, adjectives, and other parts of speech in a string.

#### Overview

Identifying the parts of speech for words in natural language text can help your program understand the meaning of sentences. For example, provided the transcription of a request spoken by the user, you might programmatically determine general intent by looking at only the nouns and verbs.

The example below shows how to use NLTagger to enumerate over natural language text and identify the part of speech for each word.

```swift
let text = "The ripe taste of cheese improves with age."
let tagger = NLTagger(tagSchemes: [.lexicalClass])
tagger.string = text
let options: NLTagger.Options = [.omitPunctuation, .omitWhitespace]
tagger.enumerateTags(in: text.startIndex..<text.endIndex, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange in
    if let tag = tag {
        print("\(text[tokenRange]): \(tag.rawValue)")
    }
    return true
}
```

1. Create an instance of [`NLTagger`](nltagger.md), specifying [`lexicalClass`](nltagscheme/lexicalclass.md) as the tag scheme to be used.
2. Set the string property of the linguistic tagger to the natural language text.
3. Create the options to omit punctuation and whitespace.
4. Enumerate over the entire range of the string, specifying [`word`](https://developer.apple.com/documentation/Foundation/NSLinguisticTag/word) as the tag unit and [`lexicalClass`](nltagscheme/lexicalclass.md) as the tag scheme, and the tagger options.
5. In the enumeration block, take a substring of the original text at `tokenRange` to obtain each word.
6. Run this code to print out each word and its part of speech on a new line.

## See Also

- [Identifying people, places, and organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [class NLTagger](nltagger.md)
  A tagger that analyzes natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/identifying-parts-of-speech)*