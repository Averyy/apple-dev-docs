# registerPort:name:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers a port with a specified name.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name;
```

#### Return Value

[`true`](../../Swift/true.md) if the registration succeeded, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Once registered, a port cannot be unregistered; instead, you need to invalidate the port.

## Parameters

- `port`: The port object to register with the bootstrap server.
- `name`: The name to associate with `port`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/registerport:name:)*