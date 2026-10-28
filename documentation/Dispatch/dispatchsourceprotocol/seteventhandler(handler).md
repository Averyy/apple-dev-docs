# setEventHandler(handler:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Sets the event handler work item for the dispatch source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func setEventHandler(handler: DispatchWorkItem)
```

## Discussion

The event handler (if specified) is submitted to the source’s target queue in response to the arrival of an event.

## Parameters

- `handler`: The event handler block to submit to the source’s target queue.

## See Also

### Installing Event Handlers
- [func setEventHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./seteventhandler%28qos,flags,handler%29.md)
- [func setRegistrationHandler(handler: DispatchWorkItem)](./setregistrationhandler%28handler%29.md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./setregistrationhandler%28qos,flags,handler%29.md)
- [DispatchSourceProtocol.DispatchSourceHandler](./dispatchsourcehandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/seteventhandler(handler:))*