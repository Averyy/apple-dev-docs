# NSStatusItem.Behavior

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A set of optional status item behaviors.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct Behavior
```

```c
enum NSStatusItemBehavior : NSUInteger;
```

## Topics

### Behaviors
- [static var removalAllowed: NSStatusItem.Behavior](./behavior-swift.struct/removalallowed.md)
  A status item that allows interactive removal.
- [static var terminationOnRemoval: NSStatusItem.Behavior](./behavior-swift.struct/terminationonremoval.md)
  A status item that quits the application upon removal.
### Initializers
- [init(rawValue: UInt)](./behavior-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing the status item’s behavior
- [var behavior: NSStatusItem.Behavior](./behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [var button: NSStatusBarButton?](./button.md)
  The button displayed in the status bar.
- [var menu: NSMenu?](./menu.md)
  The pull-down menu displayed when the user clicks the status item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.struct)*