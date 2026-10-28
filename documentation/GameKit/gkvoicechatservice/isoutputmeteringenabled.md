# isOutputMeteringEnabled

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the voice level of remote participants is monitored.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
var isOutputMeteringEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isOutputMeteringEnabled) BOOL outputMeteringEnabled;
```

## Discussion

If [`true`](../../Swift/true.md), your application can read the [`outputMeterLevel`](./outputmeterlevel.md) property to monitor sound level of remote participants. If [`false`](../../Swift/false.md), the value of the [`outputMeterLevel`](./outputmeterlevel.md) property is undefined. Default is [`false`](../../Swift/false.md). When your application doesn’t need to monitor remote participants, it should set this property to [`false`](../../Swift/false.md) to improve performance.

## See Also

### Monitoring the Audio Level
- [var isInputMeteringEnabled: Bool](./isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var inputMeterLevel: Float](./inputmeterlevel.md)
  The volume, in decibels (db), being received by the microphone.
- [var outputMeterLevel: Float](./outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/isoutputmeteringenabled)*