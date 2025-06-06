# Characteristic types

**Framework**: HomeKit

The characteristic types supported by HomeKit-based accessories.

#### Overview

A characteristic’s [`characteristicType`](hmcharacteristic/characteristictype.md) is a string constant—typically containing one of the values listed below—that tells you what the characteristic’s [`value`](hmcharacteristic/value.md) represents and how to interpret it. Manufacturers can also create custom types, not listed here.

For some characteristic types, HomeKit defines an enumeration of possible values that the corresponding characteristic can take. For example, a characteristic with type [`HMCharacteristicTypeTemperatureUnits`](hmcharacteristictypetemperatureunits.md) can only have values—corresponding to degrees Fahrenheit or degrees Celsius—from the [`HMCharacteristicValueTemperatureUnit`](hmcharacteristicvaluetemperatureunit.md) enumeration.

For other characteristic types, the corresponding value might be a plain number, a string, or Boolean, or a blob of data with encoding specific to that type.

## Topics

### Light
- [let HMCharacteristicTypeCurrentLightLevel: String](hmcharacteristictypecurrentlightlevel.md)
  The current light level.
- [let HMCharacteristicTypeHue: String](hmcharacteristictypehue.md)
  The hue of the color used by a light.
- [let HMCharacteristicTypeBrightness: String](hmcharacteristictypebrightness.md)
  The brightness of a light.
- [let HMCharacteristicTypeSaturation: String](hmcharacteristictypesaturation.md)
  The saturation of the color used by a light.
- [let HMCharacteristicTypeColorTemperature: String](hmcharacteristictypecolortemperature.md)
  The color temperature of a light.
### Power and switches
- [let HMCharacteristicTypeBatteryLevel: String](hmcharacteristictypebatterylevel.md)
  The battery level of the accessory.
- [let HMCharacteristicTypeChargingState: String](hmcharacteristictypechargingstate.md)
  The charging state of a battery.
- [let HMCharacteristicTypeContactState: String](hmcharacteristictypecontactstate.md)
  The state of a contact sensor.
- [let HMCharacteristicTypeOutletInUse: String](hmcharacteristictypeoutletinuse.md)
  The state of an outlet.
- [let HMCharacteristicTypePowerState: String](hmcharacteristictypepowerstate.md)
  The power state of the accessory.
- [let HMCharacteristicTypeStatusLowBattery: String](hmcharacteristictypestatuslowbattery.md)
  A low battery indicator.
- [let HMCharacteristicTypeOutputState: String](hmcharacteristictypeoutputstate.md)
  The output state of a programmable switch.
- [let HMCharacteristicTypeInputEvent: String](hmcharacteristictypeinputevent.md)
  The input event of a programmable switch.
- [let HMCharacteristicTypePowerModeSelection: String](hmcharacteristictypepowermodeselection.md)
  The selected power mode.
### Temperature
- [let HMCharacteristicTypeCurrentTemperature: String](hmcharacteristictypecurrenttemperature.md)
  The current temperature measured by the accessory.
- [let HMCharacteristicTypeTargetTemperature: String](hmcharacteristictypetargettemperature.md)
  The target temperature for the accessory to achieve.
- [let HMCharacteristicTypeTemperatureUnits: String](hmcharacteristictypetemperatureunits.md)
  The units of temperature currently active on the accessory.
- [let HMCharacteristicTypeTargetHeatingCooling: String](hmcharacteristictypetargetheatingcooling.md)
  The target heating or cooling mode for a thermostat.
- [let HMCharacteristicTypeCurrentHeatingCooling: String](hmcharacteristictypecurrentheatingcooling.md)
  The current heating or cooling mode for a thermostat.
- [let HMCharacteristicTypeTargetHeaterCoolerState: String](hmcharacteristictypetargetheatercoolerstate.md)
  The target state for a device that heats or cools, like an oven or a refrigerator.
- [let HMCharacteristicTypeCurrentHeaterCoolerState: String](hmcharacteristictypecurrentheatercoolerstate.md)
  The current state for a device that heats or cools, like an oven or a refrigerator.
- [let HMCharacteristicTypeCoolingThreshold: String](hmcharacteristictypecoolingthreshold.md)
  The temperature above which cooling will be active.
- [let HMCharacteristicTypeHeatingThreshold: String](hmcharacteristictypeheatingthreshold.md)
  The temperature below which heating will be active.
### Humidity
- [let HMCharacteristicTypeCurrentRelativeHumidity: String](hmcharacteristictypecurrentrelativehumidity.md)
  The current relative humidity measured by the accessory.
