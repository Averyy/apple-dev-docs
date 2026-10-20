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
var characteristic: HMCharacteristic { get }
```

```objc
@property (nonatomic, strong, readonly) HMCharacteristic * characteristic;
```

## See Also

### Inspecting a characteristic threshold event
- [var thresholdRange: HMNumberRange](./thresholdrange.md)
  The range of the characteristic value that triggers the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicthresholdrangeevent/characteristic)*