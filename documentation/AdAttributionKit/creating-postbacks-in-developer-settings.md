# Creating postbacks in developer settings

**Framework**: AdAttributionKit

Test development postbacks for your advertised app without interacting with ads from a publisher app.

#### Overview

Use the AdAttributionKit Development Postbacks tool in the developer settings to create development postbacks for your advertised app. This tool allows you to test your AdAttributionKit functionality without interacting with ads from a publisher app or publishing your app in the App Store or an alternate marketplace. Test your app from various distribution methods, such as those you build with Xcode, ad-hoc, or TestFlight.

This tool also allows you to configure the amount of data that returns in the postback to simulate different Crowd Anonymity tiers so you can validate server logic for receiving those postbacks. For more information about Crowd Anonymity tiers, see [`Identifying the parameters in a postback`](identifying-the-parameters-in-a-postback.md).

You can access the AdAttributionKit tools by enabling Developer Mode on your test device. For more information, see [`Enabling Developer Mode on a device`](https://developer.apple.com/documentation/Xcode/enabling-developer-mode-on-a-device).

> ❗ **Important**: Enabling Developer Mode reduces the privacy protections the system provides. Use this mode only during development or testing. This setting automatically turns off after two weeks.

After enabling Developer Mode, access the developer settings on your test device by choosing Settings > Developer. Then scroll down to the Ad Attribution Testing section and tap Development Postbacks, as the screenshot below shows:

![An image of the iOS Developer Mode settings that shows a number of test settings, including the switch that enables development testing for AdAttributionKit.](https://docs-assets.developer.apple.com/published/eb124a690f0cb16a89a1e285acb57f65/ad-attribution-testing%402x.png)

#### Create a Development Postback

To create development postbacks for your app, type in your app’s bundle identifier and tap the Configure Development Postbacks button.

![An image of the AdAttributionKit Developer Mode that shows the development postback setup form where someone can enter the bundle ID for their app and further configure, transmit, or clear development postbacks.](https://docs-assets.developer.apple.com/published/2bef515baed7473cb9948234352ecafa/development-postbacks%402x.png)

> **Note**: An app with the specified bundle identifier needs to exist on your device. The system doesn’t allow you to create development postbacks for an app that isn’t installed.

##### Provide the Server Url to Process the Postback

Provide the URL of the server to receive the development postbacks. AdAttributionKit sends the postback to this destination when the postback is eligible for transmission.

![An image of the AdAttributionKit postback destination form that allows someone to enter the URL to use to have the framework send development postback information to the developer's server.](https://docs-assets.developer.apple.com/published/c2ce1f1b0d9a6da8bc71a58b6cded827/postback-destination%402x.png)

You can also tap Use Developer Postback URL to generate the full postback copy URL that the app’s information property list specifies. This is the same URL that AdAttributionKit generates when creating developer copies of postbacks in full end-to-end flows. For more information on receiving developer postback copies, see [`Configuring an advertised app`](configuring-an-advertised-app.md).

> **Note**: It’s a best practice to use a server URL that’s different than the production server URL for testing. The testing URL can include a custom path that’s difficult to guess, such as a UUID that you can disable once the test is complete.

##### Fill in Postback Properties

Configure each property of the postback in this section. You can create variations of all properties in the postback, including the view or click interaction type, conversion types, and one or three conversion windows.

![An image of the AdAttributionKit postback properties form that allows someone to set values that the framework sends in a development postback.](https://docs-assets.developer.apple.com/published/44703067d263db4201cd39afcd48add3/postback-properties%402x.png)

##### Add a Conversion Tag

Fill in a conversion tag if you’re testing the overlapping conversion windows feature. After you specify a conversion tag, you can update the postback by setting the [`conversionTag`](postbackupdate/conversiontag.md) property and calling [`updateConversionValue(_:)`](postback/updateconversionvalue(_:).md). For more information on overlapping conversion windows, see [`Identifying conversion values with conversion tags`](conversion-tags.md).

##### Adjust Postback Data Tiers

AdAttributionKit uses Crowd Anonymity to control the amount of data the framework returns in postbacks in production flows. For each postback, adjust the amount of data that AdAttributionKit includes in the postback.

![An image of the AdAttributionKit postback destination form that allows someone to enter the URL to use for the framework to send development postback information to the developer's server.](https://docs-assets.developer.apple.com/published/4f5311c8ed111beb883e3315c8ac3bed/crowd-anonymity-tiers%402x.png)

You can use this to test that your server logic is processing different postback data granularities correctly. For more information about Crowd Anonymity, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

##### Examine the Jws of the Development Postback

Postbacks you create using the developer settings have notable differences from postbacks you create in a full end-to-end flow:

- The `kid` property of the JWS header is `apple-development-identifier/1`.
- The `ad-network-identifier` property of the JWS payload is `development.adattributionkit`.
- If you build and install your app with Xcode, it has an `advertised-item-identifier` of `0`. If you install the app from the App Store or alternate marketplace, it has an `advertised-item-identifier` matching the item identifier of your app in App Store Connect.

The system signs development postbacks with a different private key from production postbacks to help distinguish them. The steps for verifying development postback signatures are identical to the steps for production postbacks, with the exception of the key you use. For more information on the public key for development postbacks and verifying a postback’s JWS signature, see [`Verifying a postback`](verifying-a-postback.md).

#### Transmit Eligible Development Postbacks on Demand

The device sends eligible postbacks automatically, which can take a few minutes. To send postbacks immediately, you can transmit eligible development postbacks on-demand by tapping the Transmit Development Postbacks button.

AdAttributionKit treats a postback as eligible for transmission after its conversion window elapses or you lock it by calling the [`updateConversionValue(_:)`](postback/updateconversionvalue(_:).md) API. The duration of the postback’s conversion window depends on whether you enable AdAttributionKit Developer Mode. For more information about Developer Mode, see [`Testing ad attributions with Developer Mode`](testing-adattributionkit-with-developer-mode.md).

#### Clear Development Postbacks

Tapping Clear Development Postbacks deletes all development postbacks currently in the system, allowing you to return the device to a known starting point.

## See Also

- [Testing ad attributions with Developer Mode](testing-adattributionkit-with-developer-mode.md)
  Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.
- [Testing ad attributions with a downloaded profile](testing-ad-attributions-with-a-downloaded-profile.md)
  Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/creating-postbacks-in-developer-settings)*