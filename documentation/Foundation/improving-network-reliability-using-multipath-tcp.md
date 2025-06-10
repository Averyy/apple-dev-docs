# Improving network reliability using Multipath TCP

**Framework**: Foundation

Use the available radios in iOS devices to improve your app’s network reliability and performance.

#### Overview

When using your app on an iOS device, users are likely to move in and out of range of Wi-Fi, switching to cellular networks and back again.

Multipath TCP improves the performance of your app when a user is in a location with limited Wi-Fi and while their device is transitioning to and from cellular data usage. In its default configuration, a URL session uses a single radio for a network call, preferring Wi-Fi over cellular. However, with Multipath TCP enabled, the URL session initiates the request on both radios and selects the more responsive of the two with a preference for Wi-Fi.

##### Enable Multipath Tcp in Your App

These steps are required:

- Enable the [`Multipath Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.multipath) in the Xcode Capabilities pane for your app target.
- Set the [`multipathServiceType`](urlsessionconfiguration/multipathservicetype-swift.property.md) property in [`URLSessionConfiguration`](urlsessionconfiguration.md) to a mode other than `none`. For most cases, the handover mode is the best option. This mode provides your users with a seamless transition between Wi-Fi and cellular, allowing uninterrupted usage of your app. (For information about other modes, see [`URLSessionConfiguration.MultipathServiceType`](urlsessionconfiguration/multipathservicetype-swift.enum.md).)

While the user’s device is connected to a reliable Wi-Fi network, your app uses only Wi-Fi, and no cellular data is consumed. As the user leaves the range of the Wi-Fi network and the signal starts to deteriorate, Multipath TCP begins transitioning data usage to the cellular network to provide a seamless transition.

> ❗ **Important**:  Multipath TCP requires the destination server to have Multipath TCP enabled. Many commercial load balancers already support Multipath TCP, and you can enable it in the configuration. For Linux-based servers, the Linux kernel with Multipath TCP is available at the [`Multipath TCP`](https://developer.apple.comhttps://multipath-tcp.org) website.

##### Limitations When Using Multipath Tcp with Wi Fi Assist

Because Wi-Fi Assist is a user selectable, device-wide option, there are a few limitations when using Multipath TCP with that option enabled:

- Wi-Fi Assist prevents flows from using cellular data when your app is in the background.
- Wi-Fi Assist limits the amount of data that your app can send over cellular networks. When the limit is reached, Multipath TCP is disabled.

Wi-Fi Assist is integrated into the [`URLSession`](urlsession.md) API and doesn’t require any changes to the session configuration. At the start of each URL session task, Wi-Fi Assist determines whether to use Wi-Fi or cellular data for the connection.

After the URL session task begins, Wi-Fi Assist doesn’t change from Wi-Fi to cellular or from cellular to Wi-Fi. Multipath TCP extends the performance-improving capabilities of Wi-Fi Assist to provide seamless radio transition and improved throughput.

> **Note**:  When using a developer-enabled device for testing, you can disable the Wi-Fi Assist data limitation in the developer section of the Settings app.

## See Also

- [var multipathServiceType: URLSessionConfiguration.MultipathServiceType](urlsessionconfiguration/multipathservicetype-swift.property.md)
  A service type that specifies the Multipath TCP connection policy for transmitting data over Wi-Fi and cellular interfaces.
- [URLSessionConfiguration.MultipathServiceType](urlsessionconfiguration/multipathservicetype-swift.enum.md)
  Constants that specify the type of service that Multipath TCP uses.
- [Multipath Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/improving-network-reliability-using-multipath-tcp)*