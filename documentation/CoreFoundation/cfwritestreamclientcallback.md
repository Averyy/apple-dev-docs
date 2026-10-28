# CFWriteStreamClientCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback invoked when certain types of activity takes place on a writable stream.

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
typealias CFWriteStreamClientCallBack = (CFWriteStream?, CFStreamEventType, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct __CFWriteStream *, enum CFStreamEventType, void *) CFWriteStreamClientCallBack;
```

## Discussion

This callback is called only for the events requested when setting the client with [`CFWriteStreamSetClient(_:_:_:_:)`](./cfwritestreamsetclient%28_,_,_,_%29.md).

## Parameters

- `stream`: The stream that experienced the event `eventType`.
- `eventType`: The event that caused the callback to be called. The possible events are listed in [`CFStreamEventType`](./cfstreameventtype.md).
- `clientCallBackInfo`: The `info` member of the [`CFStreamClientContext`](./cfstreamclientcontext.md) structure that was used when setting the client for `stream`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamclientcallback)*