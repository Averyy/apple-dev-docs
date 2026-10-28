# insertCompletion(_:forPartialWordRange:movement:isFinal:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the selected completion into the text at the appropriate location.

**Availability**:
- macOS

## Declaration

```swift
func insertCompletion(_ word: String, forPartialWordRange charRange: NSRange, movement: Int, isFinal flag: Bool)
```

```objc
- (void) insertCompletion:(NSString *) word forPartialWordRange:(NSRange) charRange movement:(NSInteger) movement isFinal:(BOOL) flag;
```

## Discussion

This method has two effects, text substitution and changing of the selection:

- It replaces the text between `charRange.start` and the current insertion point with `word`.
- If `flag` is [`false`](../../Swift/false.md) it changes the selection to be the last *n* characters of `word` where *n* is equal to `[word length]` minus `charRange.length`, that is, the potential completion.
- If `flag` is [`true`](../../Swift/true.md) it makes the selection empty and puts the insertion point just after `word`.

## Parameters

- `word`: The text to insert, including the matched partial word and its potential completion.
- `charRange`: The range of characters of the matched partial word to be completed.
- `movement`: The direction of movement. For possible values see the [`NSText`](../nstext.md) Constants section. This value allows subclasses to distinguish between canceling completion and selection by arrow keys, by return, by tab, or by other means such as clicking.
- `flag`: [`false`](../../Swift/false.md) while the user navigates through the potential text completions, [`true`](../../Swift/true.md) when a completion is definitively selected or cancelled and the original value is reinserted.

## See Also

### Performing text completion
- [func complete(Any?)](./complete%28_%29.md)
  Invokes completion in a text view.
- [func completions(forPartialWordRange: NSRange, indexOfSelectedItem: UnsafeMutablePointer<Int>) -> [String]?](./completions%28forpartialwordrange,indexofselecteditem%29.md)
  Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.
- [var rangeForUserCompletion: NSRange](./rangeforusercompletion.md)
  The partial range from the most recent beginning of a word up to the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/insertcompletion(_:forpartialwordrange:movement:isfinal:))*