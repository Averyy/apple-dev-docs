# init(forWriting:settings:commonFormat:interleaved:)

**Framework**: AVFAudio  
**Kind**: init

Opens a file for writing using a specified processing format and settings.

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
init(forWriting fileURL: URL, settings: [String : Any], commonFormat format: AVAudioCommonFormat, interleaved: Bool) throws
```

#### Return Value

A new `AVAudioFile` instance for writing.

#### Discussion

This method infers the file type to create from the file extension of `fileURL`, and overwrites a file at the specified URL if a file exists.

For more information about the `settings` parameter, see the [`settings`](avaudiorecorder/settings.md) property in the [`AVAudioRecorder`](avaudiorecorder.md) class.

## Parameters

- `fileURL`: The path at which to create the file.
- `settings`: The format of the file to create.
- `format`: The processing format to use when writing to the file.
- `interleaved`: The Boolean value that indicates whether to use an interleaved processing format.

## See Also

- [var url: URL](avaudiofile/url.md)
  The location of the audio file.
- [var processingFormat: AVAudioFormat](avaudiofile/processingformat.md)
  The processing format of the file.
- [init(forReading: URL) throws](avaudiofile/init(forreading:).md)
  Opens a file for reading using the standard, deinterleaved floating point format.
- [init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](avaudiofile/init(forreading:commonformat:interleaved:).md)
  Opens a file for reading using the specified processing format.
- [init(forWriting: URL, settings: [String : Any]) throws](avaudiofile/init(forwriting:settings:).md)
  Opens a file for writing using the specified settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/init(forwriting:settings:commonformat:interleaved:))*