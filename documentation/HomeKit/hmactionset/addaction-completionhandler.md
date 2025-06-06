# addAction(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds an action to the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func addAction(_ action: HMAction) async throws
```

## Parameters

- `action`: The action to add. Actions may only be in one set—create separate   objects for the same conceptual action if you want an action to be in more than one action set.
- `completion`: The block executed after the request is processed.

## See Also

- [var actions: Set<HMAction>](hmactionset/actions.md)
  Set of actions in the action set.
- [func removeAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/removeaction(_:completionhandler:).md)
  Removes an action from the action set.
- [class HMCharacteristicWriteAction](hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.
- [class HMAction](hmaction.md)
  An abstract base class for actions in HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/addaction(_:completionhandler:))*