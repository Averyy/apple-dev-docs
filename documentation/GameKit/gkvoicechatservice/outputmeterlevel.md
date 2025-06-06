# outputMeterLevel

**Framework**: GameKit  
**Kind**: property

The volume, in decibels (db), being received from all other participants.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var outputMeterLevel: Float { get }
```

#### Discussion

The value of this property is undefined if [`isOutputMeteringEnabled`](gkvoicechatservice/isoutputmeteringenabled.md) is set to [`false`](https://developer.apple.com/documentation/swift/false).

The volume level is the aggregate volume of all remote participants, modified by the [`remoteParticipantVolume`](gkvoicechatservice/remoteparticipantvolume.md) property.

## See Also

- [var isInputMeteringEnabled: Bool](gkvoicechatservice/isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var inputMeterLevel: Float](gkvoicechatservice/inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var isOutputMeteringEnabled: Bool](gkvoicechatservice/isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/outputmeterlevel)*