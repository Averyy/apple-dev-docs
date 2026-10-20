# firmwareRevision

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

The current firmware version for the accessory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var firmwareRevision: String { get }
```

```objc
@property (nonatomic, readonly) NSString * firmwareRevision;
```

#### Discussion

The format of this string is determined by the accessory manufacturer.

## See Also

### Getting the Manufacturer-Supplied Attributes
- [var name: String](./name.md)
  The display name of the accessory.
- [var manufacturer: String](./manufacturer.md)
  The name of the accessory’s manufacturer.
- [var modelNumber: String](./modelnumber.md)
  The model information for the accessory.
- [var serialNumber: String](./serialnumber.md)
  The serial number of the accessory.
- [var hardwareRevision: String](./hardwarerevision.md)
  The hardware version of the accessory.
- [var protocolStrings: [String]](./protocolstrings.md)
  The communication protocols supported by the accessory.
- [var dockType: String](./docktype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/firmwarerevision)*