# Testing ad attributions with a downloaded profile

**Framework**: StoreKit

Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.

#### Overview

You can reduce the time window for receiving ad attribution postbacks by installing an SKAdNetwork testing profile on your test device.

> ❗ **Important**:  To download the latest profile, see the [`AdAttributionKit`](https://developer.apple.com/documentation/AdAttributionKit) article on [`Testing ad attributions with a downloaded profile`](https://developer.apple.com/documentation/AdAttributionKit/testing-ad-attributions-with-a-downloaded-profile). This profile is compatible with both AdAttributionKit and SKAdNetwork.

For information about installing profiles, see [`Install a configuration profile on your iPhone or iPad`](https://developer.apple.comhttps://support.apple.com/en-us/HT209435). You can install this profile on devices running iOS or iPadOS 14 or later.

With this profile, the installed app has five minutes to update the conversion value after initially registering. The device sends the postback within another five minutes after the rolling five-minute timer for conversion updates expires. Using this profile reduces the conversion value update and postback window from 24–48 hours to 5–10 minutes.

This testing profile expires two weeks after you install it on the device. To continue testing, download the latest profile and reinstall it.

##### Log in with an Apple Account to Test Ad Attributions

To test ad attributions, you must log in to the device with a production Apple Account. SKAdNetwork doesn’t support Sandbox Apple Accounts.

##### Inspect Postbacks Using an Http Proxy

On devices running iOS 14.7 and later with this profile installed, the system can send SKAdNetwork postbacks through an HTTP proxy that you configure. By using an HTTP proxy, you can monitor the HTTP traffic between your device and the network, including SKAdNetwork postbacks.

To configure the HTTP proxy, do the following on a testing device:

1. Go to Settings > Wi-Fi and select the Wi-Fi network you’re connected to.
2. Under the HTTP Proxy heading, select Configure Proxy.
3. Select Manual to configure the Server, Port, and Authentication settings for your proxy, or select Automatic to provide a URL for your proxy.
4. Tap Save.

With the profile installed, the SKAdNetwork postbacks that the device sends now go through the proxy you configured.

## See Also

- [Testing and validating ad impression signatures and postbacks for SKAdNetwork](../StoreKitTest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md)
  Validate your ad impressions and test your postbacks by creating unit tests using the StoreKit Test framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-ad-attributions-with-a-downloaded-profile)*