# isEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.

**Availability**:
- macOS

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the font conversion system’s user interface items (the Font panel and Font menu items) are enabled; when the value is [`false`](../../Swift/false.md), these items are not enabled.

## See Also

### Related Documentation
- [var isEnabled: Bool](../nsfontpanel/isenabled.md)
  A Boolean that shows whether the receiver’s Set button is enabled.
### Managing the Font Panel and Font Menu
- [func fontPanel(Bool) -> NSFontPanel?](./fontpanel%28_%29.md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func setFontMenu(NSMenu)](./setfontmenu%28_%29.md)
  Records the given menu as the application’s Font menu.
- [func fontMenu(Bool) -> NSMenu?](./fontmenu%28_%29.md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/isenabled)*