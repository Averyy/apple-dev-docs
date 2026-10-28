# thresholdRange

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The range of the characteristic value that triggers the event.

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
var thresholdRange: HMNumberRange { get set }
```

```objc
@property (nonatomic, copy, readwrite) HMNumberRange * thresholdRange;
```

## Discussion

Use this property to adjust the range of characteristic values that trigger the event.

## See Also

### Configuring a characteristic threshold event
- [var characteristic: HMCharacteristic](./characteristic.md)
  The characteristic associated with the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicthresholdrangeevent/thresholdrange)*