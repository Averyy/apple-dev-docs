# init(significantEvent:offset:)

**Framework**: HomeKit  
**Kind**: init

Creates a new significant time event with the specified significant event and offset.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(significantEvent: HMSignificantEvent, offset: DateComponents?)
```

#### Return Value

An initialized significant time event which fires at the specified offset from the provided significant event.

#### Discussion

To specify that this event should fire before the significant event, supply a date components object with negative values. For example, to specify 30 minutes before sunset, the [`minute`](https://developer.apple.com/documentation/Foundation/DateComponents/minute) property of the `offset` argument must be set to `-30`.

## Parameters

- `significantEvent`: The significant event for this trigger, for example  .
- `offset`: A date components instance that represents the offset from the significant event that this event fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmsignificanttimeevent/init(significantevent:offset:))*