# WKWatchOnly

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the app is a watch-only app.

**Availability**:
- watchOS 6.0+

## Details

- **Name**: `WKWatchOnly` (App is only available as a standalone watchOS app)
- **Type**: boolean

#### Discussion

Xcode automatically includes this key in the WatchKit extension’s information property list and sets its value to `YES` when you create a project using the Watch App template. When you set the value of this key to `YES`, the app is only available on Apple Watch, with no related iOS app.

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
- [PUICAutoLaunchAudioOptOut](./puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](./clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wkwatchonly)*