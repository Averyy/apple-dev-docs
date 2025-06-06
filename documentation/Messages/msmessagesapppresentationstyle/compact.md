# MSMessagesAppPresentationStyle.compact

**Framework**: Messages  
**Kind**: case

The iMessage App is displayed inside the keyboard area.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case compact
```

#### Discussion

When you use the compact presentation style, the extension’s user interface replaces the keyboard. Because the keyboard is not available, adding text fields or text views to your compact layout is not recommended.

If you have a control that requires input from the keyboard (for example, a text field), you must call [`requestPresentationStyle(_:)`](msmessagesappviewcontroller/requestpresentationstyle(_:).md) to expand the extension as soon as the user selects that control. This allows you to display both the extension’s user interface and the keyboard at the same time.

Additionally, do not include horizontally scrolling elements in a compact layout. This includes gesture recognizers for horizontal swipes.

## See Also

- [MSMessagesAppPresentationStyle.expanded](msmessagesapppresentationstyle/expanded.md)
  The iMessage App expands to fill most of the screen.
- [MSMessagesAppPresentationStyle.transcript](msmessagesapppresentationstyle/transcript.md)
  The iMessage app is displayed in the Messages app’s transcript or input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapppresentationstyle/compact)*