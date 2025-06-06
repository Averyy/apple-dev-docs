# eventValues

**Framework**: Audio Toolbox  
**Kind**: property

The values for this parameter event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var eventValues: AudioUnitParameterEvent.__Unnamed_union_eventValues
```

#### Discussion

If the parameter event type is [`AUParameterEventType.parameterEvent_Immediate`](auparametereventtype/parameterevent_immediate.md), use the `immediate` struct of this union. If the parameter event type is [`AUParameterEventType.parameterEvent_Ramped`](auparametereventtype/parameterevent_ramped.md), use the `ramp` struct of this union.

###### Immediate

###### Ramp

## See Also

- [var scope: AudioUnitScope](audiounitparameterevent/scope.md)
  The scope for this parameter event.
- [var element: AudioUnitElement](audiounitparameterevent/element.md)
  The element for this parameter event.
- [var parameter: AudioUnitParameterID](audiounitparameterevent/parameter.md)
  An identifier for this parameter event.
- [var eventType: AUParameterEventType](audiounitparameterevent/eventtype.md)
  The type for this parameter event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterevent/eventvalues)*