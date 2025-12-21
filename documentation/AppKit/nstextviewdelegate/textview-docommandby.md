# textView(_:doCommandBy:)

**Framework**: AppKit  
**Kind**: method

Sent to allow the delegate to perform the command for the text view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, doCommandBy commandSelector: Selector) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) indicates that the delegate handled the command and the text view will not attempt to perform it; [`false`](https://developer.apple.com/documentation/Swift/false) indicates that the delegate did not handle the command the text view will attempt to perform it.

#### Discussion

This method is invoked by `NSTextView`’s `doCommand(by:)` method.

## Parameters

- `textView`: The text view sending the message. This is the first text view in a series shared by a layout manager.
- `commandSelector`: The selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:docommandby:))*