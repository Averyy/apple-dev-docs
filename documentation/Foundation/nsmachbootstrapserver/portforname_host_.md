# portForName:host:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port registered under the specified name.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

#### Return Value

The port associated with `portName` on the local host. Returns `nil` if no such port exists.

## Parameters

- `name`: The name of the desired port.
- `host`: Because `NSMachBootstrapServer` is a local-only server; `hostName` must be the empty string or `nil`.

## See Also

### Looking up Ports
- [- portForName:](./portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- servicePortWithName:](./serviceportwithname_.md)
  Looks up and returns the port for the vended service that is registered under the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/portforname:host:)*