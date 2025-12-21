# menuHasKeyEquivalent(_:for:target:action:)

**Framework**: AppKit  
**Kind**: method

Invoked to allow the delegate to return the target and action for a key-down event.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func menuHasKeyEquivalent(_ menu: NSMenu, for event: NSEvent, target: AutoreleasingUnsafeMutablePointer<AnyObject?>, action: UnsafeMutablePointer<Selector?>) -> Bool
```

#### Return Value

If there is a valid and enabled menu item that corresponds to this key-down even, return [`true`](https://developer.apple.com/documentation/Swift/true) after specifying the target and action. Return [`false`](https://developer.apple.com/documentation/Swift/false) if there are no items with that key equivalent or if the item is disabled.

#### Discussion

If the delegate doesn’t define this method, the menu is populated to find out if any items have a matching key equivalent.

## Parameters

- `menu`: The menu object sending the delegation message.
- `event`: An   object representing a key-down event.
- `target`: Return by reference the target object for the menu item that corresponds to the event. Specify   to request the menu’s target.
- `action`: Return by reference the action selector for the menu item that corresponds to the event.

## See Also

- [func performActionForItem(at: Int)](nsmenu/performactionforitem(at:).md)
  Causes the application to send the action message of a specified menu item to its target.
- [Application Menu and Pop-up List Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MenuList/MenuList.html#//apple_ref/doc/uid/10000032i)
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsmenu/performkeyequivalent(with:).md)
  Performs the action for the menu item that corresponds to the given key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menuhaskeyequivalent(_:for:target:action:))*