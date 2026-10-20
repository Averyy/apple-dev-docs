# HIDUsage

**Framework**: Core HID  
**Kind**: enum  
**Role**: Enumeration

A type to represent HID usage pages.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum HIDUsage
```

#### Overview

A HID usage page combines with a HID usage to specify the intended functionality for the associated item. Associated items can be descriptors, devices, reports, report data, elements, etc..

Currently unsupported cases can be used as [`HIDUsage.generic(_:_:)`](./hidusage/generic%28_,_%29.md), but may be added as supported cases later.

For more details, see [Human Interface Devices (HID) Specifications and Tools](https://www.usb.org/hid).

## Topics

### Enumeration Cases
- [case arcade(HIDUsage.ArcadeUsage?)](./hidusage/arcade%28_%29.md)
- [case auxiliaryDisplay(HIDUsage.AuxiliaryDisplayUsage?)](./hidusage/auxiliarydisplay%28_%29.md)
- [case barcodeScanner(HIDUsage.BarcodeScannerUsage?)](./hidusage/barcodescanner%28_%29.md)
- [case batterySystem(HIDUsage.BatterySystemUsage?)](./hidusage/batterysystem%28_%29.md)
- [case brailleDisplay(HIDUsage.BrailleDisplayUsage?)](./hidusage/brailledisplay%28_%29.md)
- [case button(UInt16?)](./hidusage/button%28_%29.md)
- [case cameraControl(HIDUsage.CameraControlUsage?)](./hidusage/cameracontrol%28_%29.md)
- [case consumer(HIDUsage.ConsumerUsage?)](./hidusage/consumer%28_%29.md)
- [case digitizers(HIDUsage.DigitizersUsage?)](./hidusage/digitizers%28_%29.md)
- [case eyeAndHeadTrackers(HIDUsage.EyeAndHeadTrackersUsage?)](./hidusage/eyeandheadtrackers%28_%29.md)
- [case fidoAlliance(HIDUsage.FIDOAllianceUsage?)](./hidusage/fidoalliance%28_%29.md)
- [case gameControls(HIDUsage.GameControlsUsage?)](./hidusage/gamecontrols%28_%29.md)
- [case generic(UInt16, UInt16?)](./hidusage/generic%28_,_%29.md)
- [case genericDesktop(HIDUsage.GenericDesktopUsage?)](./hidusage/genericdesktop%28_%29.md)
- [case genericDeviceControls(HIDUsage.GenericDeviceControlsUsage?)](./hidusage/genericdevicecontrols%28_%29.md)
- [case haptics(HIDUsage.HapticsUsage?)](./hidusage/haptics%28_%29.md)
- [case keyboardOrKeypad(HIDUsage.KeyboardOrKeypadUsage?)](./hidusage/keyboardorkeypad%28_%29.md)
- [case led(HIDUsage.LEDUsage?)](./hidusage/led%28_%29.md)
- [case lightingAndIllumination(HIDUsage.LightingAndIlluminationUsage?)](./hidusage/lightingandillumination%28_%29.md)
- [case magneticStripeReader(HIDUsage.MagneticStripeReaderUsage?)](./hidusage/magneticstripereader%28_%29.md)
- [case medicalInstrument(HIDUsage.MedicalInstrumentUsage?)](./hidusage/medicalinstrument%28_%29.md)
- [case monitor(HIDUsage.MonitorUsage?)](./hidusage/monitor%28_%29.md)
- [case monitorEnumerated(UInt16?)](./hidusage/monitorenumerated%28_%29.md)
- [case ordinal(UInt16?)](./hidusage/ordinal%28_%29.md)
- [case physicalInputDevice(HIDUsage.PhysicalInputDeviceUsage?)](./hidusage/physicalinputdevice%28_%29.md)
- [case power(HIDUsage.PowerUsage?)](./hidusage/power%28_%29.md)
- [case scales(HIDUsage.ScalesUsage?)](./hidusage/scales%28_%29.md)
- [case sensors(HIDUsage.SensorsUsage?)](./hidusage/sensors%28_%29.md)
- [case simulationControls(HIDUsage.SimulationControlsUsage?)](./hidusage/simulationcontrols%28_%29.md)
- [case soc(HIDUsage.SOCUsage?)](./hidusage/soc%28_%29.md)
- [case sportControls(HIDUsage.SportControlsUsage?)](./hidusage/sportcontrols%28_%29.md)
- [case telephonyDevice(HIDUsage.TelephonyDeviceUsage?)](./hidusage/telephonydevice%28_%29.md)
- [case vesaVirtualControls(HIDUsage.VESAVirtualControlsUsage?)](./hidusage/vesavirtualcontrols%28_%29.md)
- [case vrControls(HIDUsage.VRControlsUsage?)](./hidusage/vrcontrols%28_%29.md)
### Initializers
- [init(page: UInt16, usage: UInt16?)](./hidusage/init%28page,usage%29.md)
  Creates a HID usage page from raw page and usage values.
### Instance Properties
- [var page: UInt16](./hidusage/page.md)
  The usage page value.
- [var usage: UInt16?](./hidusage/usage.md)
  The usage value.
### Enumerations
- [HIDUsage.ArcadeUsage](./hidusage/arcadeusage.md)
- [HIDUsage.AuxiliaryDisplayUsage](./hidusage/auxiliarydisplayusage.md)
- [HIDUsage.BarcodeScannerUsage](./hidusage/barcodescannerusage.md)
- [HIDUsage.BatterySystemUsage](./hidusage/batterysystemusage.md)
- [HIDUsage.BrailleDisplayUsage](./hidusage/brailledisplayusage.md)
- [HIDUsage.ButtonUsage](./hidusage/buttonusage.md)
- [HIDUsage.CameraControlUsage](./hidusage/cameracontrolusage.md)
- [HIDUsage.ConsumerUsage](./hidusage/consumerusage.md)
- [HIDUsage.DigitizersUsage](./hidusage/digitizersusage.md)
- [HIDUsage.EyeAndHeadTrackersUsage](./hidusage/eyeandheadtrackersusage.md)
- [HIDUsage.FIDOAllianceUsage](./hidusage/fidoallianceusage.md)
- [HIDUsage.GameControlsUsage](./hidusage/gamecontrolsusage.md)
- [HIDUsage.GenericDesktopUsage](./hidusage/genericdesktopusage.md)
- [HIDUsage.GenericDeviceControlsUsage](./hidusage/genericdevicecontrolsusage.md)
- [HIDUsage.HapticsUsage](./hidusage/hapticsusage.md)
- [HIDUsage.KeyboardOrKeypadUsage](./hidusage/keyboardorkeypadusage.md)
- [HIDUsage.LEDUsage](./hidusage/ledusage.md)
- [HIDUsage.LightingAndIlluminationUsage](./hidusage/lightingandilluminationusage.md)
- [HIDUsage.MagneticStripeReaderUsage](./hidusage/magneticstripereaderusage.md)
- [HIDUsage.MedicalInstrumentUsage](./hidusage/medicalinstrumentusage.md)
- [HIDUsage.MonitorEnumeratedUsage](./hidusage/monitorenumeratedusage.md)
- [HIDUsage.MonitorUsage](./hidusage/monitorusage.md)
- [HIDUsage.OrdinalUsage](./hidusage/ordinalusage.md)
- [HIDUsage.PhysicalInputDeviceUsage](./hidusage/physicalinputdeviceusage.md)
- [HIDUsage.PowerUsage](./hidusage/powerusage.md)
- [HIDUsage.SOCUsage](./hidusage/socusage.md)
- [HIDUsage.ScalesUsage](./hidusage/scalesusage.md)
- [HIDUsage.SensorsUsage](./hidusage/sensorsusage.md)
- [HIDUsage.SimulationControlsUsage](./hidusage/simulationcontrolsusage.md)
- [HIDUsage.SportControlsUsage](./hidusage/sportcontrolsusage.md)
- [HIDUsage.TelephonyDeviceUsage](./hidusage/telephonydeviceusage.md)
- [HIDUsage.VESAVirtualControlsUsage](./hidusage/vesavirtualcontrolsusage.md)
- [HIDUsage.VRControlsUsage](./hidusage/vrcontrolsusage.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interaction
- [Communicating with human interface devices](./communicatingwithhiddevices.md)
  Interact with and obtain data from devices such as keyboards and mice.
- [actor HIDDeviceClient](./hiddeviceclient.md)
  A client of a physical or virtual HID compatible peripheral.
- [struct HIDElement](./hidelement.md)
  A representation of an item from a report descriptor for a HID device.
- [struct HIDElementCollection](./hidelementcollection.md)
  A collection of items from a report descriptor for a HID device.
- [HIDElement.Value](./hidelement/value.md)
  Data associated with a HID element.
- [protocol HIDElementUpdate](./hidelementupdate.md)
  A base protocol for element update types.
- [enum HIDReportType](./hidreporttype.md)
  Types for HID reports.
- [struct HIDReportID](./hidreportid.md)
  A type to represent the report IDs of HID reports.
- [enum HIDDeviceError](./hiddeviceerror.md)
  Errors that the framework can throw.
- [enum HIDDeviceTransport](./hiddevicetransport.md)
  Common transport types that transmit data to or from a HID device.
- [enum HIDDeviceLocalizationCode](./hiddevicelocalizationcode.md)
  The localization codes that some HID devices declare to specify conformance to a certain format or language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage)*