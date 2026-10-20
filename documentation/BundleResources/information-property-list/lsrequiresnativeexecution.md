# LSRequiresNativeExecution

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether to require the execution of the app’s native architecture when multiple architectures are available.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `LSRequiresNativeExecution` (Application requires native environment)
- **Type**: boolean

#### Discussion

The presence of this key causes the system to choose a native architecture over one that requires translation. For example, this key prevents the system from using the Rosetta translation process to execute the Intel portion of a universal app on Apple silicon.

If your app’s binary supports only the Intel architecture and you link the app against the macOS 11 SDK or later, the inclusion of this key prevents your app from running on Apple silicon. If you link the app against an earlier macOS SDK, the app runs under Rosetta translation.

## See Also

### Launch conditions
- [UIRequiredDeviceCapabilities](./uirequireddevicecapabilities.md)
  The device-related features that your app requires to run.
- [LSMultipleInstancesProhibited](./lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSArchitecturePriority](./lsarchitecturepriority.md)
  An array of the architectures that the app supports, arranged according to their preferred usage.
- [WKPrefersNetworkUponForeground](./wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.
- [WKRunsIndependentlyOfCompanionApp](./wkrunsindependentlyofcompanionapp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](./wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](./puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](./clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lsrequiresnativeexecution)*