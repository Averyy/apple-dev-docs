# Tokenizing Natural Language Text

**Framework**: Foundation

Enumerate the words in a string.

#### Overview

When you work with natural language text, it’s often useful to tokenize the text into individual words. Using [`NSLinguisticTagger`](nslinguistictagger.md) to enumerate words, rather than simply splitting components by whitespace, ensures correct behavior in multiple scripts and languages. For example, neither Chinese nor Japanese uses spaces to delimit words.

The example and accompanying steps below show how you use [`NSLinguisticTagger`](nslinguistictagger.md) to enumerate over the words in natural language text.

```swift
let text = """
All human beings are born free and equal in dignity and rights.
They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.
"""

let tagger = NSLinguisticTagger(tagSchemes: [.tokenType], options: 0)
tagger.string = text

let range = NSRange(location: 0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
tagger.enumerateTags(in: range, unit: .word, scheme: .tokenType, options: options) { _, tokenRange, _ in
    let word = (text as NSString).substring(with: tokenRange)
    print(word)
}
```

1. Create an instance of [`NSLinguisticTagger`](nslinguistictagger.md), specifying [`tokenType`](nslinguistictagscheme/tokentype.md) as the tag scheme to be used.
2. Set the [`string`](nslinguistictagger/string.md) property of the linguistic tagger to the natural language text.
3. Enumerate over the entire range of the string by calling the [`enumerateTags(in:unit:scheme:options:using:)`](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md) method, specifying [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) as the tag unit and [`tokenType`](nslinguistictagscheme/tokentype.md) as the tag scheme to enumerate, and omitting any punctuation or whitespace.
4. In the enumeration block, take a substring of the original text at `tokenRange` to obtain each word.
5. Run this code to print out each word in `text` on a new line.

## See Also

- [Identifying Parts of Speech](identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [init(tagSchemes: [NSLinguisticTagScheme], options: Int)](nslinguistictagger/init(tagschemes:options:).md)
  Creates a linguistic tagger instance using the specified tag schemes and options.
- [var string: String?](nslinguistictagger/string.md)
  The string being analyzed by the linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/tokenizing-natural-language-text)*