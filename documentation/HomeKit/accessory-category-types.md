# Accessory Category Types

**Framework**: HomeKit

The accessory category types supported by HomeKit.

#### Overview

An [`HMAccessoryCategory`](hmaccessorycategory.md) instance’s read-only [`categoryType`](hmaccessorycategory/categorytype.md) property contains one of the values listed below to tell you what the associated accessory does.

Don’t confuse these values with the service types found in [`Accessory Service Types`](accessory-service-types.md). Despite the similarities, they describe different things. Accessories are the physical objects that the user installs in the home, like a garage door opener. Accessories belong to one of the categories listed here, like [`HMAccessoryCategoryTypeGarageDoorOpener`](hmaccessorycategorytypegaragedooropener.md).

Accessories have one or more services that perform tasks. The garage door opener accessory has a garage door opener service with service type [`HMServiceTypeGarageDoorOpener`](hmservicetypegaragedooropener.md). The same accessory might also have an attached light providing a light bulb service with service type [`HMServiceTypeLightbulb`](hmservicetypelightbulb.md).

## Topics

### Light
- [let HMAccessoryCategoryTypeLightbulb: String](hmaccessorycategorytypelightbulb.md)
  A lightbulb accessory.
### Power and switches
- [let HMAccessoryCategoryTypeOutlet: String](hmaccessorycategorytypeoutlet.md)
  An outlet accessory.
- [let HMAccessoryCategoryTypeProgrammableSwitch: String](hmaccessorycategorytypeprogrammableswitch.md)
  A programmable switch accessory.
- [let HMAccessoryCategoryTypeSwitch: String](hmaccessorycategorytypeswitch.md)
  A switch accessory.
### Air quality and smoke detection
- [let HMAccessoryCategoryTypeFan: String](hmaccessorycategorytypefan.md)
  A fan accessory.
- [let HMAccessoryCategoryTypeAirPurifier: String](hmaccessorycategorytypeairpurifier.md)
  An air purifier accessory.
### Temperature and humidity
- [let HMAccessoryCategoryTypeThermostat: String](hmaccessorycategorytypethermostat.md)
  A thermostat accessory.
- [let HMAccessoryCategoryTypeAirConditioner: String](hmaccessorycategorytypeairconditioner.md)
  An air conditioner accessory.
- [let HMAccessoryCategoryTypeAirDehumidifier: String](hmaccessorycategorytypeairdehumidifier.md)
  A dehumidifier accessory.
- [let HMAccessoryCategoryTypeAirHeater: String](hmaccessorycategorytypeairheater.md)
  An air heater accessory.
- [let HMAccessoryCategoryTypeAirHumidifier: String](hmaccessorycategorytypeairhumidifier.md)
  A humidifier accessory.
### Windows
- [let HMAccessoryCategoryTypeWindow: String](hmaccessorycategorytypewindow.md)
  A window accessory.
- [let HMAccessoryCategoryTypeWindowCovering: String](hmaccessorycategorytypewindowcovering.md)
  A window covering accessory.
### Locks and openers
- [let HMAccessoryCategoryTypeDoor: String](hmaccessorycategorytypedoor.md)
  A door accessory.
- [let HMAccessoryCategoryTypeDoorLock: String](hmaccessorycategorytypedoorlock.md)
  A door lock accessory.
- [let HMAccessoryCategoryTypeGarageDoorOpener: String](hmaccessorycategorytypegaragedooropener.md)
  A garage door opener accessory.
- [let HMAccessoryCategoryTypeVideoDoorbell: String](hmaccessorycategorytypevideodoorbell.md)
  A video doorbell accessory.
### Safety and security
- [let HMAccessoryCategoryTypeSensor: String](hmaccessorycategorytypesensor.md)
  A sensor accessory.
- [let HMAccessoryCategoryTypeSecuritySystem: String](hmaccessorycategorytypesecuritysystem.md)
  A security system accessory.
### Cameras
- [let HMAccessoryCategoryTypeIPCamera: String](hmaccessorycategorytypeipcamera.md)
  A networked camera accessory.
### Water
- [let HMAccessoryCategoryTypeSprinkler: String](hmaccessorycategorytypesprinkler.md)
  A sprinkler system accessory.
- [let HMAccessoryCategoryTypeFaucet: String](hmaccessorycategorytypefaucet.md)
  A faucet accessory.
- [let HMAccessoryCategoryTypeShowerHead: String](hmaccessorycategorytypeshowerhead.md)
  A shower head accessory.
### Network
- [let HMAccessoryCategoryTypeBridge: String](hmaccessorycategorytypebridge.md)
  A bridge accessory.
- [let HMAccessoryCategoryTypeRangeExtender: String](hmaccessorycategorytyperangeextender.md)
  A range extender accessory.
- [let HMAccessoryCategoryTypeAirPort: String](hmaccessorycategorytypeairport.md)
  An AirPort accessory.
- [let HMAccessoryCategoryTypeWiFiRouter: String](hmaccessorycategorytypewifirouter.md)
  A WiFi router accessory.
### Audio and sound
- [let HMAccessoryCategoryTypeAudioReceiver: String](hmaccessorycategorytypeaudioreceiver.md)
  An audio receiver accessory that supports HAP and AirPlay2.
- [let HMAccessoryCategoryTypeSpeaker: String](hmaccessorycategorytypespeaker.md)
  A speaker accessory.
### Television
- [let HMAccessoryCategoryTypeTelevision: String](hmaccessorycategorytypetelevision.md)
  A television accessory.
- [let HMAccessoryCategoryTypeTelevisionSetTopBox: String](hmaccessorycategorytypetelevisionsettopbox.md)
  A television set-top box accessory.
- [let HMAccessoryCategoryTypeTelevisionStreamingStick: String](hmaccessorycategorytypetelevisionstreamingstick.md)
  A television streaming stick accessory.
### Uncategorized
- [let HMAccessoryCategoryTypeOther: String](hmaccessorycategorytypeother.md)
  An uncategorized accessory.

## See Also

- [var categoryType: String](hmaccessorycategory/categorytype.md)
  The category to which this accessory belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/accessory-category-types)*