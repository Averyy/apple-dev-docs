# insertCompletion(_:forPartialWordRange:movement:isFinal:)

**Framework**: AppKit  
**Kind**: method

Inserts the selected completion into the text at the appropriate location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertCompletion(_ word: String, forPartialWordRange charRange: NSRange, movement: Int, isFinal flag: Bool)
```

#### Discussion

This method has two effects, text substitution and changing of the selection:

- It replaces the text between `charRange.start` and the current insertion point with `word`.
- If `flag` is [`false`](https://developer.apple.com/documentation/Swift/false) it changes the selection to be the last  characters of `word` where  is equal to `[word length]` minus `charRange.length`, that is, the potential completion.
- If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true) it makes the selection empty and puts the insertion point just after `word`.

## Parameters

- `word`: The text to insert, including the matched partial word and its potential completion.
- `charRange`: The range of characters of the matched partial word to be completed.
- `movement`: The direction of movement. For possible values see the   Constants section. This value allows subclasses to distinguish between canceling completion and selection by arrow keys, by return, by tab, or by other means such as clicking.
- `flag`:   while the user navigates through the potential text completions,   when a completion is definitively selected or cancelled and the original value is reinserted.

## See Also

- [func complete(Any?)](nstextview/complete(_:).md)
  Invokes completion in a text view.
- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](nstextview/completions(forpartialwordrange:indexofselecteditem:).md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [var rangeForUserCompletion: NSRange](nstextview/rangeforusercompletion.md)
  The partial range from the most recent beginning of a word up to the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/insertcompletion(_:forpartialwordrange:movement:isfinal:))*