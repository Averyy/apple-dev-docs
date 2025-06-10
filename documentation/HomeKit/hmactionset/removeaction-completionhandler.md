# removeAction(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes an action from the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeAction(_ action: HMAction) async throws
```

## Parameters

- `action`: The action to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var actions: Set<HMAction>](hmactionset/actions.md)
  Set of actions in the action set.
- [func addAction(HMAction, completionHandler: ((any Error)?) -> Void)](hmactionset/addaction(_:completionhandler:).md)
  Adds an action to the action set.
- [class HMCharacteristicWriteAction](hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.
- [class HMAction](hmaction.md)
  An abstract base class for actions in HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/removeaction(_:completionhandler:))*