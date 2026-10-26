# portForName:host:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port registered under the specified name on a specified host.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

#### Return Value

The port associated with `name` on the host `host`. Returns `nil` if no such port exists.

## Parameters

- `name`: The name of the desired port.
- `host`: The name of the host. `host` is an Internet domain name (for example, “`sales.anycorp.com`”). If `host` is `nil` or empty, the local host is checked.

## See Also

### Looking up Ports
- [- portForName:](./portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportnameserver/portforname:host:)*