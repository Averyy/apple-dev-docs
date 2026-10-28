# init(interval:frequency:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the recurrence rule to the specified frequency and interval.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(interval: Int, frequency: INRecurrenceFrequency)
```

```objc
- (instancetype) initWithInterval:(NSUInteger) interval frequency:(INRecurrenceFrequency) frequency;
```

## Return Value

An initialized [`INRecurrenceRule`](../inrecurrencerule.md) object or `nil` if the object could not be created.

## Parameters

- `interval`: The interval at which to repeat the specified time frame.
- `frequency`: The time frame over which to repeat the event. For a list of possible values, see [`INRecurrenceFrequency`](../inrecurrencefrequency.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrecurrencerule/init(interval:frequency:))*