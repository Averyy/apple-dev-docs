# CLKComplicationSupportedFamilies

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The complication families for which the app can provide data.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Details

- **Name**: `CLKComplicationSupportedFamilies` (ClockKit Complication - Supported Families)
- **Type**: array of string 

## Possible Values

- `CLKComplicationFamilyModularSmall`
- `CLKComplicationFamilyModularLarge`
- `CLKComplicationFamilyUtilitarianSmall`
- `CLKComplicationFamilyUtilitarianSmallFlat`
- `CLKComplicationFamilyUtilitarianLarge`
- `CLKComplicationFamilyCircularSmall`
- `CLKComplicationFamilyExtraLarge`
- `CLKComplicationFamilyGraphicCorner`
- `CLKComplicationFamilyGraphicBezel`
- `CLKComplicationFamilyGraphicCircular`
- `CLKComplicationFamilyGraphicRectangular`
- `CLKComplicationFamilyGraphicExtraLarge`

## Discussion

To add this key to the information property list, enable the desired families in the WatchKit extension’s Complication Configuration settings.

## See Also

### Launch conditions
- [UIRequiredDeviceCapabilities](./uirequireddevicecapabilities.md)
  The device-related features that your app requires to run.
- [LSMultipleInstancesProhibited](./lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSArchitecturePriority](./lsarchitecturepriority.md)
  An array of the architectures that the app supports, arranged according to their preferred usage.
- [LSRequiresNativeExecution](./lsrequiresnativeexecution.md)
  A Boolean value that indicates whether to require the execution of the app’s native architecture when multiple architectures are available.
- [WKPrefersNetworkUponForeground](./wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.
- [WKRunsIndependentlyOfCompanionApp](./wkrunsindependentlyofcompanionapp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](./wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](./puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/clkcomplicationsupportedfamilies)*