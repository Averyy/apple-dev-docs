# Testing ad attributions with Developer Mode

**Framework**: Adattributionkit

Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.

#### Overview

> ❗ **Important**: For devices running OS versions earlier than iOS 18, use the AdAttributionKit testing profile on your test device. For more information, see [`Testing ad attributions with a downloaded profile`](testing-ad-attributions-with-a-downloaded-profile.md).

In iOS 18 and later, you can reduce the time-window for receiving AdAttributionKit postbacks by enabling Developer Mode on your test device. Developer Mode is compatible with both AdAttributionKit and SKAdNetwork. For more information, see [`Enabling Developer Mode on a device`](https://developer.apple.com/documentation/Xcode/enabling-developer-mode-on-a-device).

After enabling Developer Mode, access the developer settings in Settings on your test device. Then scroll down to the Ad Attribution Testing section and enable the AdAttributionKit Developer Mode switch, as the screenshot below shows:

![An image of the iOS Developer Mode settings that shows several test settings, including the switch that enables development testing for AdAttributionKit.](https://docs-assets.developer.apple.com/published/eb124a690f0cb16a89a1e285acb57f65/ad-attribution-testing%402x.png)

> ❗ **Important**: Enabling Developer Mode reduces the privacy protections the system provides. Use this mode only during development or testing. This setting automatically turns off after two weeks.

To test ad attributions, you need to log in to the device with a production Apple ID. AdAttributionKit doesn’t support sandbox Apple IDs.

#### Create Development Impressions and Postbacks

In iOS 18 and later, you sign development impressions to receive development postbacks. Development impressions allow you to test your integration with reduced time-windows using Developer Mode. After a conversion event occurs using a development impression, the system creates development postbacks. Development postbacks aren’t subject to the rate limits that reengagement in AdAttributionKit imposes, and they generate postbacks with the highest data tier that Crowd Anonymity allows.

AdAttributionKit and SKAdNetwork both support development impressions and postbacks. Configuring development impressions can vary based on the ad framework you’re using, as follows:

- In AdAttributionKit, you create development impressions by specifying a publisher item identifier of `0` in the impression’s JSON web signature (JWS).
- Similarly, in SKAdNetwork for ads that apps show, you create development impressions by setting a source App Store identifier of `0`.
- In SKAdNetwork for web ads, the system registers development impressions for all web ads as long as Developer Mode is in an enabled state at the time of the click.

AdAttributionKit and SKAdNetwork 4 create a winning set of three development postbacks as part of multiple conversion windows. SKAdNetwork 3 and earlier create a single winning postback. For more information, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

You can test development postbacks using the production time-windows, or reduce their time-windows by enabling Developer Mode.

> **Note**: The system prioritizes production impressions over development impressions for any conversion event. If production and development impressions are present during a conversion, the system ignores development impressions.

##### Verify Development Postbacks

The system signs development postbacks with a different private key from production postbacks to help distinguish them. The system uses the `apple-development-identifier/0` `kid` to identify signed development postbacks in end-to-end flows.

The steps for verifying development postback signatures are identical to the steps for production postbacks, with the exception of the key you use. For more information on the public key for development postbacks and verifying a postback’s JWS signature, see [`Verifying a postback`](verifying-a-postback.md).

#### Reduce Time Windows Using Developer Mode

Enabling Developer Mode reduces the time-window for receiving development postbacks from the device. Developer Mode only affects the time-windows of development postbacks. Postbacks that the system generates from production impressions use the full time-windows.

When you enable Developer Mode, the framework reduces each development postback’s conversion window to 3 minutes instead of the full duration to allow for faster testing. The conversion window begins when the installed app first updates the conversion value. The first window spans 0 to 3 minutes, the second window spans 3 to 6 minutes, and the third window spans 6 to 9 minutes. Developer Mode reduces the postback delay from 24 to 48 hours to 5 to 10 minutes.

#### Inspect Postbacks Using an Http Proxy

When you enable Developer Mode, the system can send AdAttributionKit postbacks through an HTTP proxy that you configure. By using an HTTP proxy, you can monitor the HTTP traffic between your device and the network, including AdAttributionKit postbacks. To configure the HTTP proxy, follow these steps on a testing device:

1. Choose Settings > Wi-Fi and select the Wi-Fi network you’re connected to.
2. Under the HTTP Proxy heading, select Configure Proxy.
3. Select Manual to configure the Server, Port, and Authentication settings for your proxy, or select Automatic to provide a URL for your proxy.
4. Tap Save.

When you enable Developer Mode, the AdAttributionKit postbacks that the device sends go through the proxy.

## See Also

- [Creating postbacks in developer settings](creating-postbacks-in-developer-settings.md)
  Test development postbacks for your advertised app without interacting with ads from a publisher app.
- [Testing ad attributions with a downloaded profile](testing-ad-attributions-with-a-downloaded-profile.md)
  Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AdAttributionKit/testing-adattributionkit-with-developer-mode)*