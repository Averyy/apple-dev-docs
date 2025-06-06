# HMEventTrigger

**Framework**: HomeKit  
**Kind**: class

A trigger to activate an action set based on a set of events and optional conditions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMEventTrigger
```

#### Overview

Use an [`HMEventTrigger`](hmeventtrigger.md) object to trigger the execution of a scene when a combination of characteristic or location events and conditions occur. To create an event trigger, first create one or more event objects that fire an event when the specified trigger values are met. For example, you might create an [`HMCharacteristicEvent`](hmcharacteristicevent.md) that fires when the front door is open. Then, you can use [`HMEventTrigger`](hmeventtrigger.md) convenience methods to create optional predicates that specify conditions that must be met before a scene is executed. For example, you might create a condition that ensures the scene is executed only after sunset.

## Topics

### Creating an event trigger
- [init(name: String, events: [HMEvent], predicate: NSPredicate?)](hmeventtrigger/init(name:events:predicate:).md)
  Creates a new event trigger with the specified name, events, and predicate.
- [init(name: String, events: [HMEvent], end: [HMEvent]?, recurrences: [DateComponents]?, predicate: NSPredicate?)](hmeventtrigger/init(name:events:end:recurrences:predicate:).md)
  Creates a new event trigger with the specified name, events, end events, recurrences, and predicate.
### Querying trigger activation state
- [var triggerActivationState: HMEventTriggerActivationState](hmeventtrigger/triggeractivationstate.md)
  The current activation state of the trigger.
- [enum HMEventTriggerActivationState](hmeventtriggeractivationstate.md)
  The activation state of an event trigger.
### Setting trigger events
- [var events: [HMEvent]](hmeventtrigger/events.md)
  The events that activate the trigger.
- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateevents(_:completionhandler:).md)
  Updates the set of trigger events.
- [Location events](location-events.md)
  Events that represent the user’s movement among regions.
- [Time events](time-events.md)
  Events based on time, significant occurrences, and time durations.
- [Characteristic events](characteristic-events.md)
  Events based on the capabilities or characteristics of accessories.
- [Presence events](presence-events.md)
  Events based on the user’s presence in a home.
- [class HMEvent](hmevent.md)
  The abstract base class for a HomeKit event.
### Restoring the previous scene after an event
- [var endEvents: [HMEvent]](hmeventtrigger/endevents.md)
  The events associated with the end of scene represented by this trigger.
- [func updateEndEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateendevents(_:completionhandler:).md)
  Updates the set of end events associated with the event trigger.
### Controlling recurrence
- [var recurrences: [DateComponents]?](hmeventtrigger/recurrences.md)
  Specifies the days on which the trigger can execute.
- [func updateRecurrences([DateComponents]?, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updaterecurrences(_:completionhandler:).md)
  Updates the days of the week the trigger can repeat.
- [var executeOnce: Bool](hmeventtrigger/executeonce.md)
  A Boolean that can execute the trigger many times.
- [func updateExecuteOnce(Bool, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateexecuteonce(_:completionhandler:).md)
  Updates the repetition status of the event trigger.
### Adding a trigger condition
- [var predicate: NSPredicate?](hmeventtrigger/predicate.md)
  The predicate to evaluate before executing the scene associated with the event trigger.
- [func updatePredicate(NSPredicate?, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updatepredicate(_:completionhandler:).md)
  Replaces the predicate used to evaluate execution of the scene associated with the event trigger.
### Creating predicates
- [class func predicateForEvaluatingTriggerOccurring(beforeSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](hmeventtrigger/predicateforevaluatingtriggeroccurring(beforesignificantevent:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTriggerOccurring(afterSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](hmeventtrigger/predicateforevaluatingtriggeroccurring(aftersignificantevent:).md)
  Creates a predicate that evaluates whether the event occurred after a significant event.
- [class func predicate(forEvaluatingTriggerOccurringBetweenSignificantEvent: HMSignificantTimeEvent, secondSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](hmeventtrigger/predicate(forevaluatingtriggeroccurringbetweensignificantevent:secondsignificantevent:).md)
  Creates a predicate that evaluates whether the event occurred between two significant events.
- [class func predicateForEvaluatingTrigger(occurringBefore: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringbefore:).md)
  Creates a predicate that evaluates whether the event occurred before the specified time.
- [class func predicateForEvaluatingTrigger(occurringOn: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringon:).md)
  Creates a predicate that evaluates whether the event occurred at the specified time.
- [class func predicateForEvaluatingTrigger(occurringAfter: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringafter:).md)
  Creates a predicate that evaluates whether the event occurred at or after the specified time.
- [class func predicateForEvaluatingTriggerOccurringBetweenDate(with: DateComponents, secondDateWith: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtriggeroccurringbetweendate(with:seconddatewith:).md)
  Creates a predicate that evaluates whether the event occurred between the specified times.
- [class func predicateForEvaluatingTrigger(HMCharacteristic, relatedBy: NSComparisonPredicate.Operator, toValue: Any) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(_:relatedby:tovalue:).md)
  Creates a predicate that evaluates whether a characteristic value relates to the specified value.
- [class func predicateForEvaluatingTrigger(withPresence: HMPresenceEvent) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(withpresence:).md)
  Creates a predicate that evaluates the current user presence against that specified in the presence event.
- [let HMCharacteristicKeyPath: String](hmcharacteristickeypath.md)
  Specifies the key path for a characteristic in a predicate.
- [let HMCharacteristicValueKeyPath: String](hmcharacteristicvaluekeypath.md)
  Specifies the key path for a characteristic value in a predicate.
- [let HMPresenceKeyPath: String](hmpresencekeypath.md)
  Specifies the key path for a presence event in a predicate.
### Deprecated symbols
- [func addEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/addevent(_:completionhandler:).md)
  Adds a new event to the event trigger.
- [func removeEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/removeevent(_:completionhandler:).md)
  Removes the specified event from the event trigger.
- [class func predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringbefore:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringafter:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.

## Relationships

### Inherits From
- [HMTrigger](hmtrigger.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HMActionSet](hmactionset.md)
  A collection of actions that you trigger as a group.
- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger)*