# outputMeterLevel

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The volume, in decibels (db), being received from all other participants.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
var outputMeterLevel: Float { get }
```

```objc
@property (readonly) float outputMeterLevel;
```

## Discussion

The value of this property is undefined if [`isOutputMeteringEnabled`](./isoutputmeteringenabled.md) is set to [`false`](../../Swift/false.md).

The volume level is the aggregate volume of all remote participants, modified by the [`remoteParticipantVolume`](./remoteparticipantvolume.md) property.

## See Also

### Monitoring the Audio Level
- [var isInputMeteringEnabled: Bool](./isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var inputMeterLevel: Float](./inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var isOutputMeteringEnabled: Bool](./isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/outputmeterlevel)*