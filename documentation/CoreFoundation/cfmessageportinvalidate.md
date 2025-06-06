# CFMessagePortInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func

Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.

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
func CFMessagePortInvalidate(_ ms: CFMessagePort!)
```

#### Discussion

Invalidating a message port prevents the port from ever sending or receiving any more messages; the message port is not deallocated, though. If the port has not already been invalidated, the port’s invalidation callback function is invoked, if one has been set with [`CFMessagePortSetInvalidationCallBack(_:_:)`](cfmessageportsetinvalidationcallback(_:_:).md). The [`CFMessagePortContext`](cfmessageportcontext.md)  `info` information for `ms` is also released, if a release callback was specified in the port’s context structure. Finally, if a run loop source was created for `ms`, the run loop source is also invalidated.

## Parameters

- `ms`: The message port to invalidate.

## See Also

- [func CFMessagePortSendRequest(CFMessagePort!, Int32, CFData!, CFTimeInterval, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32](cfmessageportsendrequest(_:_:_:_:_:_:_:).md)
  Sends a message to a remote CFMessagePort object.
- [func CFMessagePortSetDispatchQueue(CFMessagePort!, dispatch_queue_t!)](cfmessageportsetdispatchqueue(_:_:).md)
  Schedules callbacks for the specified message port on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportinvalidate(_:))*