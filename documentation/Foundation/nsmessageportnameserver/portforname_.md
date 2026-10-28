# portForName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the `NSPort` object registered under a given name on the local host.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name;
```

## Return Value

The NSPort registered under `portName` on the local host Returns `nil` if a port named `portName` does not exist.

## Parameters

- `name`: The port name.

## See Also

### Getting Ports By Name
- [- portForName:host:](./portforname_host_.md)
  Returns the `NSPort` object registered under a given name on the local host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmessageportnameserver/portforname:)*