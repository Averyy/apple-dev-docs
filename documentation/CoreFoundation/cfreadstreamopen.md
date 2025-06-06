# CFReadStreamOpen(_:)

**Framework**: Core Foundation  
**Kind**: func

Opens a stream for reading.

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
func CFReadStreamOpen(_ stream: CFReadStream!) -> Bool
```

#### Return Value

`TRUE` if `stream` was successfully opened, `FALSE` otherwise. If `stream` is not in the [`CFStreamStatus.notOpen`](cfstreamstatus/notopen.md) state, this function returns `FALSE`.

#### Discussion

Opening a stream causes it to reserve all the system resources it requires. If the stream can open in the background without blocking, this function always returns `true`. To learn when a background open operation completes, you can either schedule the stream into a run loop with [`CFReadStreamScheduleWithRunLoop(_:_:_:)`](cfreadstreamschedulewithrunloop(_:_:_:).md) and wait for the stream’s client (set with [`CFReadStreamSetClient(_:_:_:_:)`](cfreadstreamsetclient(_:_:_:_:).md)) to be notified or you can poll the stream using [`CFReadStreamGetStatus(_:)`](cfreadstreamgetstatus(_:).md), waiting for a status of [`CFStreamStatus.open`](cfstreamstatus/open.md) or [`CFStreamStatus.error`](cfstreamstatus/error.md).

You do not need to wait until a stream has finished opening in the background before calling the [`CFReadStreamRead(_:_:_:)`](cfreadstreamread(_:_:_:).md) function. The read operation will simply block until the open has completed.

## Parameters

- `stream`: The stream to open.

## See Also

- [func CFReadStreamClose(CFReadStream!)](cfreadstreamclose(_:).md)
  Closes a readable stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamopen(_:))*