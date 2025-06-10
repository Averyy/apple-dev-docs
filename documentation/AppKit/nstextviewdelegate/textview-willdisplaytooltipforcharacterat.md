# textView(_:willDisplayToolTip:forCharacterAt:)

**Framework**: AppKit  
**Kind**: method

Returns the actual tooltip to display.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, willDisplayToolTip tooltip: String, forCharacterAt characterIndex: Int) -> String?
```

#### Return Value

The actual tooltip to display, or `nil` to suppress display of the tooltip.

#### Discussion

The tooltip string is the value of the [`toolTip`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/toolTip) attribute at `characterIndex`.

## Parameters

- `textView`: The text view sending the message.
- `tooltip`: The proposed tooltip to display.
- `characterIndex`: The location in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willdisplaytooltip:forcharacterat:))*