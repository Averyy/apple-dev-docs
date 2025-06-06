# setEventHandler(qos:flags:handler:)

**Framework**: Dispatch  
**Kind**: method

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
func setEventHandler(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], handler: Self.DispatchSourceHandler?)
```

## See Also

- [func setEventHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/seteventhandler(handler:).md)
  Sets the event handler work item for the dispatch source.
- [func setRegistrationHandler(handler: DispatchWorkItem)](dispatchsourceprotocol/setregistrationhandler(handler:).md)
  Sets the registration handler work item for the dispatch source.
- [func setRegistrationHandler(qos: DispatchQoS, flags: DispatchWorkItemFlags, handler: Self.DispatchSourceHandler?)](dispatchsourceprotocol/setregistrationhandler(qos:flags:handler:).md)
- [DispatchSourceProtocol.DispatchSourceHandler](dispatchsourceprotocol/dispatchsourcehandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/seteventhandler(qos:flags:handler:))*