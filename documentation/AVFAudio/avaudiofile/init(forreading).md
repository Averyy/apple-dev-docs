# init(forReading:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initForReading:(NSURL *) fileURL error:(NSError **) outError;
```

## Return Value

A new `AVAudioFile` instance you use for reading.

## Parameters

- `fileURL`: The file to read.

## See Also

### Creating an audio file
- [init(forReading: URL, commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](./init%28forreading,commonformat,interleaved%29.md)
  Opens a file for reading using the specified processing format.
- [init(forWriting: URL, settings: [String : Any]) throws](./init%28forwriting,settings%29.md)
  Opens a file for writing using the specified settings.
- [init(forWriting: URL, settings: [String : Any], commonFormat: AVAudioCommonFormat, interleaved: Bool) throws](./init%28forwriting,settings,commonformat,interleaved%29.md)
  Opens a file for writing using a specified processing format and settings.
- [init()](./init%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiofile/init(forreading:))*