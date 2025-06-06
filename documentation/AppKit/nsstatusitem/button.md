# button

**Framework**: AppKit  
**Kind**: property

The button displayed in the status bar.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var button: NSStatusBarButton? { get }
```

#### Discussion

The status item automatically creates this button by default. Use this property to customize the appearance and behavior of the button, such as its [`image`](nsbutton/image.md), [`target`](nscontrol/target.md), [`action`](nscontrol/action.md), [`toolTip`](nsview/tooltip.md), and so on.

## See Also

- [var behavior: NSStatusItem.Behavior](nsstatusitem/behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct.md)
  A set of optional status item behaviors.
- [var menu: NSMenu?](nsstatusitem/menu.md)
  The pull-down menu displayed when the user clicks the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/button)*