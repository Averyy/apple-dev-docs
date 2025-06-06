# HMActionSet

**Framework**: HomeKit  
**Kind**: class

A collection of actions that you trigger as a group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMActionSet
```

#### Overview

Action sets can be executed as a result of evaluating a trigger (instances of [`HMTrigger`](hmtrigger.md)) or manually with [`executeActionSet(_:completionHandler:)`](hmhome/executeactionset(_:completionhandler:).md). Actions in an action set are performed in an unspecified order. You create new action sets using the [`addActionSet(withName:completionHandler:)`](hmhome/addactionset(withname:completionhandler:).md) method of [`HMHome`](hmhome.md).

## Topics

### Identifiying an action set
- [var uniqueIdentifier: UUID](hmactionset/uniqueidentifier.md)
  The action set’s unique identifier.
- [var name: String](hmactionset/name.md)
  The name of the action set.
- [func updateName(String, completionHandler: HMErrorBlock)](hmactionset/updatename(_:completionhandler:).md)
  Updates the name of the action set.
### Specifying a type
- [var actionSetType: String](hmactionset/actionsettype.md)
  The type of the action set, such as built-in or user-defined.
- [Action Set Types](action-set-types.md)
  The types of action sets that you can define.
### Defining the associated actions
- [var actions: Set<HMAction>](hmactionset/actions.md)
  Set of actions in the action set.
- [func addAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/addaction(_:completionhandler:).md)
  Adds an action to the action set.
- [func removeAction(HMAction, completionHandler: HMErrorBlock)](hmactionset/removeaction(_:completionhandler:).md)
  Removes an action from the action set.
- [class HMCharacteristicWriteAction](hmcharacteristicwriteaction.md)
  An action in an action set that writes a value to a characteristic.
- [class HMAction](hmaction.md)
  An abstract base class for actions in HomeKit.
### Keeping track of execution
- [var isExecuting: Bool](hmactionset/isexecuting.md)
  The execution status of the action set.
- [var lastExecutionDate: Date?](hmactionset/lastexecutiondate.md)
  The last execution date of the action set.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset)*