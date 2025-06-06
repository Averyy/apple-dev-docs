# AudioFileStream_PropertyListenerProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Invoked by an audio file stream parser when it finds a property value in the audio file stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioFileStream_PropertyListenerProc = (UnsafeMutableRawPointer, AudioFileStreamID, AudioFileStreamPropertyID, UnsafeMutablePointer<AudioFileStreamPropertyFlags>) -> Void
```

#### Discussion

If you named your function `MyAudioFileStream_PropertyListenerProc`, you would declare it like this:

##### Discussion

When the parser calls your property listener, check the `ioFlags` value to see if the property value is being cached. If not, you can call the [`AudioFileStreamGetPropertyInfo(_:_:_:_:)`](audiofilestreamgetpropertyinfo(_:_:_:_:).md) and [`AudioFileStreamGetProperty(_:_:_:_:)`](audiofilestreamgetproperty(_:_:_:_:).md) functions to obtain the value of the property from inside the property listener, or you can set the `kAudioFileStreamPropertyFlag_CacheProperty` flag on return to cause the parser to cache the value.

In some cases when you call the [`AudioFileStreamGetProperty(_:_:_:_:)`](audiofilestreamgetproperty(_:_:_:_:).md) function from inside the property listener, because of boundaries in the input data, the parser returns the result code `“kAudioFileStreamError_DataUnavailable”` indicating the value is not yet available. When unavailable data is requested from within the property listener, the parser begins caching the property value and calls the property listener again when the property value is available. If the `kAudioFileStreamPropertyFlag_PropertyIsCached` flag is not set, this is your only opportunity to get the value of the property, as the data is disposed of when the property listener callback returns.

## Parameters

- `inClientData`: The value you provided in the   parameter when you called the  function.
- `inAudioFileStream`: The ID of the audio file stream parser that invoked the callback. The parser ID is returned by the   function.
- `inPropertyID`: The four-character ID of the property that the parser found in the audio file data stream. See   for possible values.
- `ioFlags`: On input, if the   value is set, the parser is caching the property value. If not, on output you can set the   flag to cause the parser to cache the value. See  .

## See Also

- [typealias AudioFileStream_PacketsProc](audiofilestream_packetsproc.md)
  Invoked by an audio file stream parser when it finds audio data in the audio file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestream_propertylistenerproc)*