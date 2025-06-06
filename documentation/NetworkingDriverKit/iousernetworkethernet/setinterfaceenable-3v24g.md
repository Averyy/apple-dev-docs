# SetInterfaceEnable

**Framework**: NetworkingDriverKit  
**Kind**: method

Enables or disables your service.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t SetInterfaceEnable(bool isEnable);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Override this method and use it to start or stop the delivery of packets to and from the device. For example, change the enabled state of the queues you use to handle packets moving to or from the device.

## Parameters

- `isEnable`: A Boolean value that indicates whether to enable or disable your service. Specify   to enable the service or   to disable it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/setinterfaceenable-3v24g)*