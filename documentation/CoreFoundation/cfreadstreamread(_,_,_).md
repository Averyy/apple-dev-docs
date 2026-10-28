# CFReadStreamRead(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Reads data from a readable stream.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFReadStreamRead(_ stream: CFReadStream!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

```c
extern CFIndex CFReadStreamRead(CFReadStreamRef stream, UInt8 *buffer, CFIndex bufferLength);
```

## Return Value

The number of bytes read; `0` if the stream has reached its end; or `-1` if either the stream is not open or an error occurs.

## Discussion

If `stream` is in the process of opening, this function waits until it has completed. This function blocks until at least one byte is available; it does not block until `buffer` is filled. To avoid blocking, call this function only if [`CFReadStreamHasBytesAvailable(_:)`](./cfreadstreamhasbytesavailable%28_%29.md) returns `TRUE` or after the stream’s client (set with [`CFReadStreamSetClient(_:_:_:_:)`](./cfreadstreamsetclient%28_,_,_,_%29.md)) is notified of a [`hasBytesAvailable`](./cfstreameventtype/hasbytesavailable.md) event.

## Parameters

- `stream`: The stream from which to read.
- `buffer`: The buffer into which to place the data.
- `bufferLength`: The size of `buffer` and the maximum number of bytes to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamread(_:_:_:))*