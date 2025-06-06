# orientation

**Framework**: AVFAudio  
**Kind**: property

The orientation of the data source relative to the device’s natural orientation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var orientation: AVAudioSession.Orientation? { get }
```

#### Discussion

This property returns `nil` if the data source’s orientation isn’t known.

## See Also

- [AVAudioSession.Orientation](avaudiosession/orientation.md)
  Constants that indicate the directions in which a data source can point, relative to the device’s natural orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/orientation)*