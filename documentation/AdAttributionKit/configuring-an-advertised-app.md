# Configuring an advertised app

**Framework**: AdAttributionKit

Prepare an advertised app to participate in ad campaigns.

#### Overview

An advertised app is an app someone installs or reengages with after viewing an ad that an ad network signs. After a conversion event occurs, the system may create postbacks for the advertised app. The advertised app needs to call one of the methods that update the postback’s conversion value at least once to begin the postback’s conversion window. It’s recommended that the app updates the conversion value when the app first launches to begin the conversion window. You can use the following methods to update the conversion value, depending on your use case: [`updateConversionValue(_:)`](postback/updateconversionvalue(_:).md), [`updateConversionValue(_:coarseConversionValue:lockPostback:)`](postback/updateconversionvalue(_:coarseconversionvalue:lockpostback:).md), and [`updateConversionValue(_:lockPostback:)`](postback/updateconversionvalue(_:lockpostback:).md).

Developers opt in to get copies of winning postbacks.

#### Configure Your App to Receive Copies of Winning Postbacks

To opt in to receive copies of winning postbacks for your advertised app, add the `AttributionCopyEndpoint` key your app’s Xcode project’s Information Property List , and configure your server to receive the postbacks.

To add the key in your app’s Information Property List through the Info pane in Xcode:

1. Select your app’s target in the Project navigator in Xcode.
2. Select the Info pane in the project settings.
3. Click the Add button (+) beside a key in the property list editor.
4. Type the key name `AdAttributionKit` and select `AdAttributionKit - Postback Copy URL` from the pop-up menu.
5. Choose String from the pop-up menu in the Type column.
6. Type a valid URL in the format of `https://example.com` that contains your domain name in place of `example.com`.

For more information about editing property lists, see [`Edit property lists`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev3f399a2a6).

The system uses the registrable part of the domain name you provide in the key, and ignores any subdomains. Using your domain name, the system generates a well-known path and sends postbacks to that URL. To receive postbacks, your domain needs to have a valid SSL certificate. Configure your server to accept HTTPS POST messages at the following well-known path:

```None
https://example.com/.well-known/appattribution/report-attribution/
```

Replace `example.com` with your domain name.

> **Note**: If your app uses the [`AdAttributionKit`](AdAttributionKit.md) framework and the [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) class, add the AdAttributionKit and `SKAdNetwork` postback copy URLs to your app’s Information Property List through the Info pane in Xcode. For more information, see [`Managing your app’s information property list values`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

For more information about receiving postbacks, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

#### Opt in to Receive Copies of Winning Reengagement Postbacks

To receive copies of winning reengagement postbacks, you need to add an additional key to your app’s Information Property List. Follow these steps:

1. Select your app’s target in the Project navigator in Xcode.
2. Select the Info pane in the project settings.
3. Click the Add button (+) beside a key in the property list editor.
4. Type the key name `AdAttributionKit` and select `AdAttributionKit - Opt in for Reengagement Postback Copies` from the pop-up menu.
5. Choose Boolean from the pop-up menu in the Type column.
6. Set its value to `YES`.

## See Also

- [Registering an ad network](registering-an-ad-network.md)
  Use the AdAttributionKit APIs for your ad campaigns after registering your ad network with Apple.
- [Configuring a publisher app](configuring-a-publisher-app.md)
  Set up a publisher app to participate in ad campaigns.
- [Configuring attribution rules for your app](configuring-attribution-rules-for-your-app.md)
  Tune aspects of attribution flow, including the time available to register impressions and the minimum time your app is willing to accept conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/configuring-an-advertised-app)*