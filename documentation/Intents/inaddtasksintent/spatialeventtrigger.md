# spatialEventTrigger

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location-based trigger to associate with each of the new tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var spatialEventTrigger: INSpatialEventTrigger? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpatialEventTrigger * spatialEventTrigger;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpatialEventTrigger * spatialEventTrigger;
```

## Discussion

Assign the specified trigger, if any, to all of the tasks that you create.

## See Also

### Getting the Trigger Information
- [var temporalEventTrigger: INTemporalEventTrigger?](./temporaleventtrigger.md)
  The time-based trigger to associate with each of the new tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintent/spatialeventtrigger)*