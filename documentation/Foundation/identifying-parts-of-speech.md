# Identifying Parts of Speech

**Framework**: Foundation

Classify nouns, verbs, adjectives, and other parts of speech in a string.

#### Overview

Identifying the parts of speech for words in natural language text can help your program understand the meaning of sentences. For example, given the transcription of a request spoken by the user, you might determine general intent by looking at only the nouns and verbs.

The example below shows how to use [`NSLinguisticTagger`](nslinguistictagger.md) to enumerate over natural language text and identify the part of speech for each word.

```swift
let text = "The ripe taste of cheese improves with age."
let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
tagger.string = text
let range = NSRange(location: 0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
    if let tag = tag {
        let word = (text as NSString).substring(with: tokenRange)
        print("\(word): \(tag)")
    }
}
```

First, an instance of [`NSLinguisticTagger`](nslinguistictagger.md) is created, specifying [`lexicalClass`](nslinguistictagscheme/lexicalclass.md) as the tag scheme to be used. Next, the [`string`](nslinguistictagger/string.md) property of the linguistic tagger is set to the natural language text. Finally, the linguistic tagger enumerates over the entire range of the string, specifying [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) as the tag unit and [`lexicalClass`](nslinguistictagscheme/lexicalclass.md) as the tag scheme, and omitting any punctuation or whitespace. In the enumeration block, the part of speech is provided by `tag`, and each word is obtained by taking a substring of the original text at `tokenRange`.

When run, this code prints out each word and its part of speech on a new line, as shown below:

| Word | Part of speech |
| --- | --- |
| The | [`determiner`](nslinguistictag/determiner.md) |
| ripe | [`adjective`](nslinguistictag/adjective.md) |
| taste | [`noun`](nslinguistictag/noun.md) |
| of | [`preposition`](nslinguistictag/preposition.md) |
| cheese | [`noun`](nslinguistictag/noun.md) |
| improves | [`verb`](nslinguistictag/verb.md) |
| with | [`preposition`](nslinguistictag/preposition.md) |
| age | [`noun`](nslinguistictag/noun.md) |

## See Also

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md)
  Use a linguistic tagger to perform named entity recognition on a string.
- [func enumerateTags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.
- [func enumerateTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:scheme:options:using:).md)
  Enumerates over a given range of the string and calls the specified block for each tag.
- [class func enumerateTags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(for:range:unit:scheme:options:orthography:using:).md)
  Enumerates over a given string and calls the specified block for each tag.
- [NSLinguisticTagger.Options](nslinguistictagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/identifying-parts-of-speech)*