# registerPort:name:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Makes a given port available on the network under a specified name.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, [`false`](../../Swift/false.md) otherwise (for example, if another `NSPort` object  has already been registered under `name`).

#### Discussion

A port can be registered under multiple names. If it is, it must be unregistered for each name with [`removePortForName:`](./removeportforname_.md) to make it completely unavailable.

## Parameters

- `port`: The port to make available.
- `name`: The name for the port.

## See Also

### Registering Ports
- [- removePortForName:](./removeportforname_.md)
  Unregisters the port for a given name on the local host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportnameserver/registerport:name:)*