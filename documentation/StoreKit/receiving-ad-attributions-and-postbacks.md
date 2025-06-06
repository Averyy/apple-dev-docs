# Receiving ad attributions and postbacks

**Framework**: StoreKit

Learn about timeframes and priorities for ad impressions that result in ad attributions, and how additional impressions qualify for postbacks.

#### Overview

Ad networks receive attributions in the form of install-validation postbacks. Before an ad network can receive a postback, the following events need to occur within limited time-windows:

- Ad networks sign and present ads in the form of StoreKit-rendered ads, view-through ads, or attributable web ads. StoreKit records the ad impressions.
- Users install the advertised app.
- Users launch the app.
- The app updates the conversion values when the user first launches the app, and continues to update it as needed.

If all these events occur within their respective time-windows, the ad impression qualifies for an install-validation postback. The following table shows the time-windows for the events:

| Event | Time-window |
| --- | --- |
| The ad network presents a StoreKit-rendered ad. | The user has 30 days to install the app. |
| The ad network presents a view-through ad. | The user has 24 hours to install the app. |
| The user taps an attributable web ad. | The user has 30 days to install the app. |
| The user installs the app. | The user has 60 days to launch the app. |
| The user launches the app and the app calls any conversion update method, such as [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md), | The device has 60 days after the user installs the app to send the first conversion value update. |
| The user launches the app and the app calls a conversion update method, such as [`updatePostbackConversionValue(_:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:completionhandler:).md) for ads signed with version 3 or earlier. | For ads signed with version 3 or earlier, the device sends install-validation postbacks 0–24 hours after a 24-hour timer expires following the final call to update the conversion value. The total delay from the final conversion update to receiving the postback is 24–48 hours. |

The minimum elapsed time between an ad impression and the time the ad network receives an install-validation postback is 24 to 48 hours. To reduce that time to 5 to 10 minutes during testing, see [`Testing ad attributions with a downloaded profile`](testing-ad-attributions-with-a-downloaded-profile.md).

Devices send one or more postbacks depending on the SKAdNetwork and iOS versions:

- For ads signed with SKAdNetwork 1 through 2.2, devices send a single, winning postback.
- Starting in iOS 14.6 for ads signed with version 3.0 or later, devices send a single winning postback, and up to five nonwinning postbacks.
- Starting in iOS 15, devices also send a copy of the winning postback to the advertised app’s developer, if the developer opts in to receive it.
- Starting in iOS 16.1 for ads signed using SKAdNetwork 4, devices can send up to three postbacks for the winning ad attribution, in three conversion windows.

Time-windows for events apply equally to winning and nonwinning postbacks.

##### Receive a Winning Postback

When multiple ad impressions qualify for install-validation postbacks, a device sends the winning postback to the ad network based on the following rules:

- In versions 1 through 2.1, the attribution goes to the most recent ad impression.
- Starting in version 2.2, the attribution goes to the most recent ad impression with the highest `fidelity-type` value.

The ad presentation option defines the `fidelity-type` value:

- StoreKit-rendered ads have the highest `fidelity-type` value of `1`.
- View-through ads have a `fidelity-type` value of `0`.

Indicate the `fidelity-type` when you generate the ad signature. Recorded ad impressions with a `fidelity-type` of `1` always take precedence over those with a `fidelity-type` of `0`. For example, if users see a StoreKit-rendered ad followed by a view-through ad for the same app, the StoreKit-rendered ad takes precedence over the view-through ad, despite the view-through ad being more recent. The source app can display StoreKit-rendered ads using  an [`SKOverlay`](skoverlay.md) or [`SKStoreProductViewController`](skstoreproductviewcontroller.md); the `fidelity-type` value is `1` in either case. For information about the fidelity of ads that an ad network presents on a Safari web page using the [`SKAdNetwork for Web Ads`](https://developer.apple.com/documentation/SKAdNetworkforWebAds) API, see [`signature`](https://developer.apple.com/documentation/SKAdNetworkforWebAds/signature).

In version 3 and later, the system indicates winning postbacks with a `did-win` parameter of value `true`.

##### Receive a Nonwinning Postback

Starting in iOS 14.6, devices can send multiple postbacks to ad networks that sign ads using version 3 or later. The system indicates nonwinning postbacks with a `did-win` parameter of value `false`. These postbacks don’t include `conversion-value` or `source-app-id`.

Each ad network can receive only one install-validation postback, winning or not winning. If you receive the winning postback, you don’t receive any nonwinning postbacks even if your ads have multiple qualifying ad impressions.

Up to five ad networks receive one nonwinning postback each. The system orders the recorded ad impressions using recency and `fidelity-type`, with the most recent ad views and highest `fidelity-type` taking precedence. Devices send nonwinning postbacks for the top five ad impressions from different ad networks that qualify for ad attribution.

##### Opt in to Receive a Copy of the Winning Postback

Starting in iOS 15, devices can send a copy of the winning install-validation postback to the developer of the advertised app. Developers opt in to receive the postback by specifying a server endpoint in their app’s `Info.plist` file. For more information about opting in and specifying the endpoint, see [`Configuring an advertised app`](configuring-an-advertised-app.md).

The postback that developers receive is an exact copy of the winning install-validation postback that the device sends to the ad network. The device sends the postback to developers at the same time it sends the winning postback to the ad network. To verify the postback, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

##### Limit View Through Ad Impressions

StoreKit records a maximum of 15 view-through ad impressions per source app before discarding the oldest one. The recorded ad impressions may advertise various products, and are each eligible to become pending attributions until they expire (after 24 hours).

##### Test Ad Impressions and Postbacks

Use the [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) framework to validate your ad impressions and test your postbacks by creating unit tests. For more information, see [`SKAdTestSession`](https://developer.apple.com/documentation/StoreKitTest/SKAdTestSession) and [`Testing and validating ad impression signatures and postbacks for SKAdNetwork`](https://developer.apple.com/documentation/StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork).

## See Also

- [Signing and providing ads](signing-and-providing-ads.md)
  Advertise apps by signing and providing StoreKit-rendered ads, view-through ads, or attributable web ads.
- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
  Learn about the data that postbacks may contain in each conversion window.
- [SKAdNetwork release notes](skadnetwork-release-notes.md)
  Learn about the features in each SKAdNetwork version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/receiving-ad-attributions-and-postbacks)*