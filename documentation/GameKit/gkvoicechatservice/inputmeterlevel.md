# inputMeterLevel

**Framework**: GameKit  
**Kind**: property

The volume, in decibels (db), being received by the microphone.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var inputMeterLevel: Float { get }
```

#### Discussion

The value of this property is undefined if [`isInputMeteringEnabled`](gkvoicechatservice/isinputmeteringenabled.md) is set to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isInputMeteringEnabled: Bool](gkvoicechatservice/isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var isOutputMeteringEnabled: Bool](gkvoicechatservice/isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.
- [var outputMeterLevel: Float](gkvoicechatservice/outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/inputmeterlevel)*