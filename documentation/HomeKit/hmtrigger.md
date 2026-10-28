# HMTrigger

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMTrigger : NSObject
```

## Overview

This class defines the basic behavior of triggers, but does not itself specify any criteria for firing a trigger. Use instances of subclasses of [`HMTrigger`](./hmtrigger.md) to set up concrete triggers for actions.

## Topics

### Managing Triggers
- [var name: String](./hmtrigger/name.md)
  The name of the trigger.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./hmtrigger/updatename%28_,completionhandler%29.md)
  Updates the name of the trigger.
- [var isEnabled: Bool](./hmtrigger/isenabled.md)
  State of the trigger.
- [func enable(Bool, completionHandler: ((any Error)?) -> Void)](./hmtrigger/enable%28_,completionhandler%29.md)
  Changes the enabled state of the trigger.
- [var lastFireDate: Date?](./hmtrigger/lastfiredate.md)
  The last time this trigger fired.
- [var uniqueIdentifier: UUID](./hmtrigger/uniqueidentifier.md)
  A unique identifier for this trigger.
### Managing Action Sets
- [var actionSets: [HMActionSet]](./hmtrigger/actionsets.md)
  Array of all action sets that will be executed by the trigger.
- [func addActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./hmtrigger/addactionset%28_,completionhandler%29.md)
  Adds an action set to the trigger.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](./hmtrigger/removeactionset%28_,completionhandler%29.md)
  Removes an action set from the trigger.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HMEventTrigger](./hmeventtrigger.md)
- [HMTimerTrigger](./hmtimertrigger.md)
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

### Triggering an action set
- [var triggers: [HMTrigger]](./hmhome/triggers.md)
  An array of triggers defined in the home.
- [func addTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](./hmhome/addtrigger%28_,completionhandler%29.md)
  Adds a trigger to the home.
- [func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](./hmhome/removetrigger%28_,completionhandler%29.md)
  Removes a trigger from the home.
- [class HMTimerTrigger](./hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](./hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger)*