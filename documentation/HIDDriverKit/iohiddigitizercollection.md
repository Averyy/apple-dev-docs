# IOHIDDigitizerCollection

**Framework**: HIDDriverKit  
**Kind**: class

A collection of elements that contain digitizer-related data.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOHIDDigitizerCollection;
```

## Topics

### Creating a Digitizer Collection
- [withType](iohiddigitizercollection/withtype.md)
- [initWithType](iohiddigitizercollection/initwithtype.md)
- [free](iohiddigitizercollection/free.md)
- [IOHIDDigitizerCollectionType](iohiddigitizercollectiontype.md)
### Accessing the Coordinates
- [getX](iohiddigitizercollection/getx.md)
- [getY](iohiddigitizercollection/gety.md)
- [getZ](iohiddigitizercollection/getz.md)
- [setX](iohiddigitizercollection/setx.md)
- [setY](iohiddigitizercollection/sety.md)
- [setZ](iohiddigitizercollection/setz.md)
### Managing the Collection Elements
- [getParentCollection](iohiddigitizercollection/getparentcollection.md)
- [addElement](iohiddigitizercollection/addelement.md)
- [getElements](iohiddigitizercollection/getelements.md)
### Accessing Touch Data
- [getTouch](iohiddigitizercollection/gettouch.md)
- [setTouch](iohiddigitizercollection/settouch.md)
### Getting the Collection Attributes
- [getType](iohiddigitizercollection/gettype.md)
- [getInRange](iohiddigitizercollection/getinrange.md)
- [setInRange](iohiddigitizercollection/setinrange.md)

## Relationships

### Inherits From
- [OSContainer](../DriverKit/OSContainer.md)

## See Also

- [IOHIDElement](iohidelement.md)
  An object that contains parsed information from a HID input report.
- [com.apple.developer.hid.virtual.device](../BundleResources/Entitlements/com.apple.developer.hid.virtual.device.md)
  A Boolean value that indicates whether the driver creates a virtual HID device.
- [Low-Level Information](low-level-information.md)
  Understand the underlying structures that support HID drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizercollection)*