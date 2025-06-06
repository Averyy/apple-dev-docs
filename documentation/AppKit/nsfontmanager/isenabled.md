# isEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the font conversion system’s user interface items (the Font panel and Font menu items) are enabled; when the value is [`false`](https://developer.apple.com/documentation/swift/false), these items are not enabled.

## See Also

- [var isEnabled: Bool](nsfontpanel/isenabled.md)
  A Boolean that shows whether the receiver’s Set button is enabled.
- [func fontPanel(Bool) -> NSFontPanel?](nsfontmanager/fontpanel(_:).md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func setFontMenu(NSMenu)](nsfontmanager/setfontmenu(_:).md)
  Records the given menu as the application’s Font menu.
- [func fontMenu(Bool) -> NSMenu?](nsfontmanager/fontmenu(_:).md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/isenabled)*