# setEventHandler(qos:flags:handler:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

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
func setEventHandler(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], handler: Self.DispatchSourceHandler?)
```

## See Also

### Installing Event Handlers
- [func setEventHandler(handler: DispatchWorkItem)](./seteventhandler%28handler%29.md)
  Sets the event handler work item for the dispatch source.
- [func setRegistrationHandler(handler: DispatchWorkItem)](./setregistrationhandler%28handler%29.md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](./setregistrationhandler%28qos,flags,handler%29.md)
- [DispatchSourceProtocol.DispatchSourceHandler](./dispatchsourcehandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/seteventhandler(qos:flags:handler:))*