# audioSamplePacketRefreshCount

**Framework**: AVFoundation  
**Kind**: property

The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.

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
var audioSamplePacketRefreshCount: Int
```

#### Discussion

The value of [`audioSampleIsIndependentlyDecodable`](avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable.md) must be [`true`](https://developer.apple.com/documentation/swift/true) for this value to take effect.

The value of this property is `0` for Immediate Playout Frames (IPFs).

## See Also

- [var audioSampleIsIndependentlyDecodable: ObjCBool](avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable.md)
  A Boolean value indicating whether the sample is independently decodable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount)*