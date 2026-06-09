# init(frame:pullsDown:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSPopUpButton` object initialized to the specified dimensions.

**Availability**:
- macOS ?+

## Declaration

```swift
init(frame buttonFrame: NSRect, pullsDown flag: Bool)
```

#### Return Value

An initialized `NSPopUpButton` object, or `nil` if the object could not be initialized.

## Parameters

- `buttonFrame`: The frame rectangle for the button, specified in the parent view’s coordinate system.
- `flag`: [`true`](https://developer.apple.com/documentation/Swift/true) if you want the receiver to display a pull-down menu; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) if you want it to display a pop-up menu.

## See Also

- [init(textCell: String, pullsDown: Bool)](nspopupbuttoncell/init(textcell:pullsdown:).md)
  Returns an `NSPopUpButtonCell` object initialized with the specified title.
- [var pullsDown: Bool](nspopupbutton/pullsdown.md)
  A Boolean value indicating whether the button displays a pull-down or pop-up menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/init(frame:pullsdown:))*