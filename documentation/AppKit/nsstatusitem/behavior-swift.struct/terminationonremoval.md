# terminationOnRemoval

**Framework**: AppKit  
**Kind**: property

A status item that quits the application upon removal.

**Availability**:
- macOS 10.12+

## Declaration

```swift
static var terminationOnRemoval: NSStatusItem.Behavior { get }
```

#### Discussion

A status item with this behavior quits the application if the user removes it from the menu bar. This behavior implicitly provides the same functionality as [`removalAllowed`](nsstatusitem/behavior-swift.struct/removalallowed.md).

The [`terminationOnRemoval`](nsstatusitem/behavior-swift.struct/terminationonremoval.md) behavior is suitable for applications that display only a [`NSStatusItem`](nsstatusitem.md) and provide no other user interface.

## See Also

- [static var removalAllowed: NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct/removalallowed.md)
  A status item that allows interactive removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/behavior-swift.struct/terminationonremoval)*