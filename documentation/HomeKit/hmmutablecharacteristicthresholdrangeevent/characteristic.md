# characteristic

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readwrite) HMCharacteristic * characteristic;
```

## Discussion

Use this property to change the event’s characteristic.

The characteristic must support notification.

## See Also

### Configuring a characteristic threshold event
- [var thresholdRange: HMNumberRange](./thresholdrange.md)
  The range of the characteristic value that triggers the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicthresholdrangeevent/characteristic)*