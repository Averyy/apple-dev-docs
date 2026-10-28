# triggerValue

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The value of the characteristic that triggers the event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var triggerValue: TriggerValueType? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) TriggerValueType triggerValue;
```

## Discussion

A value of `nil` corresponds to any change in the value of the characteristic.

## See Also

### Inspecting the event
- [var characteristic: HMCharacteristic](./characteristic.md)
  The characteristic associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/triggervalue)*