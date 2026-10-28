# audioSampleIsIndependentlyDecodable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the sample is independently decodable.

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
var audioSampleIsIndependentlyDecodable: ObjCBool
```

```c
BOOL audioSampleIsIndependentlyDecodable;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) for Immediate Playout Frames (IPFs) and Independent Frames (IFs).

## See Also

### Querying independent decodability
- [var audioSamplePacketRefreshCount: Int](./audiosamplepacketrefreshcount.md)
  The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable)*