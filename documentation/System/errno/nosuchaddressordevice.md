# noSuchAddressOrDevice

**Framework**: System  
**Kind**: property

No such device or address.

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
static var noSuchAddressOrDevice: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

Input or output on a special file referred to a device that didn’t exist, or made a request beyond the limits of the device. This error may also occur when, for example, a tape drive isn’t online or when there isn’t a disk pack loaded on a drive.

The corresponding C error is `ENXIO`.

## See Also

- [static var deviceError: Errno](errno/deviceerror.md)
  Device error.
- [static var devicePowerIsOff: Errno](errno/devicepowerisoff.md)
  Device power is off.
- [static var inappropriateIOCTLForDevice: Errno](errno/inappropriateioctlfordevice.md)
  Inappropriate control function.
- [static var ioError: Errno](errno/ioerror.md)
  Input/output error.
- [static var notBlockDevice: Errno](errno/notblockdevice.md)
  Not a block device.
- [static var operationNotSupportedByDevice: Errno](errno/operationnotsupportedbydevice.md)
  Operation not supported by device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nosuchaddressordevice)*