- [let HMCharacteristicTypeTargetRelativeHumidity: String](hmcharacteristictypetargetrelativehumidity.md)
  The target relative humidity for the accessory to achieve.
- [let HMCharacteristicTypeCurrentHumidifierDehumidifierState: String](hmcharacteristictypecurrenthumidifierdehumidifierstate.md)
  The current state of a humidifier or dehumidifier accessory.
- [let HMCharacteristicTypeTargetHumidifierDehumidifierState: String](hmcharacteristictypetargethumidifierdehumidifierstate.md)
  The state that a humidifier or dehumidifier accessory should try to achieve.
- [let HMCharacteristicTypeHumidifierThreshold: String](hmcharacteristictypehumidifierthreshold.md)
  The humidity below which a humidifier should begin to work.
- [let HMCharacteristicTypeDehumidifierThreshold: String](hmcharacteristictypedehumidifierthreshold.md)
  The humidity above which a dehumidifier should begin to work.
### Air quality and smoke detection
- [let HMCharacteristicTypeAirQuality: String](hmcharacteristictypeairquality.md)
  The air quality.
- [let HMCharacteristicTypeAirParticulateDensity: String](hmcharacteristictypeairparticulatedensity.md)
  The density of air-particulate matter.
- [let HMCharacteristicTypeAirParticulateSize: String](hmcharacteristictypeairparticulatesize.md)
  The size of the air-particulate matter.
- [let HMCharacteristicTypeSmokeDetected: String](hmcharacteristictypesmokedetected.md)
  A smoke detection indicator.
- [let HMCharacteristicTypeCarbonDioxideDetected: String](hmcharacteristictypecarbondioxidedetected.md)
  An indicator of abnormally high levels of carbon dioxide.
- [let HMCharacteristicTypeCarbonDioxideLevel: String](hmcharacteristictypecarbondioxidelevel.md)
  The measured carbon dioxide level.
- [let HMCharacteristicTypeCarbonDioxidePeakLevel: String](hmcharacteristictypecarbondioxidepeaklevel.md)
  The highest recorded level of carbon dioxide.
- [let HMCharacteristicTypeCarbonMonoxideDetected: String](hmcharacteristictypecarbonmonoxidedetected.md)
  An indicator of abnormally high levels of carbon monoxide.
- [let HMCharacteristicTypeCarbonMonoxideLevel: String](hmcharacteristictypecarbonmonoxidelevel.md)
  The measured carbon monoxide level.
- [let HMCharacteristicTypeCarbonMonoxidePeakLevel: String](hmcharacteristictypecarbonmonoxidepeaklevel.md)
  The highest recorded level of carbon monoxide.
- [let HMCharacteristicTypeNitrogenDioxideDensity: String](hmcharacteristictypenitrogendioxidedensity.md)
  The measured density of nitrogen dioxide.
- [let HMCharacteristicTypeOzoneDensity: String](hmcharacteristictypeozonedensity.md)
  The measured density of ozone.
- [let HMCharacteristicTypePM10Density: String](hmcharacteristictypepm10density.md)
  The measured density of air-particulate matter of size 10 micrograms.
- [let HMCharacteristicTypePM2_5Density: String](hmcharacteristictypepm2_5density.md)
  The measured density of air-particulate matter of size 2.5 micrograms.
- [let HMCharacteristicTypeSulphurDioxideDensity: String](hmcharacteristictypesulphurdioxidedensity.md)
  The measured density of sulphur dioxide.
- [let HMCharacteristicTypeVolatileOrganicCompoundDensity: String](hmcharacteristictypevolatileorganiccompounddensity.md)
  The measured density of volatile organic compounds.
### Fans
- [let HMCharacteristicTypeCurrentFanState: String](hmcharacteristictypecurrentfanstate.md)
  The current state of a fan.
- [let HMCharacteristicTypeTargetFanState: String](hmcharacteristictypetargetfanstate.md)
  The target state of a fan.
- [let HMCharacteristicTypeRotationDirection: String](hmcharacteristictyperotationdirection.md)
  The rotation direction of an accessory like a fan.
- [let HMCharacteristicTypeRotationSpeed: String](hmcharacteristictyperotationspeed.md)
  The rotation speed of an accessory like a fan.
- [let HMCharacteristicTypeSwingMode: String](hmcharacteristictypeswingmode.md)
  An indicator of whether a fan swings back and forth during operation.
### Purifiers and filters
- [let HMCharacteristicTypeCurrentAirPurifierState: String](hmcharacteristictypecurrentairpurifierstate.md)
  The current air purifier state.
