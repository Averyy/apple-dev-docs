# triggerValue

**Framework**: HomeKit  
**Kind**: property

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

#### Discussion

A value of `nil` corresponds to any change in the value of the characteristic.

## See Also

- [var characteristic: HMCharacteristic](hmcharacteristicevent/characteristic.md)
  The characteristic associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/triggervalue)*