# behavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The set of allowed behaviors for the status item.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var behavior: NSStatusItem.Behavior { get set }
```

```objc
@property (assign) NSStatusItemBehavior behavior;
```

#### Discussion

By default, this property includes no behavior options. See [`NSStatusItem.Behavior`](./behavior-swift.struct.md) for a list of available behavior options and their effects.

## See Also

### Managing the status item’s behavior
- [NSStatusItem.Behavior](./behavior-swift.struct.md)
  A set of optional status item behaviors.
- [var button: NSStatusBarButton?](./button.md)
  The button displayed in the status bar.
- [var menu: NSMenu?](./menu.md)
  The pull-down menu displayed when the user clicks the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.property)*