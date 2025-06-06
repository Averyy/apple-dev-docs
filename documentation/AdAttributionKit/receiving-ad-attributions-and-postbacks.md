# Receiving ad attributions and postbacks

**Framework**: Adattributionkit

Understand timeframes and priorities for ad impressions that result in ad attributions, and how impressions qualify for postbacks.

#### Overview

Ad networks receive attributions in the form of postbacks. Before an ad network can receive a postback, the following events need to occur within limited time-windows:

- Ad networks sign and present ads in the form of StoreKit-rendered ads and custom-rendered ads.
- Someone installs or reengages with the advertised app.
- A person or AdAttributionKit launches the app.
- The app updates the conversion values when the app launches, and continues to update it as needed.

The following table shows the time-windows for the events:

| Event | Time-window |
| --- | --- |
| View-through custom or StoreKit rendered ads | A person has 24 hours to install the app. |
| Click-through custom or StoreKit-rendered ads | A person has 30 days to install the app. |
| Someone installs the app. | The device has 60 days to send the first conversion value update. |
| Someone reengages with the app. | The device has 2 days to send the first conversion value update. |

The minimum elapsed time between a conversion event for the advertised app and the time the ad network receives a postback is 24 to 48 hours. To reduce that time to 5 to 10 minutes during testing, see [`Testing ad attributions with Developer Mode`](testing-adattributionkit-with-developer-mode.md).

Time-windows for events apply equally to winning and nonwinning postbacks.

#### Process Install Conversions

Install conversion events occur when someone installs the app from the App Store or alternative app marketplace after interacting with an AdAttributionKit ad. Install conversions create winning and nonwinning postbacks for ad networks that had qualifying ad impressions.

AdAttributionKit represents install postbacks as either `download` or `redownload` in the postback’s `conversion-type` field. For more information about the postback parameters, see [`Identifying the parameters in a postback`](identifying-the-parameters-in-a-postback.md).

##### Receive a Winning Postback

When multiple ad impressions qualify for postbacks from an install conversion, the device sorts the ad impressions and selects a single winner. The system considers ad impressions from both AdAttributionKit and SKAdNetwork when evaluating the attribution after someone installs the advertised app. For more information about the ad sorting criteria, see [`Understanding AdAttributionKit and SKAdNetwork interoperability`](adattributionkit-skadnetwork-interoperability.md).

> **Note**: Install conversions always produce winning postbacks if there’s a qualifying ad impression, subject to their Crowd Anonymity tier.

##### Receive a Nonwinning Postback

Each ad network can receive only one postback, winning or nonwinning. If you receive the winning postback, you don’t receive any nonwinning postbacks even if your ads have multiple qualifying ad impressions. Up to five ad networks receive one nonwinning postback each. The system sorts the recorded ad impressions based on recency and whether they are click-through or view-through, with the most recent ad views and click-through taking precedence. Devices send nonwinning postbacks for the top five ad impressions from different ad networks that qualify for ad attribution.

#### Handle Reengagement Conversions

Reengagement conversions occur when someone already has the advertised app installed and taps a custom rendered ad, or they tap the Open button on a StoreKit rendered ad. Reengagement only involves the impression that drives the conversion, so there are no nonwinning postbacks. Additionally, the system only processes reengagement conversions as a result of click interactions on ads. The system doesn’t create reengagement postbacks from view-through ads.

In iOS 18 and later, AdAttributionsKit allows publisher apps to pass a reengagement URL. The system opens the reengagement URL if the device has the advertised app installed, and the URL is a registered universal link for the advertised app. The system also appends the query parameter `AdAttributionKitReengagementOpen` to the URL to indicate AdAttributionKit opened it. When the advertised app receives the universal link, it can check the URL for the presence of this parameter to determine whether AdAttributionKit opened it. The [`reengagementOpenURLParameter`](postback/reengagementopenurlparameter.md) property also defines this parameter as a constant. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

The system also strips known tracking parameters from the URL before delivering them to the advertised app.

It’s possible a reengagement conversion may occur for an app when there’s already an existing install or reengagement conversion for that app. In this case, the system locks the active postbacks from the prior conversion and schedules them for transmission. AdAttributionsKit removes postbacks from the prior conversions that you haven’t registered and replaces them with any postbacks from the latest conversion.

AdAttributionsKit represents reengagement postbacks as `reengagement` in the postback’s `conversion-type` field. For more information about the postback parameters, see [`Identifying the parameters in a postback`](identifying-the-parameters-in-a-postback.md).

> ❗ **Important**: The system doesn’t always produce postbacks after a reengagement. The device is subject to reengagement limits on a monthly per-app basis, as well as a yearly per-device basis. The parameter AdAttributionsKit appends to the URL is always present on the URL, however, even if AdAttributionsKit doesn’t create reengagement postbacks.

#### Update Postbacks By Their Conversion Type

Advertisers may attribute conversion values differently inside their app, depending on the conversion type: `install` or `reengagement`. In iOS 18 and later, use [`updateConversionValue(_:)`](postback/updateconversionvalue(_:).md) to specify which types of postbacks to update. The system defaults to updating all types of postbacks if you specify `nil` for the conversion types, or if you use an API that doesn’t contain conversion types to update the conversion value, such as [`updateConversionValue(_:coarseConversionValue:lockPostback:)`](postback/updateconversionvalue(_:coarseconversionvalue:lockpostback:).md).

For example in an onboarding flow, an advertiser can attribute conversion values differently, depending on whether the conversion is an install or a reengagement.

```swift
private func attributeCustomerAccountCreated() async {
    do {
        // Updates any active install postbacks with a conversion value of 20.
        let installPostbackUpdate = PostbackUpdate(fineConversionValue: 20, lockPostback: false, conversionTypes: [.install])
        try await Postback.updateConversionValue(installPostbackUpdate)

        // Updates any active reengagement postbacks with a conversion value of 12.
        let reengagementPostbackUpdate = PostbackUpdate(fineConversionValue: 12, lockPostback: false, conversionTypes: [.reengagement])
        try await Postback.updateConversionValue(reengagementPostbackUpdate)
    }
    catch {
        print("Failed to update postback conversion value: \(error)")
    }
}
```

#### Opt in to Receive a Copy of the Winning Postback

Devices can send a copy of the winning postback to the developer of the advertised app. Developers opt in to receive the postback by specifying a server endpoint in their app’s `Info.plist` file. For more information about opting in and specifying the endpoint, see [`Configuring an advertised app`](configuring-an-advertised-app.md). The postback that developers receive is an exact copy of the winning postback that the device sends to the ad network. The device sends the postback to developers at the same time it sends the winning postback to the ad network. To verify the postback, see [`Verifying a postback`](verifying-a-postback.md).

#### Limit the Number of View Through Ad Impressions From a Publisher App

AdAttributionKit records a maximum of 15 view-through ad impressions per publisher app before discarding the oldest one. The recorded ad impressions may advertise various products, and are each eligible to become pending attributions until they expire (after 24 hours).

## See Also

- [Understanding AdAttributionKit and SKAdNetwork interoperability](adattributionkit-skadnetwork-interoperability.md)
  Learn how attribution APIs interact to deliver ad impressions.
- [Presenting ads in your app](presenting-ads-in-your-app.md)
  Render different ad styles in your app.
- [Identifying conversion values with conversion tags](conversion-tags.md)
  Use conversion tags to identify and update specific postbacks when you have overlapping conversion windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AdAttributionKit/receiving-ad-attributions-and-postbacks)*