# Configuring an advertised app

**Framework**: StoreKit

Prepare an advertised app to participate in ad campaigns.

#### Overview

An  is an app a user installs after viewing an ad that an ad network signs. The advertised app doesn’t require any configuration to participate in install validation. However, to register ad attributions, the app needs to call one of the methods that update conversion values when the app first launches. Those methods are: [`updatePostbackConversionValue(_:coarseValue:lockWindow:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:lockwindow:completionhandler:).md), [`updatePostbackConversionValue(_:coarseValue:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:coarsevalue:completionhandler:).md), and [`updatePostbackConversionValue(_:completionHandler:)`](skadnetwork/updatepostbackconversionvalue(_:completionhandler:).md).

Developers opt in to get copies of winning install-validation postbacks.

##### Configure Your App to Receive Copies of Winning Install Validation Postbacks

To opt in to receive copies of winning install-validation postbacks for your advertised app, add the [`NSAdvertisingAttributionReportEndpoint`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint) key in your app’s `Info.plist` file, and configure your server to receive the postbacks.

To add the key in your app’s `Info.plist` file:

1. Select `Info.plist` in the Project navigator in Xcode.
2. Click the Add button (+) beside a key in the property list editor and press Return.
3. Type the key name [`NSAdvertisingAttributionReportEndpoint`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint).
4. Choose String from the pop-up menu in the Type column.
5. Type a valid URL in the format of `“https://example.com”` that contains your domain name in place of `example.com`.

For more information about editing property lists, see [`Edit property lists`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev3f399a2a6).

The system uses the registrable part of the domain name you provide in the key, and ignores any subdomains. Using your domain name, the system generates a  and sends postbacks to that URL. To receive postbacks, your domain needs to have a valid SSL certificate. Configure your server to accept HTTPS POST messages at the following well-known path:

`https://example.com/.well-known/skadnetwork/report-attribution/`

Replace `example.com` with your domain name.

For more information about receiving postbacks, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

## See Also

- [Registering an ad network](registering-an-ad-network.md)
  Use the install-validation APIs for your ad campaigns after registering your ad network with Apple.
- [Configuring a source app](configuring-a-source-app.md)
  Set up a source app to participate in ad campaigns.
- [SKAdNetworkItems](../BundleResources/Information-Property-List/SKAdNetworkItems.md)
  An array of dictionaries containing a list of ad network IDs.
- [NSAdvertisingAttributionReportEndpoint](../BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint.md)
  The URL where Private Click Measurement and SKAdNetwork send attribution information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/configuring-an-advertised-app)*