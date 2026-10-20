# DispatchSourceProtocol.DispatchSourceHandler

**Framework**: Dispatch  
**Kind**: typealias  
**Role**: Type Alias

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
typealias DispatchSourceHandler = () -> Void
```

## See Also

### Installing Event Handlers
- [func setEventHandler(handler: DispatchWorkItem)](./seteventhandler%28handler%29.md)
  Sets the event handler work item for the dispatch source.
- [func setEventHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./seteventhandler%28qos,flags,handler%29.md)
- [func setRegistrationHandler(handler: DispatchWorkItem)](./setregistrationhandler%28handler%29.md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./setregistrationhandler%28qos,flags,handler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/dispatchsourcehandler)*