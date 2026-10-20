# WKRunsIndependentlyOfCompanionApp

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.

**Availability**:
- watchOS 6.0+

## Details

- **Name**: `WKRunsIndependentlyOfCompanionApp` (App can run independently of companion iPhone app)
- **Type**: boolean

#### Discussion

Xcode automatically includes this key in the WatchKit extension’s information property list and sets its value to `YES` when you create a project using the iOS App with Watch App template. When you set the value of this key to `YES`, the app doesn’t need its iOS companion app to operate properly. Users can choose to install the iOS app, the watchOS app, or both.

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
- [WKWatchOnly](./wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](./puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](./clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wkrunsindependentlyofcompanionapp)*