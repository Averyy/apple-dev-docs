# com.apple.developer.networking.carrier-constrained.appcategory

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The key that defines an app’s category for accessing a carrier-provided satellite network.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `com.apple.developer.networking.carrier-constrained.appcategory`
- **Type**: array of string 

## Possible Values

- `messaging-8001`: The category for apps that provide messaging services.
- `maps-8002`: The category for apps that provide information to people traveling to a physical location.
- `hiking-adventure-8003`: The category for apps that support hiking and outdoor activities.
- `music-8004`: The category for apps that enable people to discover, listen to, record, perform, or compose music, and that are interactive in nature.
- `weather-8005`: The category for apps that provide forecasts, alerts, and information related to weather conditions.
- `voip-8006`: The category for apps that offer Voice over Internet Protocol (VoIP) services.
- `emergency-8007`: The category for apps that provide emergency support.
- `light-social-8008`: The category for social apps with limited bandwidth.
- `ride-share-8009`: The category for apps that offer ride share and commuting.
- `food-delivery-8010`: The category for apps that offer food and grocery deliveries.
- `news-8011`: The category for apps that offer news.
- `productivity-8012`: The category for productivity apps such as e-mail and word processing.
- `interactive-productivity-8013`: The category for interactive productivity apps such as AI assistants.
- `health-fitness-8014`: The category for health and fitness apps.
- `payment-8015`: The category for payment apps.
- `stocks-8016`: The category for stock and finance apps.
- `podcast-8017`: The category for audio apps, like podcast apps.
- `home-8018`: The category for home app automation apps.
- `sports-8019`: The category for sports and score tracking apps.
- `games-8021`: The category for online games.
- `Shopping-8022`: The category for online shopping apps.
- `travel-8023`: The category for online travel booking apps.
- `streaming-8024`: The category for video streaming apps

#### Discussion

This entitlement defines your app’s category for a carrier-provided satellite network, if the person’s carrier provides it.

## Topics

### Optimizing a carrier-provided satellite network
- [com.apple.developer.networking.carrier-constrained.app-optimized](./com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.

## See Also

### Networking
- [Network Extensions Entitlement](./com.apple.developer.networking.networkextension.md)
  The APIs an app can use to customize networking features.
- [Personal VPN Entitlement](./com.apple.developer.networking.vpn.api.md)
  The API an app can use to create and control a custom system VPN configuration.
- [Associated Domains Entitlement](./com.apple.developer.associated-domains.md)
  The associated domains for specific services, such as shared web credentials, universal links, and App Clips.
- [com.apple.developer.networking.multicast](./com.apple.developer.networking.multicast.md)
  A Boolean value that indicates whether an app can send or receive IP multicast traffic.
- [com.apple.developer.associated-domains.applinks.read-write](./com.apple.developer.associated-domains.applinks.read-write.md)
  A Boolean value that indicates whether the app can use universal links.
- [com.apple.developer.networking.manage-thread-network-credentials](./com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [5G Network Slicing App Category](./com.apple.developer.networking.slicing.appcategory.md)
  The key that defines the app category entitlement to enable Cellular Network Slicing.
- [5G Network Slicing Traffic Category](./com.apple.developer.networking.slicing.trafficcategory.md)
  The key that defines the traffic category entitlement to enable Cellular Network Slicing.
- [com.apple.developer.networking.vmnet](./com.apple.developer.networking.vmnet.md)
- [Configuring your app for ultra-constrained networks](../configuring-your-app-for-ultra-constrained-networks.md)
  Prepare to deliver data over resource-limited data networks.
- [com.apple.developer.networking.carrier-constrained.app-optimized](./com.apple.developer.networking.carrier-constrained.app-optimized.md)
  A Boolean value that indicates whether your app is optimized for a carrier-provided satellite network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.carrier-constrained.appcategory)*