# button

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The button displayed in the status bar.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var button: NSStatusBarButton? { get }
```

```objc
@property (strong, readonly, nullable) NSStatusBarButton * button;
```

#### Discussion

The status item automatically creates this button by default. Use this property to customize the appearance and behavior of the button, such as its [`image`](../nsbutton/image.md), [`target`](../nscontrol/target.md), [`action`](../nscontrol/action.md), [`toolTip`](../nsview/tooltip.md), and so on.

## See Also

### Managing the status item’s behavior
- [var behavior: NSStatusItem.Behavior](./behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [NSStatusItem.Behavior](./behavior-swift.struct.md)
  A set of optional status item behaviors.
- [var menu: NSMenu?](./menu.md)
  The pull-down menu displayed when the user clicks the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/button)*