# textView(_:completions:forPartialWordRange:indexOfSelectedItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the actual completions for a partial word.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, completions words: [String], forPartialWordRange charRange: NSRange, indexOfSelectedItem index: UnsafeMutablePointer<Int>?) -> [String]
```

```objc
- (NSArray<NSString *> *) textView:(NSTextView *) textView completions:(NSArray<NSString *> *) words forPartialWordRange:(NSRange) charRange indexOfSelectedItem:(NSInteger *) index;
```

## Return Value

The actual array of completions that will be presented for the partial word at the given range. Returning `nil` or a zero-length array suppresses completion.

## Parameters

- `textView`: The text view sending the message.
- `words`: The proposed array of completions.
- `charRange`: The range of characters to be completed.
- `index`: On return, the index of the initially selected completion. The default is 0, and –1 indicates no selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:completions:forpartialwordrange:indexofselecteditem:))*