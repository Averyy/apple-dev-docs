# portForName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port registered under the specified name on the local host.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name;
```

## Return Value

The port associated with `portName` on the local host. Returns `nil` if no such port exists.

## Discussion

Invokes [`portForName:host:nameServerPortNumber:`](./portforname_host_nameserverportnumber_.md) with `nil` as the host name and 0 as the name server port number.

## Parameters

- `name`: The name of the desired port.

## See Also

### Looking up Ports
- [- portForName:host:](./portforname_host_.md)
  Looks up and returns the port registered under the specified name on a specified host.
- [- portForName:host:nameServerPortNumber:](./portforname_host_nameserverportnumber_.md)
  Looks up and returns the port registered under the specified name on a specified host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver/portforname:)*