# Associated Domains Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The associated domains for specific services, such as shared web credentials, universal links, and App Clips.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.15+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

#### Discussion

This key specifies a list of domains for each enabled service. Add an associated domain to the list in the following format:

```swift
<service>:<fully qualified domain>
```

Services include:

> **Note**:  In macOS 11 and later and iOS 14 and later, apps request `apple-app-site-association` files from an Apple-managed content delivery network (CDN) specifically for associated domains, instead of directly from your web server. If the CDN has an old version of the file, or doesn’t already have a copy of the file, it connects to your web server to obtain the latest version.

 In macOS 11 and later and iOS 14 and later, apps request `apple-app-site-association` files from an Apple-managed content delivery network (CDN) specifically for associated domains, instead of directly from your web server. If the CDN has an old version of the file, or doesn’t already have a copy of the file, it connects to your web server to obtain the latest version.

If you use a private web server, which is unreachable from the public internet, while developing your app, enable the alternate mode feature to bypass the CDN and connect directly to your server. To do this, add a query string to your associated domains entitlement, as shown in the following example:

```console
<service>:<fully qualified domain>?mode=<alternate mode>
```

Where `alternate mode` is one of the following:

To enable associated domains, add the Associated Domains capability to your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

> ❗ **Important**:  For watchOS apps, you must add the Associated Domains capability to the WatchKit Extension target.

 For watchOS apps, you must add the Associated Domains capability to the WatchKit Extension target.

## See Also

- [Supporting associated domains](../Xcode/supporting-associated-domains.md)
  Connect your app and a website to provide both a native app and a browser experience.
- [Creating an App Clip with Xcode](../AppClip/creating-an-app-clip-with-xcode.md)
  Add an App Clip target to your Xcode project and share code between the App Clip and its corresponding full app.
- [Network Extensions Entitlement](entitlements/com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
- [Personal VPN Entitlement](entitlements/com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
- [com.apple.developer.networking.multicast](entitlements/com.apple.developer.networking.multicast.md)
  A Boolean value that indicates whether an app can send or receive IP multicast traffic.
- [com.apple.developer.associated-domains.applinks.read-write](entitlements/com.apple.developer.associated-domains.applinks.read-write.md)
  A Boolean value that indicates whether the app can use universal links.
- [com.apple.developer.networking.manage-thread-network-credentials](entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [5G Network Slicing App Category](entitlements/com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [5G Network Slicing Traffic Category](entitlements/com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](entitlements/com.apple.developer.networking.vmnet.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.associated-domains)*