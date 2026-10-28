# CFWriteStreamOpen(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Opens a stream for writing.

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
func CFWriteStreamOpen(_ stream: CFWriteStream!) -> Bool
```

```c
extern Boolean CFWriteStreamOpen(CFWriteStreamRef stream);
```

## Return Value

`true` if `stream` was successfully opened, `false` otherwise. If `stream` is not in the [`CFStreamStatus.notOpen`](./cfstreamstatus/notopen.md) state, this function returns `false`.

## Discussion

Opening a stream causes it to reserve all the system resources it requires. If the stream can open in the background without blocking, this function always returns `true`. To learn when a background open operation completes, you can either schedule the stream into a run loop with [`CFWriteStreamScheduleWithRunLoop(_:_:_:)`](./cfwritestreamschedulewithrunloop%28_,_,_%29.md) and wait for the stream’s client (set with [`CFWriteStreamSetClient(_:_:_:_:)`](./cfwritestreamsetclient%28_,_,_,_%29.md)) to be notified or you can poll the stream using [`CFWriteStreamGetStatus(_:)`](./cfwritestreamgetstatus%28_%29.md), waiting for a status of [`CFStreamStatus.open`](./cfstreamstatus/open.md) or [`CFStreamStatus.error`](./cfstreamstatus/error.md).

## Parameters

- `stream`: The stream to open.

## See Also

### Opening and Closing a Stream
- [func CFWriteStreamClose(CFWriteStream!)](./cfwritestreamclose%28_%29.md)
  Closes a writable stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamopen(_:))*