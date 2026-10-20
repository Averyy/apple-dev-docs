# removeAction(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes an action from the action set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeAction(_ action: HMAction, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeAction(_ action: HMAction) async throws
```

```objc
- (void) removeAction:(HMAction *) action completionHandler:(HMErrorBlock) completion;
```

## Parameters

- `action`: The action to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Defining the associated actions
- [var actions: Set<HMAction>](./actions.md)
  Set of actions in the action set.
- [func addAction(HMAction, completionHandler: ((any Error)?) -> Void)](./addaction%28_,completionhandler%29.md)
  Adds an action to the action set.
- [class HMCharacteristicWriteAction](../hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.
- [class HMAction](../hmaction.md)
  An abstract base class for actions in HomeKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/removeaction(_:completionhandler:))*