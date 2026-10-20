# HMAction

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMAction : NSObject
```

#### Overview

Actions can be added to [`HMActionSet`](./hmactionset.md) objects. Action sets can then be set for automatic execution in response to specific conditions using [`HMTrigger`](./hmtrigger.md) objects, or manually triggered with [`executeActionSet(_:completionHandler:)`](./hmhome/executeactionset%28_,completionhandler%29.md).

## Topics

### Identifying an action
- [var uniqueIdentifier: UUID](./hmaction/uniqueidentifier.md)
  A unique identifier for the action.
### Initializers
- [init()](./hmaction/init%28%29.md)
### Type Methods
- [class func new() -> Self](./hmaction/new%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HMCharacteristicWriteAction](./hmcharacteristicwriteaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [HomeKit Developer Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
### Defining the associated actions
- [var actions: Set<HMAction>](./hmactionset/actions.md)
  Set of actions in the action set.
- [func addAction(HMAction, completionHandler: ((any Error)?) -> Void)](./hmactionset/addaction%28_,completionhandler%29.md)
  Adds an action to the action set.
- [func removeAction(HMAction, completionHandler: ((any Error)?) -> Void)](./hmactionset/removeaction%28_,completionhandler%29.md)
  Removes an action from the action set.
- [class HMCharacteristicWriteAction](./hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaction)*