# NLTokenUnit.paragraph

**Framework**: Natural Language  
**Kind**: case

An individual paragraph.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case paragraph
```

#### Discussion

Use this linguistic unit to tokenize text into paragraphs, like in the following example:

```swift
let text = "This is a sentence. This is another sentence.\nThis is a second paragraph."

let tokenizer = NLTokenizer(unit: .paragraph)
tokenizer.string = text

let range = text.startIndex..<text.endIndex

let tokenArray = tokenizer.tokens(for: range)
print("Number of tokens: \(tokenArray.count)")

tokenizer.enumerateTokens(in: range) { tokenRange, _ in
    print(text[tokenRange])
    return true
}
```

For more information, see [`Tokenizing natural language text`](tokenizing-natural-language-text.md).

## See Also

- [NLTokenUnit.word](nltokenunit/word.md)
  An individual word.
- [NLTokenUnit.sentence](nltokenunit/sentence.md)
  An individual sentence.
- [NLTokenUnit.document](nltokenunit/document.md)
  The document in its entirety.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltokenunit/paragraph)*