# SCNetworkConnectionCreateWithServiceID(_:_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Creates a new connection reference to use for getting the status or for connecting or disconnecting the associated service.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionCreateWithServiceID(_ allocator: CFAllocator?, _ serviceID: CFString, _ callout: SCNetworkConnectionCallBack?, _ context: UnsafeMutablePointer<SCNetworkConnectionContext>?) -> SCNetworkConnection?
```

#### Return Value

A reference to a new network connection.

## Parameters

- `allocator`: The allocator that should be used to allocate memory for the connection structure. This parameter may be  , in which case the current default allocator is used. If this reference is not a valid allocator, the behavior is undefined.
- `serviceID`: The service identifier of the connection. This value uniquely identifies service in the system configuration database.
- `callout`: The function to be called when the status of the connection changes. If this parameter is  , the application receives notifications of status change and will need to poll for updates.
- `context`: User-specified data associated with the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncreatewithserviceid(_:_:_:_:))*