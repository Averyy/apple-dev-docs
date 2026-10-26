# removePortForName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Unregisters the port for a given name on the local host.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) removePortForName:(NSString *) name;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, otherwise [`false`](../../Swift/false.md).

#### Discussion

If the operation is successful, the port can no longer be looked up using the name `name`. Other applications that already have a reference to the port can continue to use it until it becomes invalid.

## Parameters

- `name`: The name of the port to unregister.

## See Also

### Registering Ports
- [- registerPort:name:](./registerport_name_.md)
  Makes a given port available on the network under a specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportnameserver/removeportforname:)*