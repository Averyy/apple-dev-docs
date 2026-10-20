# menu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The pull-down menu displayed when the user clicks the status item.

**Availability**:
- macOS

## Declaration

```swift
var menu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * menu;
```

#### Discussion

When non-`nil`, the status item’s single click action behavior is not used. Setting the value of this property to `nil` removes the menu.

## See Also

### Managing the status item’s behavior
- [var behavior: NSStatusItem.Behavior](./behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [NSStatusItem.Behavior](./behavior-swift.struct.md)
  A set of optional status item behaviors.
- [var button: NSStatusBarButton?](./button.md)
  The button displayed in the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/menu)*