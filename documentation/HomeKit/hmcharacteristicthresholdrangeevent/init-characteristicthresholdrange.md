# init(characteristic:thresholdRange:)

**Framework**: HomeKit  
**Kind**: init

Creates a characteristic threshold range event for the specified characteristic and number range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(characteristic: HMCharacteristic, thresholdRange: HMNumberRange)
```

#### Return Value

An initialized characteristic threshold range event.

#### Discussion

Use a characteristic that supports notification; otherwise this initializer throws an exception.

## Parameters

- `characteristic`: The characteristic that the event is observing.
- `thresholdRange`: The range for the characteristic value that triggers the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicthresholdrangeevent/init(characteristic:thresholdrange:))*