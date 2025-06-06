# isInputMeteringEnabled

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the microphone’s sound level is being monitored.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isInputMeteringEnabled: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), your application can read the [`inputMeterLevel`](gkvoicechatservice/inputmeterlevel.md) property to monitor the sound level of the microphone. If [`false`](https://developer.apple.com/documentation/swift/false), the value of the [`inputMeterLevel`](gkvoicechatservice/inputmeterlevel.md) property is undefined. Default is [`false`](https://developer.apple.com/documentation/swift/false). When your application doesn’t need to monitor the microphone, it should set this property to [`false`](https://developer.apple.com/documentation/swift/false) to improve performance.

## See Also

- [var inputMeterLevel: Float](gkvoicechatservice/inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var isOutputMeteringEnabled: Bool](gkvoicechatservice/isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.
- [var outputMeterLevel: Float](gkvoicechatservice/outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/isinputmeteringenabled)*