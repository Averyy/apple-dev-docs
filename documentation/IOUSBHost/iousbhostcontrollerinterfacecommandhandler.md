# IOUSBHostControllerInterfaceCommandHandler

**Framework**: IOUSBHost  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostControllerInterfaceCommandHandler = (IOUSBHostControllerInterface, IOUSBHostCIMessage) -> Void
```

```c
typedef void (^)(IOUSBHostControllerInterface *, struct IOUSBHostCIMessage) IOUSBHostControllerInterfaceCommandHandler;
```

## See Also

### Data Types
- [typealias IOUSBHostCIDoorbell](./iousbhostcidoorbell.md)
- [typealias IOUSBHostCIPortStatus](./iousbhostciportstatus.md)
- [typealias IOUSBHostControllerInterfaceDoorbellHandler](./iousbhostcontrollerinterfacedoorbellhandler.md)
- [typealias IOUSBHostIsochronousTransactionCompletionHandler](./iousbhostisochronoustransactioncompletionhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterfacecommandhandler)*