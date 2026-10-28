# kIOHIDElementCollectionTypePhysical

**Framework**: HIDDriverKit  
**Kind**: case  
**Role**: Enumeration Case

A collection in which the child elements are data points collected at one geometric point.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
kIOHIDElementCollectionTypePhysical
```

## Discussion

A sensing device might associate sets of measured or sensed data with a single point. This type does not indicate that multiple data values come from the device.

## See Also

### Getting the Element Collection Types
- [kIOHIDElementCollectionTypeApplication](./kiohidelementcollectiontypeapplication.md)
  A collection in which the child elements serve different purposes in a single device.
- [kIOHIDElementCollectionTypeLogical](./kiohidelementcollectiontypelogical.md)
  A collection in which the child elements form a composite data structure.
- [kIOHIDElementCollectionTypeReport](./kiohidelementcollectiontypereport.md)
  A collection that wraps all the other elements in a report.
- [kIOHIDElementCollectionTypeNamedArray](./kiohidelementcollectiontypenamedarray.md)
  A collection in which the elements are an array of selector usages.
- [kIOHIDElementCollectionTypeUsageSwitch](./kiohidelementcollectiontypeusageswitch.md)
  A collection that modifies the meaning of the usage it contains.
- [kIOHIDElementCollectionTypeUsageModifier](./kiohidelementcollectiontypeusagemodifier.md)
  A collection that modifies the meaning of the usage attached to the encompassing collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelementcollectiontype/kiohidelementcollectiontypephysical)*