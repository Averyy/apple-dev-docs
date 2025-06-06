# HMTrigger

**Framework**: HomeKit  
**Kind**: class

An abstract base class for triggering actions based on a set of conditions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMTrigger
```

#### Overview

This class defines the basic behavior of triggers, but does not itself specify any criteria for firing a trigger. Use instances of subclasses of [`HMTrigger`](hmtrigger.md) to set up concrete triggers for actions.

## Topics

### Managing Triggers
- [var name: String](hmtrigger/name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmtrigger/updatename(_:completionhandler:).md)
  Updates the name of the trigger.
- [var isEnabled: Bool](hmtrigger/isenabled.md)
  State of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](hmtrigger/enable(_:completionhandler:).md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](hmtrigger/lastfiredate.md)
  The last time this trigger fired.
- [var uniqueIdentifier: UUID](hmtrigger/uniqueidentifier.md)
  A unique identifier for this trigger.
### Managing Action Sets
- [var actionSets: [HMActionSet]](hmtrigger/actionsets.md)
  Array of all action sets that will be executed by the trigger.
- [func addActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmtrigger/addactionset(_:completionhandler:).md)
  Adds an action set to the trigger.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmtrigger/removeactionset(_:completionhandler:).md)
  Removes an action set from the trigger.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HMEventTrigger](hmeventtrigger.md)
- [HMTimerTrigger](hmtimertrigger.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var triggers: [HMTrigger]](hmhome/triggers.md)
  An array of triggers defined in the home.
- [func addTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/addtrigger(_:completionhandler:).md)
  Adds a trigger to the home.
- [func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/removetrigger(_:completionhandler:).md)
  Removes a trigger from the home.
- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger)*