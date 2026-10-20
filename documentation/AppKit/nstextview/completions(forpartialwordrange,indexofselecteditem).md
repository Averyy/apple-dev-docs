# completions(forPartialWordRange:indexOfSelectedItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of potential completions, in the order to be presented, representing possible word completions available from a partial word.

**Availability**:
- macOS

## Declaration

```swift
func completions(forPartialWordRange charRange: NSRange, indexOfSelectedItem index: UnsafeMutablePointer<Int>) -> [String]?
```

```objc
- (NSArray<NSString *> *) completionsForPartialWordRange:(NSRange) charRange indexOfSelectedItem:(NSInteger *) index;
```

#### Return Value

An array of potential completions, in the order to be presented, representing possible word completions available from a partial word at `charRange`. Returning `nil` or a zero-length array suppresses completion.

#### Discussion

May be overridden by subclasses to modify or override the list of possible completions.

This method should call the delegate method [`textView(_:completions:forPartialWordRange:indexOfSelectedItem:)`](../nstextviewdelegate/textview%28_,completions,forpartialwordrange,indexofselecteditem%29.md) if the delegate implements such a method.

## Parameters

- `charRange`: The range of characters of the matched partial word to be completed.
- `index`: On return, optionally set to the completion that should be initially selected. The default is 0, and –1 indicates no selection.

## See Also

### Performing text completion
- [func complete(Any?)](./complete%28_%29.md)
  Invokes completion in a text view.
- [func insertCompletion(String, forPartialWordRange: NSRange, movement: Int, isFinal: Bool)](./insertcompletion%28_,forpartialwordrange,movement,isfinal%29.md)
  Inserts the selected completion into the text at the appropriate location.
- [var rangeForUserCompletion: NSRange](./rangeforusercompletion.md)
  The partial range from the most recent beginning of a word up to the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/completions(forpartialwordrange:indexofselecteditem:))*