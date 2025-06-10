# actions

**Framework**: HomeKit  
**Kind**: property

Set of actions in the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var actions: Set<HMAction> { get }
```

## See Also

- [func addAction(HMAction, completionHandler: ((any Error)?) -> Void)](hmactionset/addaction(_:completionhandler:).md)
  Adds an action to the action set.
- [func removeAction(HMAction, completionHandler: ((any Error)?) -> Void)](hmactionset/removeaction(_:completionhandler:).md)
  Removes an action from the action set.
- [class HMCharacteristicWriteAction](hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.
- [class HMAction](hmaction.md)
  An abstract base class for actions in HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/actions)*