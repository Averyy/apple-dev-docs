# isOutputMeteringEnabled

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the voice level of remote participants is monitored.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isOutputMeteringEnabled: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), your application can read the [`outputMeterLevel`](gkvoicechatservice/outputmeterlevel.md) property to monitor sound level of remote participants. If [`false`](https://developer.apple.com/documentation/swift/false), the value of the [`outputMeterLevel`](gkvoicechatservice/outputmeterlevel.md) property is undefined. Default is [`false`](https://developer.apple.com/documentation/swift/false). When your application doesn’t need to monitor remote participants, it should set this property to [`false`](https://developer.apple.com/documentation/swift/false) to improve performance.

## See Also

- [var isInputMeteringEnabled: Bool](gkvoicechatservice/isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var inputMeterLevel: Float](gkvoicechatservice/inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var outputMeterLevel: Float](gkvoicechatservice/outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/isoutputmeteringenabled)*