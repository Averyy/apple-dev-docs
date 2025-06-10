# NSStatusItem.Behavior

**Framework**: AppKit  
**Kind**: struct

A set of optional status item behaviors.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct Behavior
```

## Topics

### Behaviors
- [static var removalAllowed: NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct/removalallowed.md)
  A status item that allows interactive removal.
- [static var terminationOnRemoval: NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct/terminationonremoval.md)
  A status item that quits the application upon removal.
### Initializers
- [init(rawValue: UInt)](nsstatusitem/behavior-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var behavior: NSStatusItem.Behavior](nsstatusitem/behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [var button: NSStatusBarButton?](nsstatusitem/button.md)
  The button displayed in the status bar.
- [var menu: NSMenu?](nsstatusitem/menu.md)
  The pull-down menu displayed when the user clicks the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.struct)*