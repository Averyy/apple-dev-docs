# init(audioUnit:busType:)

**Framework**: Audio Toolbox  
**Kind**: init  
**Role**: Initializer

Initializes an empty bus array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(audioUnit owner: AUAudioUnit, busType: AUAudioUnitBusType)
```

```objc
- (instancetype) initWithAudioUnit:(AUAudioUnit *) owner busType:(AUAudioUnitBusType) busType;
```

#### Return Value

A newly-initialized bus array.

## Parameters

- `owner`: The audio unit that owns the bus array.
- `busType`: Determines whether the bus array is for input or output.

## See Also

### Initialization
- [init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType, busses: [AUAudioUnitBus])](./init%28audiounit,bustype,busses%29.md)
  Initializes a bus array by making a copy of the supplied busses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/init(audiounit:bustype:))*