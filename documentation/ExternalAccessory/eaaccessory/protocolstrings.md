# protocolStrings

**Framework**: External Accessory  
**Kind**: property

The communication protocols supported by the accessory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var protocolStrings: [String] { get }
```

#### Discussion

Protocol names are formatted as reverse-DNS strings. For example, the string “`com.apple.myProtocol`” might represent a custom protocol defined by Apple. Manufacturers can define custom protocols for their accessories or work with other manufacturers and organizations to define standard protocols for different accessory types.

When encountering a new accessory, always check the list of supported protocols for the one you expect to use before creating a session. Even an accessory that you recognize by its other properties may not be prepared to support a protocol that it normally does. For example, an accessory may be connected but not yet authenticated, in which case the array of supported protocols will be empty.

If your application supports multiple protocols for a single accessory, your code should always choose the highest-fidelity protocol that you support.

## See Also

- [var name: String](eaaccessory/name.md)
  The display name of the accessory.
- [var manufacturer: String](eaaccessory/manufacturer.md)
  The name of the accessory’s manufacturer.
- [var modelNumber: String](eaaccessory/modelnumber.md)
  The model information for the accessory.
- [var serialNumber: String](eaaccessory/serialnumber.md)
  The serial number of the accessory.
- [var firmwareRevision: String](eaaccessory/firmwarerevision.md)
  The current firmware version for the accessory.
- [var hardwareRevision: String](eaaccessory/hardwarerevision.md)
  The hardware version of the accessory.
- [var dockType: String](eaaccessory/docktype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/protocolstrings)*