# init(forReading:)

**Framework**: AVFAudio  
**Kind**: init

Opens a file for reading using the standard, deinterleaved floating point format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forReading fileURL: URL) throws
```

#### Return Value

A new `AVAudioFile` instance you use for reading.

## Parameters

- `fileURL`: The file to read.

## See Also

- [init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](avaudiofile/init(forreading:commonformat:interleaved:).md)
  Opens a file for reading using the specified processing format.
- [init(forWriting: URL, settings: [String : Any]) throws](avaudiofile/init(forwriting:settings:).md)
  Opens a file for writing using the specified settings.
- [init(forWriting: URL, settings: [String : Any], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](avaudiofile/init(forwriting:settings:commonformat:interleaved:).md)
  Opens a file for writing using a specified processing format and settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/init(forreading:))*