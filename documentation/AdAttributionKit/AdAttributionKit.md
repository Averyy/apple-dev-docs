# AdAttributionKit

**Framework**: AdAttributionKit  
**Kind**: module

Present, process, and register postbacks for in-app ads in the App Store and alternative app marketplaces.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

#### Overview

AdAttributionKit helps advertisers measure the success of ad campaigns while helping maintain user privacy.

The API involves three participants:

- Ad networks that sign ads and receive postbacks after ads result in conversions
- Publisher apps that display ads from the ad networks
- Advertised apps that update conversion values as people engage with the app

Ad networks register with Apple to get an ad network ID and to use the API. Developers configure their apps to accept attributable ads from ad networks and receive copies of winning postbacks. For information about setup, see [`Registering an ad network`](registering-an-ad-network.md), [`Configuring a publisher app`](configuring-a-publisher-app.md), and [`Configuring an advertised app`](configuring-an-advertised-app.md).

Below is the path of an ad impression that wins ad attribution. The ad network serves an ad that an app displays. A person taps the ad and downloads or reengages with the advertised app.
![“A flow diagram showing the path of a winning ad impression. The diagram has two horizontal sections that contain rectangles. The top section is labeled Server and the bottom is labeled Device. The flow begins at the top left with the rectangle labeled Ad network serves ad. An arrow points down from it to a second rectangle in the bottom section labeled App presents ad, and another arrow points down from the second rectangle to a third labeled Download or reengagement. From the third rectangle, a dotted line on the right connects to a rectangle in the top section labeled Apple ensures crowd anonymity, and an arrow just below the dotted line connects to an adjacent rectangle labeled Person interacts with advertised app. A dotted line labeled Postback data tier connects downward from the Apple ensures crowd anonymity rectangle to the Person interacts with advertised app rectangle. An arrow connects the Person interacts with advertised app rectangle to a rectangle on the right labeled Multiple conversions that contains three subrectangles labeled Postback 1, Postback 2, and Postback 3. Arrows connect each subrectangle to a rectangle in the top section that contains two subrectangles labeled Ad Network (winning) and Developer.”](https://docs-assets.developer.apple.com/published/3b3d53d0451298e0d08b41db5f1d00eb/adattributionkit-winning-A%402x.png)

Apple determines a postback data tier for the conversion, and the device uses the tier later to determine the level of detail the postback can contain to help ensure crowd anonymity. For more information about the postback contents and the data tiers, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

If a person launches the app within an attribution time-window, the ad impression is eligible for postbacks. As that person engages with the app, the app updates the conversion value. The system provides three conversion windows if the ad network meets the criteria for conversion. The system sends the postbacks to the ad network, and to the app’s developer if they opt in to receive postbacks.

Devices send postbacks to multiple ad networks that sign their ads.

- One ad network receives postbacks, as part of multiple conversion windows, with a `did-win` parameter value of `true` for the ad impression that wins the ad attribution.
- For install conversions, up to five other ad networks receive a postback with a `did-win` parameter value of `false` if their ad impressions qualify for the attribution, but don’t win.
- For reengagement conversions, a single ad network may receive winning postbacks in multiple conversion windows. The framework doesn’t generate runner-up postbacks for reengagements.

The following diagram shows the path of ad impressions that qualify for, but don’t win, the ad attribution. Up to five ad networks receive a single nonwinning postback.

![“A flow diagram showing the path of a nonwinning ad impression. The diagram has two horizontal sections that contain rectangles. The top section is labeled Server and the bottom is labeled Device. The flow begins at the top left with the rectangle labeled Ad network serves ad. An arrow points down from it to a second rectangle in the bottom section labeled App presents ad, and another arrow points down from the second rectangle to a third labeled Download or reengagement. From the third rectangle, a dotted line on the right connects to a rectangle in the top section labeled Apple ensures crowd anonymity, and an arrow just below the dotted line connects to an adjacent rectangle labeled Person interacts with advertised app. A dotted line labeled Postback data tier connects downward from the Apple ensures crowd anonymity rectangle to the Person interacts with advertised app rectangle. An arrow connects the Person interacts with advertised app rectangle to a rectangle on the right labeled Postback that contains a stack of rectangles labeled Nonwinning postbacks. Arrows connect the rectangles to a collection of stacked rectangles in the top section labeled Ad Networks (nonwinning).”](https://docs-assets.developer.apple.com/published/ee17d89742ccefcdf3499b3c2fbcef6a/adattributionkit-non-winning-A%402x.png)

For more information about receiving ad attributions, including time-window details, information about install and reengagement conversions, and other constraints, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md). The information in the postback that Apple cryptographically signs doesn’t include user- or device-specific data. It can include values from the ad network and the advertised app if providing those values meets the privacy threshold that Apple sets. For more information about postback values and postback data tiers, see  [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md). For more information about the contents of postbacks, see [`Verifying a postback`](verifying-a-postback.md).

##### Present Ads Update Conversion Values and Receive Attribution

Each participant has specific responsibilities when using the APIs to present ads and receive attribution.

The ad network’s responsibilities are to:

- Register and provide its ad network identifier to developers. See [`Registering an ad network`](registering-an-ad-network.md).
- Serve signed ads to the publisher app. See [`Presenting ads in your app`](presenting-ads-in-your-app.md).
- Receive postbacks at the URL it establishes during registration.
- Verify the postbacks. See [`Verifying a postback`](verifying-a-postback.md).

The publisher app’s responsibilities are to:

- Add the ad network identifiers to its `Info.plist` file. See [`Configuring a publisher app`](configuring-a-publisher-app.md).
- Display ads that the ad network signs. See [`Presenting ads in your app`](presenting-ads-in-your-app.md).

The advertised app’s responsibilities are to:

- Register a conversion by updating the conversion value when a person first launches the app by calling one of the conversion updating methods, such as [`updateConversionValue(_:lockPostback:)`](postback/updateconversionvalue(_:lockpostback:).md).
- Optionally, continue to update the conversion value as the person engages with the app by calling one of the conversion updating methods, such as [`updateConversionValue(_:coarseConversionValue:lockPostback:)`](postback/updateconversionvalue(_:coarseconversionvalue:lockpostback:).md).
- Optionally, specify a server URL in its `Info.plist` file to receive a copy of the winning postback. See [`Configuring an advertised app`](configuring-an-advertised-app.md) .

Apple designs ad attribution APIs to help maintain user privacy. Apps don’t need to use [`App Tracking Transparency`](https://developer.apple.comhttps://developer.apple.com/documentation/apptrackingtransparency) before calling ad attribution APIs, and can call these APIs regardless of their tracking authorization status. For more information about privacy, see [`User privacy and data use`](https://developer.apple.comhttps://developer.apple.com/app-store/user-privacy-and-data-use/).

## Topics

### Essentials
- [Understanding AdAttributionKit and SKAdNetwork interoperability](adattributionkit-skadnetwork-interoperability.md)
  Learn how attribution APIs interact to deliver ad impressions.
- [Presenting ads in your app](presenting-ads-in-your-app.md)
  Render different ad styles in your app.
- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
  Understand timeframes and priorities for ad impressions that result in ad attributions, and how impressions qualify for postbacks.
- [Identifying conversion values with conversion tags](conversion-tags.md)
  Use conversion tags to identify and update specific postbacks when you have overlapping conversion windows.
### Ad network registration and configuration
- [Registering an ad network](registering-an-ad-network.md)
  Use the AdAttributionKit APIs for your ad campaigns after registering your ad network with Apple.
- [Configuring a publisher app](configuring-a-publisher-app.md)
  Set up a publisher app to participate in ad campaigns.
- [Configuring an advertised app](configuring-an-advertised-app.md)
  Prepare an advertised app to participate in ad campaigns.
### Ad attribution testing
- [Testing ad attributions with Developer Mode](testing-adattributionkit-with-developer-mode.md)
  Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.
- [Creating postbacks in developer settings](creating-postbacks-in-developer-settings.md)
  Test development postbacks for your advertised app without interacting with ads from a publisher app.
- [Testing ad attributions with a downloaded profile](testing-ad-attributions-with-a-downloaded-profile.md)
  Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.
### Signatures
- [Generating JWS impressions](generating-jws-impressions.md)
  Create a JSON Web Signature (JWS) for use with app impressions in AdAttributionKit.
### App impressions
- [struct AppImpression](appimpression.md)
  A structure that represents an attributable impression the developer generates in response to a person’s interaction with an ad in an app.
### Postbacks
- [struct Postback](postback.md)
  A structure that provides methods you use to update conversion values for ad attributions.
- [struct PostbackUpdate](postbackupdate.md)
  Values you use to update properties in a postback, such as the conversion value.
- [enum CoarseConversionValue](coarseconversionvalue.md)
  Values that describe developer-defined, relative-attribution conversion values.
### Postback verification and parameter identification
- [Verifying a postback](verifying-a-postback.md)
  Ensure the validity of a postback you receive after an ad conversion by verifying its cryptographic signature.
- [Identifying the parameters in a postback](identifying-the-parameters-in-a-postback.md)
  Interpret postback properties to understand the attribution report.
### Errors
- [enum AdAttributionKitError](adattributionkiterror.md)
  Values that describe ad attribution error conditions.
### Articles
- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
  Learn about the data that postbacks can contain in each conversion window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AdAttributionKit)*