- [let HMCharacteristicTypeTargetAirPurifierState: String](hmcharacteristictypetargetairpurifierstate.md)
  The target air purifier state.
- [let HMCharacteristicTypeFilterLifeLevel: String](hmcharacteristictypefilterlifelevel.md)
  The amount of useful life remaining in a filter.
- [let HMCharacteristicTypeFilterChangeIndication: String](hmcharacteristictypefilterchangeindication.md)
  A filter’s change indicator.
- [let HMCharacteristicTypeFilterResetChangeIndication: String](hmcharacteristictypefilterresetchangeindication.md)
  A reset control for a filter change notification.
### Water
- [let HMCharacteristicTypeWaterLevel: String](hmcharacteristictypewaterlevel.md)
  The water level measured by an accessory.
- [let HMCharacteristicTypeValveType: String](hmcharacteristictypevalvetype.md)
  The type of automated valve that controls fluid flow.
- [let HMCharacteristicTypeLeakDetected: String](hmcharacteristictypeleakdetected.md)
  A leak detection indicator.
### Doors and windows
- [let HMCharacteristicTypeCurrentDoorState: String](hmcharacteristictypecurrentdoorstate.md)
  The current door state.
- [let HMCharacteristicTypeTargetDoorState: String](hmcharacteristictypetargetdoorstate.md)
  The target door state.
- [let HMCharacteristicTypeCurrentPosition: String](hmcharacteristictypecurrentposition.md)
  The current position of a door, window, awning, or window covering.
- [let HMCharacteristicTypeTargetPosition: String](hmcharacteristictypetargetposition.md)
  The target position of a door, window, awning, or window covering.
- [let HMCharacteristicTypePositionState: String](hmcharacteristictypepositionstate.md)
  The position of an accessory like a door, window, awning, or window covering.
- [let HMCharacteristicTypeStatusJammed: String](hmcharacteristictypestatusjammed.md)
  An indicator of whether an accessory is jammed.
- [let HMCharacteristicTypeHoldPosition: String](hmcharacteristictypeholdposition.md)
  A control for holding the position of an accessory like a door or window.
- [let HMCharacteristicTypeSlatType: String](hmcharacteristictypeslattype.md)
  The type of slat on an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentSlatState: String](hmcharacteristictypecurrentslatstate.md)
  The current state of slats on an accessory like a window or a fan.
### Tilting mechanisms
- [let HMCharacteristicTypeCurrentHorizontalTilt: String](hmcharacteristictypecurrenthorizontaltilt.md)
  The current tilt angle of a horizontal slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetHorizontalTilt: String](hmcharacteristictypetargethorizontaltilt.md)
  The target tilt angle of a horizontal slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentVerticalTilt: String](hmcharacteristictypecurrentverticaltilt.md)
  The current tilt angle of a vertical slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetVerticalTilt: String](hmcharacteristictypetargetverticaltilt.md)
  The target tilt angle of a vertical slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentTilt: String](hmcharacteristictypecurrenttilt.md)
  The current tilt angle of a slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetTilt: String](hmcharacteristictypetargettilt.md)
  The target tilt angle of a slat for an accessory like a window or a fan.
### Locks and openers
- [let HMCharacteristicTypeLockManagementAutoSecureTimeout: String](hmcharacteristictypelockmanagementautosecuretimeout.md)
  The automatic timeout for a lockable accessory that supports automatic lockout.
- [let HMCharacteristicTypeLockManagementControlPoint: String](hmcharacteristictypelockmanagementcontrolpoint.md)
  A control that accepts vendor-specific actions for lock management.
- [let HMCharacteristicTypeLockMechanismLastKnownAction: String](hmcharacteristictypelockmechanismlastknownaction.md)
  The last known action of the locking mechanism.
- [let HMCharacteristicTypeLockPhysicalControls: String](hmcharacteristictypelockphysicalcontrols.md)
  The lock’s physical control state.
- [let HMCharacteristicTypeMotionDetected: String](hmcharacteristictypemotiondetected.md)
  An indicator of whether the accessory has detected motion.
- [let HMCharacteristicTypeCurrentLockMechanismState: String](hmcharacteristictypecurrentlockmechanismstate.md)
  The current state of the locking mechanism.
- [let HMCharacteristicTypeTargetLockMechanismState: String](hmcharacteristictypetargetlockmechanismstate.md)
  The target state for the locking mechanism.
- [let HMCharacteristicTypeRemoteKey: String](hmcharacteristictyperemotekey.md)
  The accessory remote control key.
### Safety and security
- [let HMCharacteristicTypeCurrentSecuritySystemState: String](hmcharacteristictypecurrentsecuritysystemstate.md)
  The current security system state.
