# triggerValue

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The value of the characteristic that triggers the event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var triggerValue: TriggerValueType? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) TriggerValueType triggerValue;
```

## Discussion

Use this property to adjust the value that triggers the event.

Set this property to `nil` to trigger the event whenever the value of the characteristic changes.

## See Also

### Configuring the event
- [var characteristic: HMCharacteristic](./characteristic.md)
  The characteristic associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicevent/triggervalue)*