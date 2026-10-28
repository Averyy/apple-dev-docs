# configureWithValue:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Selects a new configuration for the device and registers the interfaces for matching.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) configureWithValue:(NSUInteger) value error:(NSError **) error;
```

## Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Parameters

- `value`: A configuration value to select.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../kernel/ioreturn.md) value on failure.

## See Also

### Configuring the Device
- [- configureWithValue:matchInterfaces:error:](./configurewithvalue_matchinterfaces_error_.md)
  Selects a new configuration for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/configurewithvalue:error:)*