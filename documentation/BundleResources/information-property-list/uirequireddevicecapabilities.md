# UIRequiredDeviceCapabilities

**Framework**: Bundle Resources  
**Kind**: typealias

The device-related features that your app requires to run.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Discussion

The App Store prevents customers from installing an app on a device that doesn’t support the required capabilities for that app. Use this key to declare the capabilities your app requires. For a list of the features that different devices support, see [`Required Device Capabilities`](https://developer.apple.comhttps://developer.apple.com/support/required-device-capabilities/).

You typically use an array for the key’s associated value. The presence in that array of any of the above possible values indicates that the app requires the corresponding feature. Omit a value to indicate that the app doesn’t require the feature, but it can be present.

Alternatively, you can use a dictionary as the associated value for the [`UIRequiredDeviceCapabilities`](information-property-list/uirequireddevicecapabilities.md) key. In that case, use the values above as the dictionary’s keys, each with an associated Boolean value. Set the value to `true` to require the corresponding feature. Set the value to `false` to indicate that the feature must not be present on the device. Omit the feature from the dictionary to indicate that your app neither requires nor disallows it.

Specify only the features that your app absolutely requires. If your app can accommodate missing features by avoiding the code paths that use those features, don’t include the corresponding key.

> ❗ **Important**:  Your app must include the [`UIRequiredDeviceCapabilities`](information-property-list/uirequireddevicecapabilities.md) key in the [`Information Property List`](information-property-list.md) file that you submit with your binary. For app updates, you can only maintain or relax capability requirements. Submitting an update with added requirements would prevent some customers who previously downloaded your app from running the update.

## See Also

- [LSMultipleInstancesProhibited](information-property-list/lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSArchitecturePriority](information-property-list/lsarchitecturepriority.md)
  An array of the architectures that the app supports, arranged according to their preferred usage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequireddevicecapabilities)*