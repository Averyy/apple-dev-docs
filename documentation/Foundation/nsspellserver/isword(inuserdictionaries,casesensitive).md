# isWord(inUserDictionaries:caseSensitive:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether a given word is in the user’s list of learned words or the document’s list of words to ignore.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func isWord(inUserDictionaries word: String, caseSensitive flag: Bool) -> Bool
```

```objc
- (BOOL) isWordInUserDictionaries:(NSString *) word caseSensitive:(BOOL) flag;
```

#### Return Value

A Boolean value indicating whether the word is in the user dictionaries. If [`true`](../../Swift/true.md), the word is acceptable to the user.

## Parameters

- `word`: The word to compare with those in the user dictionaries.
- `flag`: Specifies whether the comparison is case sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserver/isword(inuserdictionaries:casesensitive:))*