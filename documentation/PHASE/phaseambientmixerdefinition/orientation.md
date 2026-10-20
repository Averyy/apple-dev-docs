# orientation

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A quaternion that describes the orientation of the speaker layout relative to the scene origin.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var orientation: simd_quatf { get }
```

```objc
@property (nonatomic, readonly) simd_quatf orientation;
```

#### Discussion

The framework sets the value to the `orientation` initializer argument. See [`init(channelLayout:orientation:)`](./init%28channellayout,orientation%29.md).

## See Also

### Inspecting the Mixer
- [var inputChannelLayout: AVAudioChannelLayout](./inputchannellayout.md)
  The channel layout of input audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseambientmixerdefinition/orientation)*