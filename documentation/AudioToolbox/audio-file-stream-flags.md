# Audio File Stream Flags

**Framework**: Audio Toolbox

Flags set by the property listener callback and the [`AudioFileStreamParseBytes(_:_:_:_:)`](audiofilestreamparsebytes(_:_:_:_:).md) function.

## Topics

### Constants
- [static var propertyIsCached: AudioFileStreamPropertyFlags](audiofilestreampropertyflags/propertyiscached.md)
  This flag is set when the callback [`AudioFileStream_PropertyListenerProc`](audiofilestream_propertylistenerproc.md) is invoked in the case that the value of the property has been cached and can be obtained later.
- [static var cacheProperty: AudioFileStreamPropertyFlags](audiofilestreampropertyflags/cacheproperty.md)
  A property listener sets this flag to instruct the parser to cache the property value so that it remains available after the callback returns.
- [static var discontinuity: AudioFileStreamParseFlags](audiofilestreamparseflags/discontinuity.md)
  Pass this flag to the [`AudioFileStreamParseBytes(_:_:_:_:)`](audiofilestreamparsebytes(_:_:_:_:).md) function to signal a discontinuity in the audio data.
- [static var offsetIsEstimated: AudioFileStreamSeekFlags](audiofilestreamseekflags/offsetisestimated.md)
  This flag is returned by the [`AudioFileStreamSeek(_:_:_:_:)`](audiofilestreamseek(_:_:_:_:).md) function if the byte offset is only an estimate.

## See Also

- [Audio File Stream Properties](1391506-audio-file-stream-properties.md)
  Audio file stream properties contain information that you can use to help interpret the audio data in a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-file-stream-flags)*