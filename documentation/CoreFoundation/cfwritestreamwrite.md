# CFWriteStreamWrite(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Writes data to a writable stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFWriteStreamWrite(_ stream: CFWriteStream!, _ buffer: UnsafePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

#### Return Value

The number of bytes successfully written, `0` if the stream has been filled to capacity (for fixed-length streams), or `-1` if either the stream is not open or an error occurs.

#### Discussion

If `stream` is in the process of opening, this function waits until it has completed. If the stream is not full, this call blocks until at least one byte is written; it does not block until all the bytes in `buffer` is written. To avoid blocking, call this function only if [`CFWriteStreamCanAcceptBytes(_:)`](cfwritestreamcanacceptbytes(_:).md) returns `true` or after the stream’s client (set with [`CFWriteStreamSetClient(_:_:_:_:)`](cfwritestreamsetclient(_:_:_:_:).md)) is notified of a [`canAcceptBytes`](cfstreameventtype/canacceptbytes.md) event.

## Parameters

- `stream`: The stream to which to write.
- `buffer`: The buffer holding the data to write.
- `bufferLength`: The number of bytes from   to write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamwrite(_:_:_:))*