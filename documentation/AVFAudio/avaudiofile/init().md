# init()

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 10.10+ - Deprecated in 26.0
- macOS 10.10+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Deprecated - use initForReading or initForWriting

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## See Also

### Creating an audio file
- [init(forReading: URL) throws](./init%28forreading%29.md)
  Opens a file for reading using the standard, deinterleaved floating point format.
- [init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](./init%28forreading,commonformat,interleaved%29.md)
  Opens a file for reading using the specified processing format.
- [init(forWriting: URL, settings: [String : Any]) throws](./init%28forwriting,settings%29.md)
  Opens a file for writing using the specified settings.
- [init(forWriting: URL, settings: [String : Any], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](./init%28forwriting,settings,commonformat,interleaved%29.md)
  Opens a file for writing using a specified processing format and settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/init())*