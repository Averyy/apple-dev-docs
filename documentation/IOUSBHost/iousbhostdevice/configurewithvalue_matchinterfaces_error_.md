# configureWithValue:matchInterfaces:error:

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Selects a new configuration for the device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```objc
- (BOOL) configureWithValue:(NSUInteger) value matchInterfaces:(BOOL) matchInterfaces error:(NSError **) error;
```

#### Return Value

`YES` if the request completes successfully; otherwise, `NO`.

## Parameters

- `value`: The configuration value to select.
- `matchInterfaces`: A Boolean to register the new interfaces for matching. If `YES`, any interfaces within the new configuration register for matching. The default value is `YES`.
- `error`: An [`NSError`](../../Foundation/nserror.md) that contains an [`IOReturn`](../../iokit/ioreturn.md) value on failure.

## See Also

### Configuring the Device
- [- configureWithValue:error:](./configurewithvalue_error_.md)
  Selects a new configuration for the device and registers the interfaces for matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice/configurewithvalue:matchinterfaces:error:)*