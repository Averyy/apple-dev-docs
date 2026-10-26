# spatialEventTrigger

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location-based trigger to apply to the task.

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

#### Discussion

If no trigger information is available in this property, do not attempt to change the spatial trigger of the task.

## See Also

### Getting the Triggers
- [var temporalEventTrigger: INTemporalEventTrigger?](./temporaleventtrigger.md)
  The time-based trigger to apply to the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/spatialeventtrigger)*