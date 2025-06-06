# CFWriteStreamClientCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when certain types of activity takes place on a writable stream.

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
typealias CFWriteStreamClientCallBack = (CFWriteStream?, CFStreamEventType, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

This callback is called only for the events requested when setting the client with [`CFWriteStreamSetClient(_:_:_:_:)`](cfwritestreamsetclient(_:_:_:_:).md).

## Parameters

- `stream`: The stream that experienced the event  .
- `eventType`: The event that caused the callback to be called. The possible events are listed in  .
- `clientCallBackInfo`: The   member of the   structure that was used when setting the client for  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamclientcallback)*