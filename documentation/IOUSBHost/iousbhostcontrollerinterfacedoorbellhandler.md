# IOUSBHostControllerInterfaceDoorbellHandler

**Framework**: IOUSBHost  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias IOUSBHostControllerInterfaceDoorbellHandler = (IOUSBHostControllerInterface, UnsafeMutablePointer<IOUSBHostCIDoorbell>, UInt32) -> Void
```

```c
typedef void (^)(IOUSBHostControllerInterface *, unsigned int *, unsigned int) IOUSBHostControllerInterfaceDoorbellHandler;
```

## See Also

### Data Types
- [typealias IOUSBHostCIDoorbell](./iousbhostcidoorbell.md)
- [typealias IOUSBHostCIPortStatus](./iousbhostciportstatus.md)
- [typealias IOUSBHostControllerInterfaceCommandHandler](./iousbhostcontrollerinterfacecommandhandler.md)
- [typealias IOUSBHostIsochronousTransactionCompletionHandler](./iousbhostisochronoustransactioncompletionhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterfacedoorbellhandler)*