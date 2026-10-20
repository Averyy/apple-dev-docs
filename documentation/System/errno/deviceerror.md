# deviceError

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Device error.

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
static var deviceError: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

A device error has occurred; for example, a printer running out of paper.

The corresponding C error is `EDEVERR`.

## See Also

### Device Errors
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
- [static var operationNotSupportedByDevice: Errno](./operationnotsupportedbydevice.md)
  Operation not supported by device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/deviceerror)*