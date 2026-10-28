# operationNotSupportedByDevice

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Operation not supported by device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var operationNotSupportedByDevice: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

You attempted to apply an inappropriate function to a device; for example, trying to read a write-only device such as a printer.

The corresponding C error is `ENODEV`.

## See Also

### Device Errors
- [static var deviceError: Errno](./deviceerror.md)
  Device error.
- [static var devicePowerIsOff: Errno](./devicepowerisoff.md)
  Device power is off.
- [static var inappropriateIOCTLForDevice: Errno](./inappropriateioctlfordevice.md)
  Inappropriate control function.
- [static var ioError: Errno](./ioerror.md)
  Input/output error.
- [static var noSuchAddressOrDevice: Errno](./nosuchaddressordevice.md)
  No such device or address.
- [static var notBlockDevice: Errno](./notblockdevice.md)
  Not a block device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/operationnotsupportedbydevice)*