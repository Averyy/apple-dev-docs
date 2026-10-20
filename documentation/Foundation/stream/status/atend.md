# Stream.Status.atEnd

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case atEnd
```

```c
NSStreamStatusAtEnd
```

## See Also

### Enumeration Cases
- [Stream.Status.closed](./closed.md)
  The stream is closed ([`close()`](../close%28%29.md) has been called on it).
- [Stream.Status.error](./error.md)
  The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [Stream.Status.notOpen](./notopen.md)
  The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [Stream.Status.open](./open.md)
  The stream is open, but no reading or writing is occurring.
- [Stream.Status.opening](./opening.md)
  The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [Stream.Status.reading](./reading.md)
  Data is being read from the stream. This status would be returned if code on another thread were to call [`streamStatus`](../streamstatus.md) on the stream while a [`read(_:maxLength:)`](../../inputstream/read%28_,maxlength%29.md) call ([`InputStream`](../../inputstream.md)) was in progress.
- [Stream.Status.writing](./writing.md)
  Data is being written to the stream. This status would be returned if code on another thread were to call [`streamStatus`](../streamstatus.md) on the stream while a [`write(_:maxLength:)`](../../outputstream/write%28_,maxlength%29.md) call ([`OutputStream`](../../outputstream.md)) was in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/status/atend)*