# eventValues

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The values for this parameter event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues
```

```c
union { ... } eventValues;
```

## Discussion

If the parameter event type is [`AUParameterEventType.parameterEvent_Immediate`](../auparametereventtype/parameterevent_immediate.md), use the `immediate` struct of this union. If the parameter event type is [`AUParameterEventType.parameterEvent_Ramped`](../auparametereventtype/parameterevent_ramped.md), use the `ramp` struct of this union.

#### immediate

- ****bufferOffset****: A `UInt32` value that indicates the sample time at which to change the parameter value.
- ****value****: An [`AudioUnitParameterValue`](../audiounitparametervalue.md) that indicates the new parameter value.

#### ramp

- ****startBufferOffset****: An `SInt32` value that indicates the sample time at which to begin the parameter value change.
- ****durationInFrames****: A `UInt32` value that indicates the number of frames over which the parameter value should linearly change from  `startValue` to `endValue`.
- ****startValue****: An [`AudioUnitParameterValue`](../audiounitparametervalue.md) that indicates the starting parameter value.
- ****endValue****: An [`AudioUnitParameterValue`](../audiounitparametervalue.md) that indicates the ending parameter value.

## Topics

### Instance Properties
- [immediate](./eventvalues/immediate.md)
- [ramp](./eventvalues/ramp.md)

## See Also

### Fields
- [var scope: AudioUnitScope](./scope.md)
  The scope for this parameter event.
- [var element: AudioUnitElement](./element.md)
  The element for this parameter event.
- [var parameter: AudioUnitParameterID](./parameter.md)
  An identifier for this parameter event.
- [var eventType: AUParameterEventType](./eventtype.md)
  The type for this parameter event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/eventvalues)*