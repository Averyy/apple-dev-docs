# orderFrontSharingServicePicker(_:)

**Framework**: AppKit  
**Kind**: method

Creates and displays a new instance of the sharing service picker.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func orderFrontSharingServicePicker(_ sender: Any?)
```

#### Discussion

Creates a new instance of [`NSSharingServicePicker`](nssharingservicepicker.md) based on the current selection and shows to the screen. The items passed to the [`NSSharingServicePicker`](nssharingservicepicker.md) initializer are determined using the delegate method `textView:willShowSharingServicePicker:forItems:`.

When the current selection is 0 length, the whole document is passed to the method.

## Parameters

- `sender`: The sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/orderfrontsharingservicepicker(_:))*