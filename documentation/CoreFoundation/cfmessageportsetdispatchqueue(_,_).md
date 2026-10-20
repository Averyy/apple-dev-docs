# CFMessagePortSetDispatchQueue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Schedules callbacks for the specified message port on the specified dispatch queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFMessagePortSetDispatchQueue(_ ms: CFMessagePort!, _ queue: dispatch_queue_t!)
```

```c
extern void CFMessagePortSetDispatchQueue(CFMessagePortRef ms, dispatch_queue_t queue);
```

## Parameters

- `ms`: The message port to schedule.
- `queue`: The libdispatch queue.

## See Also

### Using a Message Port
- [func CFMessagePortInvalidate(CFMessagePort!)](./cfmessageportinvalidate%28_%29.md)
  Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [func CFMessagePortSendRequest(CFMessagePort!, Int32, CFData!, CFTimeInterval, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32](./cfmessageportsendrequest%28_,_,_,_,_,_,_%29.md)
  Sends a message to a remote CFMessagePort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportsetdispatchqueue(_:_:))*