# CVBuffer Attachment Keys

**Framework**: Core Video

The attachment types for a Core Video buffer.

## Topics

### Constants
- [let kCVBufferMovieTimeKey: CFString](kcvbuffermovietimekey.md)
  The movie time associated with the buffer. Generally only available for frames emitted by QuickTime (type `CFDictionary` containing the [`kCVBufferTimeValueKey`](kcvbuffertimevaluekey.md) and [`kCVBufferTimeScaleKey`](kcvbuffertimescalekey.md) keys).
- [let kCVBufferTimeValueKey: CFString](kcvbuffertimevaluekey.md)
  The time value associated with the movie.
- [let kCVBufferTimeScaleKey: CFString](kcvbuffertimescalekey.md)
  The time scale associated with the movie.

## See Also

- [CVBuffer Attribute Keys](cvbuffer-attribute-keys.md)
  The attributes associated with Core Video buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvbuffer-attachment-keys)*