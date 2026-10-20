# audioSamplePacketRefreshCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var audioSamplePacketRefreshCount: Int
```

```c
NSInteger audioSamplePacketRefreshCount;
```

#### Discussion

The value of [`audioSampleIsIndependentlyDecodable`](./audiosampleisindependentlydecodable.md) must be [`true`](../../Swift/true.md) for this value to take effect.

The value of this property is `0` for Immediate Playout Frames (IPFs).

## See Also

### Querying independent decodability
- [var audioSampleIsIndependentlyDecodable: ObjCBool](./audiosampleisindependentlydecodable.md)
  A Boolean value indicating whether the sample is independently decodable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount)*