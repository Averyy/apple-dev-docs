# DispatchSourceProtocol.DispatchSourceHandler

**Framework**: Dispatch  
**Kind**: typealias

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
typealias DispatchSourceHandler = () -> Void
```

## See Also

- [func setEventHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/seteventhandler(handler:).md)
  Sets the event handler work item for the dispatch source.
- [func setEventHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/seteventhandler(qos:flags:handler:).md)
- [func setRegistrationHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setregistrationhandler(handler:).md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/setregistrationhandler(qos:flags:handler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/dispatchsourcehandler)*