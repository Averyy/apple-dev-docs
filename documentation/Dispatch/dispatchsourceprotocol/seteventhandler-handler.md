# setEventHandler(handler:)

**Framework**: Dispatch  
**Kind**: method

Sets the event handler work item for the dispatch source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func setEventHandler(handler: DispatchWorkItem)
```

#### Discussion

The event handler (if specified) is submitted to the source’s target queue in response to the arrival of an event.

## Parameters

- `handler`: The event handler block to submit to the source’s target queue.

## See Also

- [func setEventHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/seteventhandler(qos:flags:handler:).md)
- [func setRegistrationHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setregistrationhandler(handler:).md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/setregistrationhandler(qos:flags:handler:).md)
- [DispatchSourceProtocol.DispatchSourceHandler](dispatchsourceprotocol/dispatchsourcehandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/seteventhandler(handler:))*