# inappropriateIOCTLForDevice

**Framework**: System  
**Kind**: property

Inappropriate control function.

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
static var inappropriateIOCTLForDevice: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

You attempted a control function that can’t be performed on the specified file or device. For information about control functions, see `ioctl(2)`.

The corresponding C error is `ENOTTY`.

## See Also

- [static var deviceError: Errno](errno/deviceerror.md)
  Device error.
- [static var devicePowerIsOff: Errno](errno/devicepowerisoff.md)
  Device power is off.
- [static var ioError: Errno](errno/ioerror.md)
  Input/output error.
- [static var noSuchAddressOrDevice: Errno](errno/nosuchaddressordevice.md)
  No such device or address.
- [static var notBlockDevice: Errno](errno/notblockdevice.md)
  Not a block device.
- [static var operationNotSupportedByDevice: Errno](errno/operationnotsupportedbydevice.md)
  Operation not supported by device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/inappropriateioctlfordevice)*