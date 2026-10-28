# ioError

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Input/output error.

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
static var ioError: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

Some physical input or output error occurred. This error isn’t reported until you attempt a subsequent operation on the same file descriptor, and the error may be lost (overwritten) by subsequent errors.

The corresponding C error is `EIO`.

## See Also

### Device Errors
- [static var deviceError: Errno](./deviceerror.md)
  Device error.
- [static var devicePowerIsOff: Errno](./devicepowerisoff.md)
  Device power is off.
- [static var inappropriateIOCTLForDevice: Errno](./inappropriateioctlfordevice.md)
  Inappropriate control function.
- [static var noSuchAddressOrDevice: Errno](./nosuchaddressordevice.md)
  No such device or address.
- [static var notBlockDevice: Errno](./notblockdevice.md)
  Not a block device.
- [static var operationNotSupportedByDevice: Errno](./operationnotsupportedbydevice.md)
  Operation not supported by device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/ioerror)*