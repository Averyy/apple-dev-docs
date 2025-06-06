# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method

Performs the action for the menu item that corresponds to the given key equivalent.

**Availability**:
- macOS ?+

## Declaration

```swift
func performKeyEquivalent(with event: NSEvent) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if `event` is a key equivalent that the menu should handle, otherwise returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `event`: An   object that represents a key-equivalent event.

## See Also

- [func menuHasKeyEquivalent(NSMenu, for: NSEvent, target: AutoreleasingUnsafeMutablePointer<AnyObject?>, action: UnsafeMutablePointer<Selector?>) -> Bool](nsmenudelegate/menuhaskeyequivalent(_:for:target:action:).md)
  Invoked to allow the delegate to return the target and action for a key-down event.
- [func performActionForItem(at: Int)](nsmenu/performactionforitem(at:).md)
  Causes the application to send the action message of a specified menu item to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/performkeyequivalent(with:))*