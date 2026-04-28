# init(PCMFormat:bufferListNoCopy:deallocator:)

**Framework**: AVFAudio  
**Kind**: init

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init?(PCMFormat format: AVAudioFormat, bufferListNoCopy bufferList: UnsafePointer<AudioBufferList>, deallocator: ((UnsafePointer<AudioBufferList>) -> Void)? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(pcmformat:bufferlistnocopy:deallocator:)-2ms1j)*