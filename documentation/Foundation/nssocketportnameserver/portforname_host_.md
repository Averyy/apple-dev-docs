# portForName:host:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port registered under the specified name on a specified host.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

#### Return Value

The port associated with `portName` on the host `hostName`. Returns `nil` if no such port exists.

#### Discussion

Invokes [`portForName:host:nameServerPortNumber:`](./portforname_host_nameserverportnumber_.md) with 0 as the name server port number.

## Parameters

- `name`: The name of the desired port.
- `host`: The name of the host. `hostName` is an Internet domain name (for example, “`sales.anycorp.com`”). If `hostName` is `nil` or empty, the local host is checked.

## See Also

### Looking up Ports
- [- portForName:](./portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- portForName:host:nameServerPortNumber:](./portforname_host_nameserverportnumber_.md)
  Looks up and returns the port registered under the specified name on a specified host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver/portforname:host:)*