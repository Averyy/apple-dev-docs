# init(textCell:pullsDown:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSPopUpButtonCell` object initialized with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(textCell stringValue: String, pullsDown pullDown: Bool)
```

#### Return Value

An initialized `NSPopUpButtonCell` object, or `nil` if the object could not be initialized.

#### Discussion

This menu item is assigned the default pop-up button action that displays the menu. To set the action and target, use the setAction: and setTarget: methods of the item’s corresponding [`NSMenuItem`](nsmenuitem.md) object.

This method is the designated initializer of the class.

## Parameters

- `stringValue`: The title of the first menu. You may specify an empty string if you do not want to add an initial menu item.
- `pullDown`:   if you want the receiver to display a pull-down menu; otherwise,   if you want it to display a pop-up menu.

## See Also

- [Application Menu and Pop-up List Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/MenuList.html#//apple_ref/doc/uid/10000032i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/init(textcell:pullsdown:))*