# terminationOnRemoval

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A status item that quits the application upon removal.

**Availability**:
- macOS 10.12+

## Declaration

```swift
static var terminationOnRemoval: NSStatusItem.Behavior { get }
```

```c
NSStatusItemBehaviorTerminationOnRemoval
```

## Discussion

A status item with this behavior quits the application if the user removes it from the menu bar. This behavior implicitly provides the same functionality as [`removalAllowed`](./removalallowed.md).

The [`terminationOnRemoval`](./terminationonremoval.md) behavior is suitable for applications that display only a [`NSStatusItem`](../../nsstatusitem.md) and provide no other user interface.

## See Also

### Behaviors
- [static var removalAllowed: NSStatusItem.Behavior](./removalallowed.md)
  A status item that allows interactive removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.struct/terminationonremoval)*