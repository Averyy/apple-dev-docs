# IOUSBHostIsochronousTransactionCompletionHandler

**Framework**: IOUSBHost  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostIsochronousTransactionCompletionHandler = (IOReturn, UnsafeMutablePointer<IOUSBHostIsochronousTransaction>) -> Void
```

```c
typedef void (^)(int, struct IOUSBHostIsochronousTransaction *) IOUSBHostIsochronousTransactionCompletionHandler;
```

## See Also

### Data Types
- [typealias IOUSBHostCIDoorbell](./iousbhostcidoorbell.md)
- [typealias IOUSBHostCIPortStatus](./iousbhostciportstatus.md)
- [typealias IOUSBHostControllerInterfaceCommandHandler](./iousbhostcontrollerinterfacecommandhandler.md)
- [typealias IOUSBHostControllerInterfaceDoorbellHandler](./iousbhostcontrollerinterfacedoorbellhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostisochronoustransactioncompletionhandler)*