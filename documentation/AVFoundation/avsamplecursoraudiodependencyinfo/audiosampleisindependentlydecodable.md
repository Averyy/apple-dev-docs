# audioSampleIsIndependentlyDecodable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the sample is independently decodable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var audioSampleIsIndependentlyDecodable: ObjCBool
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) for Immediate Playout Frames (IPFs) and Independent Frames (IFs).

## See Also

- [var audioSamplePacketRefreshCount: Int](avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount.md)
  The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable)*