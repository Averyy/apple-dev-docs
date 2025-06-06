# Tokenizing natural language text

**Framework**: Natural Language

Enumerate the words in a string.

#### Overview

When you work with natural language text, it’s often useful to tokenize the text into individual words. Using [`NLTokenizer`](nltokenizer.md) to enumerate words, rather than simply splitting components by whitespace, ensures correct behavior in multiple scripts and languages. For example, neither Chinese nor Japanese uses spaces to delimit words.

The example and accompanying steps below show how you use [`NLTokenizer`](nltokenizer.md) to enumerate over the words in natural language text.

```swift
let text = """
All human beings are born free and equal in dignity and rights.
They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.
"""

let tokenizer = NLTokenizer(unit: .word)
tokenizer.string = text

tokenizer.enumerateTokens(in: text.startIndex..<text.endIndex) { tokenRange, _ in
    print(text[tokenRange])
    return true
}
```

1. Create an instance of [`NLTokenizer`](nltokenizer.md), specifying [`NLTokenUnit.word`](nltokenunit/word.md) as the unit to tokenize.
2. Set the [`string`](nltokenizer/string.md) property of the tokenizer to the natural language text.
3. Enumerate over the entire range of the string by calling the [`enumerateTokensInRange:usingBlock:`](nltokenizer/enumeratetokensinrange:usingblock:.md) method, specifying the entire range of the string to process.
4. In the enumeration block, take a substring of the original text at `tokenRange` to obtain each word.
5. Run this code to print out each word in text on a new line.

## See Also

- [class NLTokenizer](nltokenizer.md)
  A tokenizer that segments natural language text into semantic units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/tokenizing-natural-language-text)*