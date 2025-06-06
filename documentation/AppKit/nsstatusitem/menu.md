# menu

**Framework**: AppKit  
**Kind**: property

The pull-down menu displayed when the user clicks the status item.

**Availability**:
- macOS ?+

## Declaration

```swift
var menu: NSMenu? { get set }
```

#### Discussion

When non-`nil`, the status item’s single click action behavior is not used. Setting the value of this property to `nil` removes the menu.

## See Also

- [var behavior: NSStatusItem.Behavior](nsstatusitem/behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct.md)
  A set of optional status item behaviors.
- [var button: NSStatusBarButton?](nsstatusitem/button.md)
  The button displayed in the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/menu)*