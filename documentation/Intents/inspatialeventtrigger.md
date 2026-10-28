# INSpatialEventTrigger

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A trigger condition based on the user’s arrival or departure from a given location.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INSpatialEventTrigger
```

```objc
@interface INSpatialEventTrigger : NSObject
```

## Overview

When configuring tasks, you can add an [`INSpatialEventTrigger`](./inspatialeventtrigger.md) object to display a reminder when the user approaches or leaves a specific location. Spatial event triggers rely on location services to generate events.

## Topics

### Initializing an Event Trigger
- [init(placemark: CLPlacemark, event: INSpatialEvent)](./inspatialeventtrigger/init%28placemark,event%29.md)
  Initializes the event trigger with the specified location-based information.
### Getting the Trigger Condition
- [var placemark: CLPlacemark](./inspatialeventtrigger/placemark.md)
  The location that triggers an event.
- [var event: INSpatialEvent](./inspatialeventtrigger/event.md)
  The conditions which trigger an event for the specified location.
- [enum INSpatialEvent](./inspatialevent.md)
  Constants indicating when to deliver location-related events.
### Initializers
- [init?(coder: NSCoder)](./inspatialeventtrigger/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Event Triggers
- [class INTemporalEventTrigger](./intemporaleventtrigger.md)
  A trigger condition based on a date or time.
- [class INTemporalEventTriggerTypeOptionsResolutionResult](./intemporaleventtriggertypeoptionsresolutionresult.md)
  A resolution result that adds a temporal event trigger.
- [struct INDayOfWeekOptions](./indayofweekoptions.md)
  Days of the week.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspatialeventtrigger)*