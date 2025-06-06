# removalAllowed

**Framework**: AppKit  
**Kind**: property

A status item that allows interactive removal.

**Availability**:
- macOS 10.12+

## Declaration

```swift
static var removalAllowed: NSStatusItem.Behavior { get }
```

#### Discussion

Status items with this behavior allow interactive removal from the menu bar. Upon removal, the item’s [`isVisible`](nsstatusitem/isvisible.md) property changes to [`false`](https://developer.apple.com/documentation/swift/false). This change is observable using key-value observation.

## See Also

- [static var terminationOnRemoval: NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct/terminationonremoval.md)
  A status item that quits the application upon removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.struct/removalallowed)*