# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs the action for the menu item that corresponds to the given key equivalent.

**Availability**:
- macOS

## Declaration

```swift
func performKeyEquivalent(with event: NSEvent) -> Bool
```

```objc
- (BOOL) performKeyEquivalent:(NSEvent *) event;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if `event` is a key equivalent that the menu should handle, otherwise returns [`false`](../../Swift/false.md).

## Parameters

- `event`: An [`NSEvent`](../nsevent.md) object that represents a key-equivalent event.

## See Also

### Related Documentation
- [func menuHasKeyEquivalent(NSMenu, for: NSEvent, target: AutoreleasingUnsafeMutablePointer<AnyObject?>, action: UnsafeMutablePointer<Selector?>) -> Bool](../nsmenudelegate/menuhaskeyequivalent%28_,for,target,action%29.md)
  Invoked to allow the delegate to return the target and action for a key-down event.
- [func performActionForItem(at: Int)](./performactionforitem%28at%29.md)
  Causes the application to send the action message of a specified menu item to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/performkeyequivalent(with:))*