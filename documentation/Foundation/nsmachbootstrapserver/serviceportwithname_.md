# servicePortWithName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port for the vended service that is registered under the specified name.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.13

## Declaration

```objc
- (NSPort *) servicePortWithName:(NSString *) name;
```

## Return Value

The port associated with `name`. Returns `nil` if no such port exists.

## Parameters

- `name`: The name of the vended service.

## See Also

### Looking up Ports
- [- portForName:](./portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- portForName:host:](./portforname_host_.md)
  Looks up and returns the port registered under the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/serviceportwithname:)*