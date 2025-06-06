# init(frame:pullsDown:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSPopUpButton` object initialized to the specified dimensions.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(frame buttonFrame: NSRect, pullsDown flag: Bool)
```

#### Return Value

An initialized `NSPopUpButton` object, or `nil` if the object could not be initialized.

## Parameters

- `buttonFrame`: The frame rectangle for the button, specified in the parent view’s coordinate system.
- `flag`:   if you want the receiver to display a pull-down menu; otherwise,   if you want it to display a pop-up menu.

## See Also

- [Application Menu and Pop-up List Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/MenuList.html#//apple_ref/doc/uid/10000032i)
- [var pullsDown: Bool](nspopupbutton/pullsdown.md)
  A Boolean value indicating whether the button displays a pull-down or pop-up menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/init(frame:pullsdown:))*