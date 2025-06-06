# init(characteristic:triggerValue:)

**Framework**: HomeKit  
**Kind**: init

Creates a new characteristic event which triggers when the specified characteristic reaches the specified value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
init(characteristic: HMCharacteristic, triggerValue: TriggerValueType?)
```

#### Return Value

An initialized characteristic event for the specified characteristic and trigger value.

#### Discussion

Use a characteristic that supports notification; otherwise this initializer throws an exception.

## Parameters

- `characteristic`: The characteristic that the event is observing.
- `triggerValue`: The value of the characteristic that triggers the event. Specifying   causes the event to fire every time the value of the characteristic changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/init(characteristic:triggervalue:))*