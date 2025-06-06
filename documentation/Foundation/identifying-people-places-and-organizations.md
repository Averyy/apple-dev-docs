# Identifying People, Places, and Organizations

**Framework**: Foundation

Use a linguistic tagger to perform named entity recognition on a string.

#### Overview

Identifying named entities in natural language text can help make your app more intelligent. For example, a messaging app might look for names of people and places in text in order to display related information like contact information or directions.

The example below shows how to use [`NSLinguisticTagger`](nslinguistictagger.md) to enumerate over natural language text and identify any named person, place, or organization.

```swift
let text = "The American Red Cross was established in Washington, D.C., by Clara Barton."
let tagger = NSLinguisticTagger(tagSchemes: [.nameType], options: 0)
tagger.string = text
let range = NSRange(location:0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace, .joinNames]
let tags: [NSLinguisticTag] = [.personalName, .placeName, .organizationName]
tagger.enumerateTags(in: range, unit: .word, scheme: .nameType, options: options) { tag, tokenRange, stop in
    if let tag = tag, tags.contains(tag) {
        let name = (text as NSString).substring(with: tokenRange)
        print("\(name): \(tag)")
    }
}
```

First, an instance of [`NSLinguisticTagger`](nslinguistictagger.md) is created, specifying [`nameType`](nslinguistictagscheme/nametype.md) as the tag scheme to be used. Next, the [`string`](nslinguistictagger/string.md) property of the linguistic tagger is set to the natural language text. Finally, the linguistic tagger enumerates over the entire range of the string, specifying [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) as the tag unit and [`nameType`](nslinguistictagscheme/nametype.md) as the tag scheme, omitting any punctuation or whitespace, and joining words that are part of a single name into the same token. In the enumeration block, the name type is provided by `tag`, and each word is obtained by taking a substring of the original text at `tokenRange`.

When run, this code prints out each name and its type on a new line, as shown below:

| Name | Type |
| --- | --- |
| The American Red Cross | [`organizationName`](nslinguistictag/organizationname.md) |
| Washington, D.C. | [`placeName`](nslinguistictag/placename.md) |
| Clara Barton | [`personalName`](nslinguistictag/personalname.md) |

## See Also

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [Identifying Parts of Speech](identifying-parts-of-speech.md)
  Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [func enumerateTags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:unit:scheme:options:using:).md)
  Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.
- [func enumerateTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(in:scheme:options:using:).md)
  Enumerates over a given range of the string and calls the specified block for each tag.
- [class func enumerateTags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslinguistictagger/enumeratetags(for:range:unit:scheme:options:orthography:using:).md)
  Enumerates over a given string and calls the specified block for each tag.
- [NSLinguisticTagger.Options](nslinguistictagger/options.md)
  Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/identifying-people-places-and-organizations)*