# CFReadStreamClientCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback invoked when certain types of activity takes place on a readable stream.

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
typealias CFReadStreamClientCallBack = (CFReadStream?, CFStreamEventType, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct __CFReadStream *, enum CFStreamEventType, void *) CFReadStreamClientCallBack;
```

#### Discussion

This callback is called only for the events requested when setting the client with [`CFReadStreamSetClient(_:_:_:_:)`](./cfreadstreamsetclient%28_,_,_,_%29.md).

## Parameters

- `stream`: The stream that experienced the event `eventType`.
- `eventType`: The event that caused the callback to be called. The possible events are listed in [`CFStreamEventType`](./cfstreameventtype.md).
- `clientCallBackInfo`: The `info` member of the [`CFStreamClientContext`](./cfstreamclientcontext.md) structure that was used when setting the client for `stream`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamclientcallback)*