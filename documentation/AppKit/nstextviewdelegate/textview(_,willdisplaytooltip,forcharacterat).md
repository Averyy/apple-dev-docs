# textView(_:willDisplayToolTip:forCharacterAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the actual tooltip to display.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, willDisplayToolTip tooltip: String, forCharacterAt characterIndex: Int) -> String?
```

```objc
- (NSString *) textView:(NSTextView *) textView willDisplayToolTip:(NSString *) tooltip forCharacterAtIndex:(NSUInteger) characterIndex;
```

## Return Value

The actual tooltip to display, or `nil` to suppress display of the tooltip.

## Discussion

The tooltip string is the value of the [`toolTip`](../../Foundation/nsattributedstring/key/tooltip.md) attribute at `characterIndex`.

## Parameters

- `textView`: The text view sending the message.
- `tooltip`: The proposed tooltip to display.
- `characterIndex`: The location in `textView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willdisplaytooltip:forcharacterat:))*