# MSMessagesAppPresentationStyle.compact

**Framework**: Messages  
**Kind**: case  
**Role**: Case

The iMessage App is displayed inside the keyboard area.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case compact
```

```c
MSMessagesAppPresentationStyleCompact
```

## Discussion

When you use the compact presentation style, the extension’s user interface replaces the keyboard. Because the keyboard is not available, adding text fields or text views to your compact layout is not recommended.

If you have a control that requires input from the keyboard (for example, a text field), you must call [`requestPresentationStyle(_:)`](../msmessagesappviewcontroller/requestpresentationstyle%28_%29.md) to expand the extension as soon as the user selects that control. This allows you to display both the extension’s user interface and the keyboard at the same time.

Additionally, do not include horizontally scrolling elements in a compact layout. This includes gesture recognizers for horizontal swipes.

## See Also

### Presentation Styles
- [MSMessagesAppPresentationStyle.expanded](./expanded.md)
  The iMessage App expands to fill most of the screen.
- [MSMessagesAppPresentationStyle.transcript](./transcript.md)
  The iMessage app is displayed in the Messages app’s transcript or input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapppresentationstyle/compact)*