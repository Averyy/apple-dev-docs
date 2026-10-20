# removalAllowed

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A status item that allows interactive removal.

**Availability**:
- macOS 10.12+

## Declaration

```swift
static var removalAllowed: NSStatusItem.Behavior { get }
```

```c
NSStatusItemBehaviorRemovalAllowed
```

#### Discussion

Status items with this behavior allow interactive removal from the menu bar. Upon removal, the item’s [`isVisible`](../isvisible.md) property changes to [`false`](../../../Swift/false.md). This change is observable using key-value observation.

## See Also

### Behaviors
- [static var terminationOnRemoval: NSStatusItem.Behavior](./terminationonremoval.md)
  A status item that quits the application upon removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.struct/removalallowed)*