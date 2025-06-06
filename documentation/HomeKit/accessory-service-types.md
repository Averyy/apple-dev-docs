# Accessory Service Types

**Framework**: HomeKit

The service types supported by HomeKit.

#### Overview

An [`HMService`](hmservice.md) instance’s read-only [`serviceType`](hmservice/servicetype.md) property contains one of the values listed below to tell you what the service does.

Don’t confuse these values with the accessory categories found in [`Accessory Category Types`](accessory-category-types.md). Despite the similarities, they describe different things. Accessories are the physical objects that the user installs in the home, like a garage door opener. Accessories belong to a particular category, like [`HMAccessoryCategoryTypeGarageDoorOpener`](hmaccessorycategorytypegaragedooropener.md).

Accessories have one or more services that perform tasks. The garage door opener accessory has a garage door opener service with service type [`HMServiceTypeGarageDoorOpener`](hmservicetypegaragedooropener.md), given below. The same accessory might also have an attached light providing a light bulb service with service type [`HMServiceTypeLightbulb`](hmservicetypelightbulb.md), also given below.

## Topics

### Light
- [let HMServiceTypeLightbulb: String](hmservicetypelightbulb.md)
  A light bulb service.
- [let HMServiceTypeLightSensor: String](hmservicetypelightsensor.md)
  A light sensor service.
### Power and Switches
- [let HMServiceTypeSwitch: String](hmservicetypeswitch.md)
  A switch service.
- [let HMServiceTypeBattery: String](hmservicetypebattery.md)
  A battery service.
- [let HMServiceTypeOutlet: String](hmservicetypeoutlet.md)
  An outlet service.
- [let HMServiceTypeStatefulProgrammableSwitch: String](hmservicetypestatefulprogrammableswitch.md)
  A stateful programmable switch service.
- [let HMServiceTypeStatelessProgrammableSwitch: String](hmservicetypestatelessprogrammableswitch.md)
  A stateless programmable switch service.
### Air Quality and Smoke Detection
- [let HMServiceTypeAirPurifier: String](hmservicetypeairpurifier.md)
  An air purifier service.
- [let HMServiceTypeAirQualitySensor: String](hmservicetypeairqualitysensor.md)
  An air quality sensor service.
- [let HMServiceTypeCarbonDioxideSensor: String](hmservicetypecarbondioxidesensor.md)
  A carbon dioxide sensor service.
- [let HMServiceTypeCarbonMonoxideSensor: String](hmservicetypecarbonmonoxidesensor.md)
  A carbon monoxide sensor service.
- [let HMServiceTypeSmokeSensor: String](hmservicetypesmokesensor.md)
  A smoke sensor service.
### Temperature and Humidity
- [let HMServiceTypeHeaterCooler: String](hmservicetypeheatercooler.md)
  A heater or cooler service.
- [let HMServiceTypeTemperatureSensor: String](hmservicetypetemperaturesensor.md)
  A temperature sensor service.
- [let HMServiceTypeThermostat: String](hmservicetypethermostat.md)
  A thermostat service.
- [let HMServiceTypeFan: String](hmservicetypefan.md)
  A fan service.
- [let HMServiceTypeFilterMaintenance: String](hmservicetypefiltermaintenance.md)
  A filter maintenance service.
- [let HMServiceTypeHumidifierDehumidifier: String](hmservicetypehumidifierdehumidifier.md)
  A humidifier or dehumidifier service.
- [let HMServiceTypeHumiditySensor: String](hmservicetypehumiditysensor.md)
  A humidity sensor service.
- [let HMServiceTypeVentilationFan: String](hmservicetypeventilationfan.md)
  A ventilation fan service.
### Windows
- [let HMServiceTypeWindow: String](hmservicetypewindow.md)
  A window service.
- [let HMServiceTypeWindowCovering: String](hmservicetypewindowcovering.md)
  A window covering service.
- [let HMServiceTypeSlats: String](hmservicetypeslats.md)
  A slats service.
### Water
- [let HMServiceTypeFaucet: String](hmservicetypefaucet.md)
  A faucet service.
- [let HMServiceTypeValve: String](hmservicetypevalve.md)
  A valve service.
- [let HMServiceTypeIrrigationSystem: String](hmservicetypeirrigationsystem.md)
  An irrigation system service.
- [let HMServiceTypeLeakSensor: String](hmservicetypeleaksensor.md)
  A leak sensor service.
### Locks and Openers
- [let HMServiceTypeDoor: String](hmservicetypedoor.md)
  A door service.
- [let HMServiceTypeDoorbell: String](hmservicetypedoorbell.md)
  A doorbell service.
- [let HMServiceTypeGarageDoorOpener: String](hmservicetypegaragedooropener.md)
  A garage door opener service.
- [let HMServiceTypeLockManagement: String](hmservicetypelockmanagement.md)
  A lock management service.
- [let HMServiceTypeLockMechanism: String](hmservicetypelockmechanism.md)
  A lock mechanism service.
### Safety and Security
- [let HMServiceTypeMotionSensor: String](hmservicetypemotionsensor.md)
  A motion sensor service.
- [let HMServiceTypeOccupancySensor: String](hmservicetypeoccupancysensor.md)
  An occupancy sensor service.
- [let HMServiceTypeSecuritySystem: String](hmservicetypesecuritysystem.md)
  A security system service.
- [let HMServiceTypeContactSensor: String](hmservicetypecontactsensor.md)
  A contact sensor service.
### Video and Audio
- [let HMServiceTypeCameraControl: String](hmservicetypecameracontrol.md)
  A camera control service.
- [let HMServiceTypeCameraRTPStreamManagement: String](hmservicetypecamerartpstreammanagement.md)
  A stream management service.
- [let HMServiceTypeMicrophone: String](hmservicetypemicrophone.md)
  A microphone service.
- [let HMServiceTypeSpeaker: String](hmservicetypespeaker.md)
  An audio speaker service.
- [let HMServiceTypeInputSource: String](hmservicetypeinputsource.md)
  An accessory input source service.
- [let HMServiceTypeTelevision: String](hmservicetypetelevision.md)
  A television service.
### Network
- [let HMServiceTypeWiFiRouter: String](hmservicetypewifirouter.md)
  A WiFi router service.
- [let HMServiceTypeWiFiSatellite: String](hmservicetypewifisatellite.md)
  A Satellite WiFi router service.
### Information
- [let HMServiceTypeLabel: String](hmservicetypelabel.md)
  A label namespace service used when an accessory supports multiple services of the same type.
- [let HMServiceTypeAccessoryInformation: String](hmservicetypeaccessoryinformation.md)
  An accessory information service.

## See Also

- [var serviceType: String](hmservice/servicetype.md)
  The type of the service.
- [var localizedDescription: String](hmservice/localizeddescription.md)
  The localized description of the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/accessory-service-types)*