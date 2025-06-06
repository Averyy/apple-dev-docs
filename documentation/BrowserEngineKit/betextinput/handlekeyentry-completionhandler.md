# handleKeyEntry(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Accepts key-entry events from the text system for the text view to process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func handleKeyEntry(_ entry: BEKeyEntry) async -> (BEKeyEntry, Bool)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Overview

Implement this method to receive keyboard events from the operating system. If you handle the `entry` in code, call the completion handler with `true` as the second parameter. Otherwise, call the completion handler with `false` as the second argument, and call the delegate’s [`shouldDeferEventHandlingToSystem(for:context:)`](betextinputdelegate/shoulddefereventhandlingtosystem(for:context:).md) method. In either case, pass the `entry` you received as the first parameter to the completion handler.

The operating system delivers events on a serial queue, so call the completion handler after your view processes an event to allow the operating system to send a subsequent event.

## Parameters

- `entry`: The keyboard event delivered by the operating system.
- `completionHandler`: A block that you call to indicate whether your text view handled the event.

## See Also

- [var isEditable: Bool](betextinput/iseditable.md)
  Reflects the ability to modify text
- [func shiftKeyStateChanged(fromState: BEKeyModifierFlags, toState: BEKeyModifierFlags)](betextinput/shiftkeystatechanged(fromstate:tostate:).md)
  Indicates a transition in shift state
- [func text(in: UITextRange) -> String?](betextinput/text(in:).md)
  Returns the text in the specified range.
- [func offset(from: UITextPosition, to: UITextPosition) -> Int](betextinput/offset(from:to:).md)
  Returns the number of UTF-16 characters between one text position and another text position.
- [func setBaseWritingDirection(NSWritingDirection, for: UITextRange)](betextinput/setbasewritingdirection(_:for:).md)
  Sets the base writing direction for a specified range of text in a document.
- [func delete(in: UITextStorageDirection, to: UITextGranularity)](betextinput/delete(in:to:).md)
  Deletes text by the specified direction and granularity.  Current supported combinations include:


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/handlekeyentry(_:completionhandler:))*