- [let HMCharacteristicTypeTargetSecuritySystemState: String](hmcharacteristictypetargetsecuritysystemstate.md)
  The target security system state.
- [let HMCharacteristicTypeObstructionDetected: String](hmcharacteristictypeobstructiondetected.md)
  An indicator of whether an obstruction is detected, as when something prevents a garage door from closing.
- [let HMCharacteristicTypeOccupancyDetected: String](hmcharacteristictypeoccupancydetected.md)
  An indicator of whether the home is occupied.
- [let HMCharacteristicTypeSecuritySystemAlarmType: String](hmcharacteristictypesecuritysystemalarmtype.md)
  The alarm trigger state.
- [let HMCharacteristicPropertyRequiresAuthorizationData: String](hmcharacteristicpropertyrequiresauthorizationdata.md)
  A variable that specifies that the characteristic requires authorization data to write.
### Audio and video
- [let HMCharacteristicTypeSupportedRTPConfiguration: String](hmcharacteristictypesupportedrtpconfiguration.md)
  The supported Real-time Transport Protocol (RTP) configuration.
- [let HMCharacteristicTypeDigitalZoom: String](hmcharacteristictypedigitalzoom.md)
  The digital zoom of a video Real-time Transport Protocol (RTP) service.
- [let HMCharacteristicTypeOpticalZoom: String](hmcharacteristictypeopticalzoom.md)
  The optical zoom setting of the camera sourcing a video Real-time Transport Protocol (RTP) service.
- [let HMCharacteristicTypeImageMirroring: String](hmcharacteristictypeimagemirroring.md)
  An indicator of whether the image should be flipped about the vertical axis.
- [let HMCharacteristicTypeImageRotation: String](hmcharacteristictypeimagerotation.md)
  The angle of rotation for an image.
- [let HMCharacteristicTypeNightVision: String](hmcharacteristictypenightvision.md)
  An indicator of whether night vision is enabled on a video Real-time Transport Protocol (RTP) service.
- [let HMCharacteristicTypeStreamingStatus: String](hmcharacteristictypestreamingstatus.md)
  A description of the status of the Real-time Transport Protocol (RTP) stream management service.
- [let HMCharacteristicTypeSupportedVideoStreamConfiguration: String](hmcharacteristictypesupportedvideostreamconfiguration.md)
  The video stream’s configuration.
- [let HMCharacteristicTypeSupportedAudioStreamConfiguration: String](hmcharacteristictypesupportedaudiostreamconfiguration.md)
  The audio stream’s configuration.
- [let HMCharacteristicTypeSelectedStreamConfiguration: String](hmcharacteristictypeselectedstreamconfiguration.md)
  The selected stream’s configuration.
- [let HMCharacteristicTypeSetupStreamEndpoint: String](hmcharacteristictypesetupstreamendpoint.md)
  The stream’s endpoint configuration.
- [let HMCharacteristicTypeAudioFeedback: String](hmcharacteristictypeaudiofeedback.md)
  An indicator of whether audio feedback, like a beep or other external sound mechanism, is enabled.
- [let HMCharacteristicTypeVolume: String](hmcharacteristictypevolume.md)
  The input or output volume of an audio device.
- [let HMCharacteristicTypeMute: String](hmcharacteristictypemute.md)
  A control for muting audio.
- [let HMCharacteristicTypeVolumeSelector: String](hmcharacteristictypevolumeselector.md)
  The mechanism to increment or decrement the volume by the default step value.
- [let HMCharacteristicTypeVolumeControlType: String](hmcharacteristictypevolumecontroltype.md)
  The volume control capabilities of an accessory.
- [let HMCharacteristicTypeClosedCaptions: String](hmcharacteristictypeclosedcaptions.md)
  An indictator of whether closed captions are enabled or disabled.
- [let HMCharacteristicTypePictureMode: String](hmcharacteristictypepicturemode.md)
  The selected picture mode.
### General state
- [let HMCharacteristicTypeActive: String](hmcharacteristictypeactive.md)
  The current status of an accessory.
- [let HMCharacteristicTypeStatusTampered: String](hmcharacteristictypestatustampered.md)
  An indicator of whether an accessory has been tampered with.
- [let HMCharacteristicTypeStatusFault: String](hmcharacteristictypestatusfault.md)
  An indicator of whether the accessory has experienced a fault.
- [let HMCharacteristicTypeStatusActive: String](hmcharacteristictypestatusactive.md)
  An indicator of whether the service is working.
- [let HMCharacteristicTypeInUse: String](hmcharacteristictypeinuse.md)
  The current usage state of an accessory.
