# init(textCell:pullsDown:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSPopUpButtonCell` object initialized with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
init(textCell stringValue: String, pullsDown pullDown: Bool)
```

#### Return Value

An initialized `NSPopUpButtonCell` object, or `nil` if the object could not be initialized.

#### Discussion

This menu item is assigned the default pop-up button action that displays the menu. To set the action and target, use the setAction: and setTarget: methods of the item’s corresponding [`NSMenuItem`](nsmenuitem.md) object.

This method is the designated initializer of the class.

## Parameters

- `stringValue`: The title of the first menu. You may specify an empty string if you do not want to add an initial menu item.
- `pullDown`: [`true`](https://developer.apple.com/documentation/swift/true) if you want the receiver to display a pull-down menu; otherwise, [`false`](https://developer.apple.com/documentation/swift/false) if you want it to display a pop-up menu.

## See Also

- [init(frame: NSRect, pullsDown: Bool)](nspopupbutton/init(frame:pullsdown:).md)
  Returns an `NSPopUpButton` object initialized to the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/init(textcell:pullsdown:))*