# PUICAutoLaunchAudioOptOut

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.

**Availability**:
- watchOS 5.0+

## Details

- **Name**: `PUICAutoLaunchAudioOptOut` (Opt out of Auto-launch Audio App (Watch))
- **Type**: boolean

#### Discussion

If your watchOS app does not act as a remote control for the iOS app, set this key to `YES` in your WatchKit extension’s information property list.

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
- [CLKComplicationSupportedFamilies](./clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/puicautolaunchaudiooptout)*