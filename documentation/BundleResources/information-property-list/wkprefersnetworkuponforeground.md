# WKPrefersNetworkUponForeground

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app requires network access on launch.

**Availability**:
- watchOS 9.0+

#### Discussion

In low-power mode, the system turns off cellular data to preserve battery life. If this key is `NO`, the system waits until an app requests a network connection before turning on cellular data. This can cause a few seconds of delay before your app can perform network requests.

If your app needs access to the network immediately upon launch, set this key to `YES`.

[`WKPrefersNetworkUponForeground`](information-property-list/wkprefersnetworkuponforeground.md) defaults to `NO`.

## See Also

- [UIRequiredDeviceCapabilities](information-property-list/uirequireddevicecapabilities.md)
  The device-related features that your app requires to run.
- [LSMultipleInstancesProhibited](information-property-list/lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSArchitecturePriority](information-property-list/lsarchitecturepriority.md)
  An array of the architectures that the app supports, arranged according to their preferred usage.
- [LSRequiresNativeExecution](information-property-list/lsrequiresnativeexecution.md)
  A Boolean value that indicates whether to require the execution of the app’s native architecture when multiple architectures are available.
- [WKRunsIndependentlyOfCompanionApp](information-property-list/wkrunsindependentlyofcompanionapp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](information-property-list/wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](information-property-list/puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](information-property-list/clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/wkprefersnetworkuponforeground)*