- [let HMCharacteristicTypeIsConfigured: String](hmcharacteristictypeisconfigured.md)
  The configuration state of an accessory.
- [let HMCharacteristicTypeRemainingDuration: String](hmcharacteristictyperemainingduration.md)
  The number of seconds remaining for the activity being carried out by the accessory.
- [let HMCharacteristicTypeSetDuration: String](hmcharacteristictypesetduration.md)
  The duration of the activity being carried out by the accessory.
- [let HMCharacteristicTypeProgramMode: String](hmcharacteristictypeprogrammode.md)
  The current mode of the accessory’s scheduled programs.
- [let HMCharacteristicTypeWiFiSatelliteStatus: String](hmcharacteristictypewifisatellitestatus.md)
  The network status of the WiFi satellite accessory.
- [let HMCharacteristicTypeWANStatusList: String](hmcharacteristictypewanstatuslist.md)
  The WAN status list of an accessory.
- [let HMCharacteristicTypeTargetMediaState: String](hmcharacteristictypetargetmediastate.md)
  The target media state.
- [let HMCharacteristicTypeRouterStatus: String](hmcharacteristictyperouterstatus.md)
  The current status of the router.
- [let HMCharacteristicTypeCurrentMediaState: String](hmcharacteristictypecurrentmediastate.md)
  The current state of the media.
- [let HMCharacteristicTypeCurrentVisibilityState: String](hmcharacteristictypecurrentvisibilitystate.md)
  The current visibility state for a service.
- [let HMCharacteristicTypeTargetVisibilityState: String](hmcharacteristictypetargetvisibilitystate.md)
  The target visibility state for a service.
- [let HMCharacteristicPropertySupportsEventNotification: String](hmcharacteristicpropertysupportseventnotification-2f0ml.md)
  The characteristic supports event notifications.
### Accessory identification
- [let HMCharacteristicTypeName: String](hmcharacteristictypename.md)
  The name of the accessory.
- [let HMCharacteristicTypeIdentify: String](hmcharacteristictypeidentify.md)
  A control you can use to ask the accessory to identify itself.
- [let HMCharacteristicTypeVersion: String](hmcharacteristictypeversion.md)
  The version of the accessory.
- [let HMCharacteristicTypeLogs: String](hmcharacteristictypelogs.md)
  Log data for the accessory.
- [let HMCharacteristicTypeAdminOnlyAccess: String](hmcharacteristictypeadminonlyaccess.md)
  An indicator of whether the accessory accepts only administrator access.
- [let HMCharacteristicTypeHardwareVersion: String](hmcharacteristictypehardwareversion.md)
  The hardware version of the accessory.
- [let HMCharacteristicTypeSoftwareVersion: String](hmcharacteristictypesoftwareversion.md)
  The software version of the accessory.
- [let HMCharacteristicTypeLabelIndex: String](hmcharacteristictypelabelindex.md)
  The index of the label for the service on an accessory with multiple instances of the same service.
- [let HMCharacteristicTypeLabelNamespace: String](hmcharacteristictypelabelnamespace.md)
  The naming schema used to label the services on an accessory with multiple services of the same type.
- [let HMCharacteristicTypeActiveIdentifier: String](hmcharacteristictypeactiveidentifier.md)
  An index that maps to the current active Input Source service.
- [let HMCharacteristicTypeIdentifier: String](hmcharacteristictypeidentifier.md)
  The identifier for an accessory.
- [let HMCharacteristicTypeInputDeviceType: String](hmcharacteristictypeinputdevicetype.md)
  The accessory input device type.
- [let HMCharacteristicTypeInputSourceType: String](hmcharacteristictypeinputsourcetype.md)
  The accessory input source type.
- [let HMCharacteristicTypeConfiguredName: String](hmcharacteristictypeconfiguredname.md)
  A `UTF‑8` encoded user visible name on an accessory.
### Deprecated characteristic types
- [let HMCharacteristicTypeManufacturer: String](hmcharacteristictypemanufacturer.md)
  The manufacturer of the accessory.
- [let HMCharacteristicTypeModel: String](hmcharacteristictypemodel.md)
  The model of the accessory.
- [let HMCharacteristicTypeFirmwareVersion: String](hmcharacteristictypefirmwareversion.md)
  The firmware version of the accessory.
- [let HMCharacteristicTypeSerialNumber: String](hmcharacteristictypeserialnumber.md)
  The serial number of the accessory.

## See Also

- [var characteristicType: String](hmcharacteristic/characteristictype.md)
  The type of the characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/characteristic-types)*