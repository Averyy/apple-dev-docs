# portForName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port registered under the specified name on the local host.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name;
```

## Return Value

The port associated with `portName` on the local host. Returns `nil` if no such port exists.

## Discussion

Invokes [`portForName:host:`](./portforname_host_.md) with `nil` as the host name.

## Parameters

- `name`: The name of the desired port.

## See Also

### Looking up Ports
- [- portForName:host:](./portforname_host_.md)
  Looks up and returns the port registered under the specified name on a specified host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportnameserver/portforname:)*