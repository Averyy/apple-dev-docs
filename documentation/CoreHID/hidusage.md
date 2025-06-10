# HIDUsage

**Framework**: Core HID  
**Kind**: enum

A type to represent HID usage pages.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum HIDUsage
```

#### Overview

A HID usage page combines with a HID usage to specify the intended functionality for the associated item. Associated items can be descriptors, devices, reports, report data, elements, etc..

Currently unsupported cases can be used as [`HIDUsage.generic(_:_:)`](hidusage/generic(_:_:).md), but may be added as supported cases later.

For more details, see [`Human Interface Devices (HID) Specifications and Tools`](https://developer.apple.comhttps://www.usb.org/hid).

## Topics

### Operators
- [static func == (HIDUsage, HIDUsage) -> Bool](hidusage/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [case arcade(HIDUsage.ArcadeUsage?)](hidusage/arcade(_:).md)
- [case auxiliaryDisplay(HIDUsage.AuxiliaryDisplayUsage?)](hidusage/auxiliarydisplay(_:).md)
- [case barcodeScanner(HIDUsage.BarcodeScannerUsage?)](hidusage/barcodescanner(_:).md)
- [case batterySystem(HIDUsage.BatterySystemUsage?)](hidusage/batterysystem(_:).md)
- [case brailleDisplay(HIDUsage.BrailleDisplayUsage?)](hidusage/brailledisplay(_:).md)
- [case button(UInt16?)](hidusage/button(_:).md)
- [case cameraControl(HIDUsage.CameraControlUsage?)](hidusage/cameracontrol(_:).md)
- [case consumer(HIDUsage.ConsumerUsage?)](hidusage/consumer(_:).md)
- [case digitizers(HIDUsage.DigitizersUsage?)](hidusage/digitizers(_:).md)
- [case eyeAndHeadTrackers(HIDUsage.EyeAndHeadTrackersUsage?)](hidusage/eyeandheadtrackers(_:).md)
- [case fidoAlliance(HIDUsage.FIDOAllianceUsage?)](hidusage/fidoalliance(_:).md)
- [case gameControls(HIDUsage.GameControlsUsage?)](hidusage/gamecontrols(_:).md)
- [case generic(UInt16, UInt16?)](hidusage/generic(_:_:).md)
- [case genericDesktop(HIDUsage.GenericDesktopUsage?)](hidusage/genericdesktop(_:).md)
- [case genericDeviceControls(HIDUsage.GenericDeviceControlsUsage?)](hidusage/genericdevicecontrols(_:).md)
- [case haptics(HIDUsage.HapticsUsage?)](hidusage/haptics(_:).md)
- [case keyboardOrKeypad(HIDUsage.KeyboardOrKeypadUsage?)](hidusage/keyboardorkeypad(_:).md)
- [case led(HIDUsage.LEDUsage?)](hidusage/led(_:).md)
- [case lightingAndIllumination(HIDUsage.LightingAndIlluminationUsage?)](hidusage/lightingandillumination(_:).md)
- [case magneticStripeReader(HIDUsage.MagneticStripeReaderUsage?)](hidusage/magneticstripereader(_:).md)
- [case medicalInstrument(HIDUsage.MedicalInstrumentUsage?)](hidusage/medicalinstrument(_:).md)
- [case monitor(HIDUsage.MonitorUsage?)](hidusage/monitor(_:).md)
- [case monitorEnumerated(UInt16?)](hidusage/monitorenumerated(_:).md)
- [case ordinal(UInt16?)](hidusage/ordinal(_:).md)
- [case physicalInputDevice(HIDUsage.PhysicalInputDeviceUsage?)](hidusage/physicalinputdevice(_:).md)
- [case power(HIDUsage.PowerUsage?)](hidusage/power(_:).md)
- [case scales(HIDUsage.ScalesUsage?)](hidusage/scales(_:).md)
- [case sensors(HIDUsage.SensorsUsage?)](hidusage/sensors(_:).md)
- [case simulationControls(HIDUsage.SimulationControlsUsage?)](hidusage/simulationcontrols(_:).md)
- [case soc(HIDUsage.SOCUsage?)](hidusage/soc(_:).md)
- [case sportControls(HIDUsage.SportControlsUsage?)](hidusage/sportcontrols(_:).md)
- [case telephonyDevice(HIDUsage.TelephonyDeviceUsage?)](hidusage/telephonydevice(_:).md)
- [case vesaVirtualControls(HIDUsage.VESAVirtualControlsUsage?)](hidusage/vesavirtualcontrols(_:).md)
- [case vrControls(HIDUsage.VRControlsUsage?)](hidusage/vrcontrols(_:).md)
### Initializers
- [init(page: UInt16, usage: UInt16?)](hidusage/init(page:usage:).md)
  Creates a HID usage page from raw page and usage values.
### Instance Properties
- [var hashValue: Int](hidusage/hashvalue.md)
  The hash value.
- [var page: UInt16](hidusage/page.md)
  The usage page value.
- [var usage: UInt16?](hidusage/usage.md)
  The usage value.
### Instance Methods
- [func hash(into: inout Hasher)](hidusage/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [HIDUsage.ArcadeUsage](hidusage/arcadeusage.md)
- [HIDUsage.AuxiliaryDisplayUsage](hidusage/auxiliarydisplayusage.md)
- [HIDUsage.BarcodeScannerUsage](hidusage/barcodescannerusage.md)
- [HIDUsage.BatterySystemUsage](hidusage/batterysystemusage.md)
- [HIDUsage.BrailleDisplayUsage](hidusage/brailledisplayusage.md)
- [HIDUsage.ButtonUsage](hidusage/buttonusage.md)
- [HIDUsage.CameraControlUsage](hidusage/cameracontrolusage.md)
- [HIDUsage.ConsumerUsage](hidusage/consumerusage.md)
- [HIDUsage.DigitizersUsage](hidusage/digitizersusage.md)
- [HIDUsage.EyeAndHeadTrackersUsage](hidusage/eyeandheadtrackersusage.md)
- [HIDUsage.FIDOAllianceUsage](hidusage/fidoallianceusage.md)
- [HIDUsage.GameControlsUsage](hidusage/gamecontrolsusage.md)
- [HIDUsage.GenericDesktopUsage](hidusage/genericdesktopusage.md)
- [HIDUsage.GenericDeviceControlsUsage](hidusage/genericdevicecontrolsusage.md)
- [HIDUsage.HapticsUsage](hidusage/hapticsusage.md)
- [HIDUsage.KeyboardOrKeypadUsage](hidusage/keyboardorkeypadusage.md)
- [HIDUsage.LEDUsage](hidusage/ledusage.md)
- [HIDUsage.LightingAndIlluminationUsage](hidusage/lightingandilluminationusage.md)
- [HIDUsage.MagneticStripeReaderUsage](hidusage/magneticstripereaderusage.md)
- [HIDUsage.MedicalInstrumentUsage](hidusage/medicalinstrumentusage.md)
- [HIDUsage.MonitorEnumeratedUsage](hidusage/monitorenumeratedusage.md)
- [HIDUsage.MonitorUsage](hidusage/monitorusage.md)
- [HIDUsage.OrdinalUsage](hidusage/ordinalusage.md)
- [HIDUsage.PhysicalInputDeviceUsage](hidusage/physicalinputdeviceusage.md)
- [HIDUsage.PowerUsage](hidusage/powerusage.md)
- [HIDUsage.SOCUsage](hidusage/socusage.md)
- [HIDUsage.ScalesUsage](hidusage/scalesusage.md)
- [HIDUsage.SensorsUsage](hidusage/sensorsusage.md)
- [HIDUsage.SimulationControlsUsage](hidusage/simulationcontrolsusage.md)
- [HIDUsage.SportControlsUsage](hidusage/sportcontrolsusage.md)
- [HIDUsage.TelephonyDeviceUsage](hidusage/telephonydeviceusage.md)
- [HIDUsage.VESAVirtualControlsUsage](hidusage/vesavirtualcontrolsusage.md)
- [HIDUsage.VRControlsUsage](hidusage/vrcontrolsusage.md)
### Default Implementations
- [CustomStringConvertible Implementations](hidusage/customstringconvertible-implementations.md)
- [Equatable Implementations](hidusage/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Communicating with human interface devices](communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](hidelement.md)
  A representation of an item from a report descriptor for a HID device.
- [struct HIDElementCollection](hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [HIDElement.Value](hidelement/value.md)
  Data associated with a HID element.
- [protocol HIDElementUpdate](hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](hidreporttype.md)
  Types for HID reports.
- [struct HIDReportID](hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDDeviceError](hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage)*