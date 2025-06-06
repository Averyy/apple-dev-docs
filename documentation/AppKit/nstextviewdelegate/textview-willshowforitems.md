# textView(_:willShow:forItems:)

**Framework**: AppKit  
**Kind**: method

Returns a sharing service picker for the current selection.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, willShow servicePicker: NSSharingServicePicker, forItems items: [Any]) -> NSSharingServicePicker?
```

#### Return Value

An [`NSSharingServicePicker`](nssharingservicepicker.md) instance. The original sharing picker or a new sharing picker instance can be returned.

#### Discussion

Returns a sharing service picker created for items right before shown to the screen when the `orderFrontSharingServicePicker:` method. Return `nil` to remove the Share item from the menu.

The delegate is specified as the delegate for the `NSSharingServicePicker` instance.

## Parameters

- `textView`: The text view.
- `servicePicker`: The service picker.
- `items`: The ranges of the items to share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:willshow:foritems:))*