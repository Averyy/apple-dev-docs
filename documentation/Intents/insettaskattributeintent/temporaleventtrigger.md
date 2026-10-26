# temporalEventTrigger

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The time-based trigger to apply to the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var temporalEventTrigger: INTemporalEventTrigger? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INTemporalEventTrigger * temporalEventTrigger;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INTemporalEventTrigger * temporalEventTrigger;
```

#### Discussion

If no trigger information is available in this property, do not attempt to change the temporal trigger of the task.

## See Also

### Getting the Triggers
- [var spatialEventTrigger: INSpatialEventTrigger?](./spatialeventtrigger.md)
  The location-based trigger to apply to the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/temporaleventtrigger)*