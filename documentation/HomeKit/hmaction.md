# HMAction

**Framework**: HomeKit  
**Kind**: class

An abstract base class for actions in HomeKit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMAction
```

#### Overview

Actions can be added to [`HMActionSet`](hmactionset.md) objects. Action sets can then be set for automatic execution in response to specific conditions using [`HMTrigger`](hmtrigger.md) objects, or manually triggered with [`executeActionSet(_:completionHandler:)`](hmhome/executeactionset(_:completionhandler:).md).

## Topics

### Identifying an action
- [var uniqueIdentifier: UUID](hmaction/uniqueidentifier.md)
  A unique identifier for the action.
### Initializers
- [init()](hmaction/init.md)
### Type Methods
- [class func new() -> Self](hmaction/new.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HMCharacteristicWriteAction](hmcharacteristicwriteaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [HomeKit Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
- [var actions: Set<HMAction>](hmactionset/actions.md)
  Set of actions in the action set.
- [func addAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/addaction(_:completionhandler:).md)
  Adds an action to the action set.
- [func removeAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/removeaction(_:completionhandler:).md)
  Removes an action from the action set.
- [class HMCharacteristicWriteAction](hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaction)*