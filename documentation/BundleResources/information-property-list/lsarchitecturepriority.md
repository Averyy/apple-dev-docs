# LSArchitecturePriority

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of the architectures that the app supports, arranged according to their preferred usage.

**Availability**:
- macOS 10.1+

## Details

- **Name**: `LSArchitecturePriority` (Architecture priority)
- **Type**: array of string 

## Possible Values

- `i386`: The 32-bit Intel architecture.
- `x86_64`: The 64-bit Intel architecture.
- `arm64`: The 64-bit ARM architecture.
- `arm64e`: The 64-bit ARM architecture with pointer authentication code support.



**Default**: `i386`

#### Discussion

Use this key to prioritize the execution of a specific architecture in a universal binary. This key contains an array of strings, with each string specifying the name of a supported architecture. The order of the strings in the array represents your preference for executing the app. For example, if you specify the `x86_64` architecture first for a universal app, the system runs that app under Rosetta translation on Apple silicon. For more information about Rosetta translation, see [About the Rosetta translation environment](../../apple-silicon/about-the-rosetta-translation-environment.md).

## See Also

### Launch conditions
- [UIRequiredDeviceCapabilities](./uirequireddevicecapabilities.md)
  The device-related features that your app requires to run.
- [LSMultipleInstancesProhibited](./lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
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
- [CLKComplicationSupportedFamilies](./clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/lsarchitecturepriority)*