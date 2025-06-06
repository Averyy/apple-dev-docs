# characteristic

**Framework**: HomeKit  
**Kind**: property

The characteristic associated with the event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var characteristic: HMCharacteristic { get set }
```

#### Discussion

Use this property to change the event’s characteristic.

The characteristic must support notification.

## See Also

- [var triggerValue: TriggerValueType?](hmmutablecharacteristicevent/triggervalue.md)
  The value of the characteristic that triggers the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicevent/characteristic)*