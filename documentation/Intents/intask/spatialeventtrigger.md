# spatialEventTrigger

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A location-based trigger that reminds the user to complete the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTask is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

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

## See Also

### Getting the Event Triggers
- [var temporalEventTrigger: INTemporalEventTrigger?](./temporaleventtrigger.md)
  A time-based trigger that reminds the user to complete the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intask/spatialeventtrigger)*