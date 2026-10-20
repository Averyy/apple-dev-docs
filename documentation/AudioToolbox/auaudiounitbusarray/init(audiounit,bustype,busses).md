# init(audioUnit:busType:busses:)

**Framework**: Audio Toolbox  
**Kind**: init

Initializes a bus array by making a copy of the supplied busses.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(audioUnit owner: AUAudioUnit, busType: AUAudioUnitBusType, busses busArray: [AUAudioUnitBus])
```

#### Return Value

A newly-initialized bus array.

## Parameters

- `owner`: The audio unit that owns the bus array.
- `busType`: Determines whether the busses are for input or output.
- `busArray`: An array of busses.

## See Also

- [convenience init(audioUnit: AUAudioUnit, busType: AUAudioUnitBusType)](auaudiounitbusarray/init(audiounit:bustype:).md)
  Initializes an empty bus array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/init(audiounit:bustype:busses:))*