# inputMeterLevel

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The volume, in decibels (db), being received by the microphone.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
var inputMeterLevel: Float { get }
```

```objc
@property (readonly) float inputMeterLevel;
```

#### Discussion

The value of this property is undefined if [`isInputMeteringEnabled`](./isinputmeteringenabled.md) is set to [`false`](../../Swift/false.md).

## See Also

### Monitoring the Audio Level
- [var isInputMeteringEnabled: Bool](./isinputmeteringenabled.md)
  A Boolean value that indicates whether the microphone’s sound level is being monitored.
- [var isOutputMeteringEnabled: Bool](./isoutputmeteringenabled.md)
  A Boolean value that indicates whether the voice level of remote participants is monitored.
- [var outputMeterLevel: Float](./outputmeterlevel.md)
  The volume, in decibels (db), being received from all other participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/inputmeterlevel)*