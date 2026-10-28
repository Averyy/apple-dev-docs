# audioUnit

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The underlying Core Audio audio unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) AudioUnit audioUnit;
```

## Discussion

This property is a reference to the underlying audio unit. The `AVAudioUnit` exposes it here so that you can modify parameters, that you don’t see through `AVAudioUnit` subclasses, using the AudioUnit C API. For example, changing initialization state, stream formats, channel layouts, or connections to other audio units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/audiounit-4wpas)*