# LSArchitecturePriority

**Framework**: Bundle Resources  
**Kind**: typealias

An array of the architectures that the app supports, arranged according to their preferred usage.

**Availability**:
- macOS 10.1+

#### Discussion

Use this key to prioritize the execution of a specific architecture in a universal binary. This key contains an array of strings, with each string specifying the name of a supported architecture. The order of the strings in the array represents your preference for executing the app. For example, if you specify the `x86_64` architecture first for a universal app, the system runs that app under Rosetta translation on Apple silicon. For more information about Rosetta translation, see [`About the Rosetta translation environment`](https://developer.apple.com/documentation/Apple-Silicon/about-the-rosetta-translation-environment).

## See Also

- [UIRequiredDeviceCapabilities](information-property-list/uirequireddevicecapabilities.md)
  The device-related features that your app requires to run.
- [LSMultipleInstancesProhibited](information-property-list/lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSRequiresNativeExecution](information-property-list/lsrequiresnativeexecution.md)
  A Boolean value that indicates whether to require the execution of the app’s native architecture when multiple architectures are available.
- [WKPrefersNetworkUponForeground](information-property-list/wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.
- [WKRunsIndependentlyOfCompanionApp](information-property-list/wkrunsindependentlyofcompanionapp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](information-property-list/wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](information-property-list/puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](information-property-list/clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lsarchitecturepriority)*