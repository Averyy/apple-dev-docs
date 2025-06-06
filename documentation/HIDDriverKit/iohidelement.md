# IOHIDElement

**Framework**: HIDDriverKit  
**Kind**: class

An object that contains parsed information from a HID input report.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
class IOHIDElement;
```

#### Overview

An `IOHIDElement` object contains details about a particular aspect of a HID-related input report. After receiving an input report from a HID device, `IOUserHIDEventService` and `IOHIDInterface` objects divide the report details into `IOHIDElement` objects for easier management. You use these element objects to obtain details about the report, such as the current value reported by the device, how that value is meant to be used, and the minimum and maximum values. For example, a report from a mouse usually contains separate elements for the mouse’s x and y positions.

You don’t create `IOHIDElement` objects directly. Instead, use the `getElements` method of your [`IOUserHIDEventService`](iouserhideventservice.md) or [`IOHIDInterface`](iohidinterface.md) object to fetch the elements associated with the latest report. Each time you call that method, the corresponding object updates the element data using the most recent report.

## Topics

### Getting an Element’s Usage Information
- [getUsagePage](iohidelement/getusagepage.md)
- [getUsage](iohidelement/getusage.md)
### Accessing the Element’s Value
- [getValue](iohidelement/getvalue.md)
  Gets the logical value that the device reported.
- [getDataValue](iohidelement/getdatavalue.md)
  Gets the data value.
- [getScaledValue](iohidelement/getscaledvalue.md)
  Returns a scaled version of the logical value.
- [getScaledFixedValue](iohidelement/getscaledfixedvalue.md)
  Returns a fixed number that represents the scaled version of the element’s logical value.
- [setValue](iohidelement/setvalue.md)
  Sets the value of the element.
- [setDataValue](iohidelement/setdatavalue.md)
  Sets the data value of the element.
- [getUnit](iohidelement/getunit.md)
  Returns the units that you use to interpret the element’s value.
- [getUnitExponent](iohidelement/getunitexponent.md)
  Returns the exponent that you use to interpret the element’s value.
- [IOHIDValueOptions](iohidvalueoptions.md)
  A type for specifying value-related options.
- [Value Options](value-options-enum.md)
  Options for how to retrieve an element’s values.
- [IOHIDValueScaleType](iohidvaluescaletype.md)
  The type of scaling to use for an element’s value.
- [Value Scale Types](value-scale-types-enum.md)
  The different types of scaling that you can perform on element values.
### Getting Minimum and Maximum Values
- [getLogicalMin](iohidelement/getlogicalmin.md)
- [getLogicalMax](iohidelement/getlogicalmax.md)
- [getPhysicalMin](iohidelement/getphysicalmin.md)
- [getPhysicalMax](iohidelement/getphysicalmax.md)
### Getting the Element’s Timestamp
- [getTimeStamp](iohidelement/gettimestamp.md)
### Managing the Element Hierarchy
- [getType](iohidelement/gettype.md)
- [getCollectionType](iohidelement/getcollectiontype.md)
- [getChildElements](iohidelement/getchildelements.md)
- [getParentElement](iohidelement/getparentelement.md)
- [IOHIDElementType](iohidelementtype.md)
  The types of HID elements that you can examine.
- [IOHIDElementCollectionType](iohidelementcollectiontype.md)
  Constants that indicate the types of relationships that exist between two or more elements.
### Getting Report Information
- [getReportID](iohidelement/getreportid.md)
- [getReportCount](iohidelement/getreportcount.md)
- [getReportSize](iohidelement/getreportsize.md)
- [IOHIDReportType](iohidreporttype.md)
  Describes the different types of HID reports.
### Identifying the Element
- [getCookie](iohidelement/getcookie.md)
- [IOHIDElementCookie](iohidelementcookie.md)
  A type that an element uses to distinguish itself from other elements.
### Getting the Element Flags
- [getFlags](iohidelement/getflags.md)
- [IOHIDElementFlags](iohidelementflags.md)
- [HID Element Flags](hid-element-flags-enum.md)
### Committing Changes to Elements
- [commit](iohidelement/commit.md)
  Commits the element value to and from the device.
- [IOHIDElementCommitDirection](iohidelementcommitdirection.md)
  The commit direction for an HID element.
### Instance Methods
- [conformsTo](iohidelement/conformsto.md)

## Relationships

### Inherits From
- [OSContainer](../DriverKit/OSContainer.md)

## See Also

- [IOHIDDigitizerCollection](iohiddigitizercollection.md)
  A collection of elements that contain digitizer-related data.
- [com.apple.developer.hid.virtual.device](../BundleResources/Entitlements/com.apple.developer.hid.virtual.device.md)
  A Boolean value that indicates whether the driver creates a virtual HID device.
- [Low-Level Information](low-level-information.md)
  Understand the underlying structures that support HID drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement)*