# menuHasKeyEquivalent(_:for:target:action:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to allow the delegate to return the target and action for a key-down event.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func menuHasKeyEquivalent(_ menu: NSMenu, for event: NSEvent, target: AutoreleasingUnsafeMutablePointer<AnyObject?>, action: UnsafeMutablePointer<Selector?>) -> Bool
```

```objc
- (BOOL) menuHasKeyEquivalent:(NSMenu *) menu forEvent:(NSEvent *) event target:(id*) target action:(SEL*) action;
```

#### Return Value

If there is a valid and enabled menu item that corresponds to this key-down even, return [`true`](../../Swift/true.md) after specifying the target and action. Return [`false`](../../Swift/false.md) if there are no items with that key equivalent or if the item is disabled.

#### Discussion

If the delegate doesn’t define this method, the menu is populated to find out if any items have a matching key equivalent.

## Parameters

- `menu`: The menu object sending the delegation message.
- `event`: An [`NSEvent`](../nsevent.md) object representing a key-down event.
- `target`: Return by reference the target object for the menu item that corresponds to the event. Specify `nil` to request the menu’s target.
- `action`: Return by reference the action selector for the menu item that corresponds to the event.

## See Also

### Related Documentation
- [func performActionForItem(at: Int)](../nsmenu/performactionforitem%28at%29.md)
  Causes the application to send the action message of a specified menu item to its target.
- [func performKeyEquivalent(with: NSEvent) -> Bool](../nsmenu/performkeyequivalent%28with%29.md)
  Performs the action for the menu item that corresponds to the given key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menuhaskeyequivalent(_:for:target:action:))*