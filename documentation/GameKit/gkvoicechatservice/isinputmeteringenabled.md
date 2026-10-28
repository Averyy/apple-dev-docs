# isInputMeteringEnabled

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the microphone’s sound level is being monitored.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
var isInputMeteringEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isInputMeteringEnabled) BOOL inputMeteringEnabled;
```

## Discussion

If [`true`](../../Swift/true.md), your application can read the [`inputMeterLevel`](./inputmeterlevel.md) property to monitor the sound level of the microphone. If [`false`](../../Swift/false.md), the value of the [`inputMeterLevel`](./inputmeterlevel.md) property is undefined. Default is [`false`](../../Swift/false.md). When your application doesn’t need to monitor the microphone, it should set this property to [`false`](../../Swift/false.md) to improve performance.

## See Also

### Monitoring the Audio Level
- [var inputMeterLevel: Float](./inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var isOutputMeteringEnabled: Bool](./isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.
- [var outputMeterLevel: Float](./outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/isinputmeteringenabled)*