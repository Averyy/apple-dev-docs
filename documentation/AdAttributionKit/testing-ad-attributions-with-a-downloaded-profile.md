# Testing ad attributions with a downloaded profile

**Framework**: AdAttributionKit

Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.

#### Overview

> ❗ **Important**: You can only use the AdAttributionKit testing profile for devices running OS versions earlier than iOS 18. In iOS 18 and later, the testing profile no longer works in AdAttributionKit or SKAdNetwork, so you need to use the AdAttributionKit Developer Mode. For more information see, [`Testing ad attributions with Developer Mode`](testing-adattributionkit-with-developer-mode.md).

You can only use the AdAttributionKit testing profile for devices running OS versions earlier than iOS 18. In iOS 18 and later, the testing profile no longer works in AdAttributionKit or SKAdNetwork, so you need to use the AdAttributionKit Developer Mode. For more information see, [`Testing ad attributions with Developer Mode`](testing-adattributionkit-with-developer-mode.md).

You can reduce the time-window for receiving ad attribution postbacks by installing an AdAttributionKit testing profile on your test device.

Download the latest profile by signing in to your [`Apple Developer account`](https://developer.apple.comhttps://developer.apple.com/) and then downloading the [`AdAttributionKit profile`](https://developer.apple.comhttps://developer.apple.com/services-account/download?path=/Developer_Tools/AdAttributionKit_Profile/AdAttributionKitDeveloperTestingProfile.mobileconfig). This profile is compatible with both AdAttributionKit and [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork).

For information about installing profiles, see [`Install a configuration profile on your iPhone or iPad`](https://developer.apple.comhttps://support.apple.com/en-us/102400). You can install this profile on devices running iOS or iPadOS 17.4 or later.

With this profile, the installed app has 5 minutes to update the conversion value after initially registering. The device sends the postback within another 5 minutes after the rolling 5-minute timer for conversion updates expires. Using this profile reduces the conversion value update and postback window from 24–48 hours to 5–10 minutes.

This testing profile expires 2 weeks after you install it on the device. To continue testing, download the latest profile and reinstall it.

> **Note**: To test ad attributions, you need to log in to the device with a production Apple ID. AdAttributionKit doesn’t support sandbox Apple IDs.

To test ad attributions, you need to log in to the device with a production Apple ID. AdAttributionKit doesn’t support sandbox Apple IDs.

#### Inspect Postbacks Using an Http Proxy

With this installed profile, the system can send AdAttributionKit postbacks through an HTTP proxy that you configure. By using an HTTP proxy, you can monitor the HTTP traffic between your device and the network, including AdAttributionKit postbacks. To configure the HTTP proxy, follow these steps on a testing device:

1. Choose Settings > Wi-Fi and select the Wi-Fi network you’re connected to.
2. Under the HTTP Proxy heading, select Configure Proxy.
3. Select Manual to configure the Server, Port, and Authentication settings for your proxy, or select Automatic to provide a URL for your proxy.
4. Tap Save.

With the installed profile, the AdAttributionKit postbacks that the device sends go through the proxy.

## See Also

- [Testing ad attributions with Developer Mode](testing-adattributionkit-with-developer-mode.md)
  Reduce the time-window for ad attributions and inspect postbacks using a proxy during testing.
- [Creating postbacks in developer settings](creating-postbacks-in-developer-settings.md)
  Test development postbacks for your advertised app without interacting with ads from a publisher app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/testing-ad-attributions-with-a-downloaded-profile)*