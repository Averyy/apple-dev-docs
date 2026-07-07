# ContentCachingService

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the Content Caching service.

**Availability**:
- macOS 10.13.4+

## Declaration

```swift
object ContentCachingService
```

#### Discussion

Specify `com.apple.AssetCache.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | N/A |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AllowPersonalCaching</key>
            <false/>
            <key>AllowSharedCaching</key>
            <true/>
            <key>AutoActivation</key>
            <true/>
            <key>CacheLimit</key>
            <integer>180000000000</integer>
            <key>DenyTetheredCaching</key>
            <false/>
            <key>ListenRangesOnly</key>
            <false/>
            <key>LocalSubnetsOnly</key>
            <true/>
            <key>LogClientIdentity</key>
            <false/>
            <key>ParentSelectionPolicy</key>
            <string>round-robin</string>
            <key>PeerLocalSubnetsOnly</key>
            <true/>
            <key>Port</key>
            <integer>0</integer>
            <key>PayloadIdentifier</key>
            <string>com.example.mycontentcachingpayload</string>
            <key>PayloadType</key>
            <string>com.apple.AssetCache.managed</string>
            <key>PayloadUUID</key>
            <string>c7d8c850-e4ef-0135-0bd6-0c4de9ce4c04</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Content Caching</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>a430c370-b5d5-4e5b-b46b-137931e8b230</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ContentCachingService.Ranges](contentcachingservice/ranges.md)
  A range of IP addresses to cache.

## Properties

- `AllowCacheDelete` (boolean): If true, the system purges content from the cache automatically when it needs disk space for other apps when free disk space runs low on the computer. Set to `false` to maximize effectiveness of Content Caching. Available: macOS 10.15+
Deprecated: macOS 27+
- `AllowPersonalCaching` (boolean): If `true`, the system caches the user’s iCloud data. Changes to this value don’t have an immediate effect. Clients may take some time, such as hours or days, to react to changes. > **Note**:  At least one of the `AllowPersonalCaching` or `AllowSharedCaching` keys need to be `true`. Deprecated: macOS 27+
- `AllowSharedCaching` (boolean): If `true`, the system caches non-iCloud content, such as apps and software updates. Changes to this value don’t have an immediate effect. Clients may take some time, such as hours or days, to react to changes. > **Note**:  At least one of the `AllowPersonalCaching` or `AllowSharedCaching` keys need to be `true`. Deprecated: macOS 27+
- `AutoActivation` (boolean): If `true`, the system automatically activates the content cache when possible and prevents disabling it. If `allowContentCaching` is `false`, `AutoActivation` is also `false`. Removing a profile that set `AutoActivation` to `true` doesn’t deactivate the Content Cache. Deprecated: macOS 27+
- `AutoEnableTetheredCaching` (boolean): If `true`, the system automatically enables Internet connection sharing when possible and prevent disabling Internet connection sharing. `DenyTetheredCaching` overrides `AutoEnableTetheredCaching`. Tethered caching requires Content Caching. Available: macOS 10.15.4+
Deprecated: macOS 27+
- `CacheLimit` (integer): The maximum number of bytes of disk space to use for the content cache. Set to `0` for unlimited disk space. Deprecated: macOS 27+
- `DataPath` (string): The path to the directory used to store cached content. Changing this setting manually doesn’t automatically move cached content from the old location to the new one. To move content automatically, use the Sharing preference’s Content Caching pane. The value must be (or end with) `/Library/Application Support/Apple/AssetCache/Data`. The system creates a directory and its intermediates for the given data path if it doesn’t already exist. The directory is owned by `_assetcache:_assetcache` and has mode 0750. Its immediate parent directory (`.../Library/Application Support/Apple/AssetCache`) is owned by `_assetcache:_assetcache` and has mode `0755`. Deprecated: macOS 27+
- `DenyTetheredCaching` (boolean): If `true`, the system disables tethered caching. Deprecated: macOS 27+
- `DisplayAlerts` (boolean): If `true`, Content Caching displays exceptional conditions (alerts) as system notifications in the upper corner of the screen. The device automatically displayed alerts starting in macOS 10.13. In macOS 10.15 the alerts are off by default, but still available through this setting. Available: macOS 10.15+
Deprecated: macOS 27+
- `KeepAwake` (boolean): If `true`, the system prevents the computer from sleeping as long as Content Caching is on (System Preferences > Sharing > Content Caching is on). Customers who want Content Caching to be as available as much as possible should turn this setting on. Available: macOS 10.15+
Deprecated: macOS 27+
- `ListenRanges` ([ContentCachingService.Ranges]): An array of dictionaries that describe a range of client IP addresses to serve. Deprecated: macOS 27+
- `ListenRangesOnly` (boolean): If `true`, the content cache provides content to the clients in the `ListenRanges`. Deprecated: macOS 27+
- `ListenWithPeersAndParents` (boolean): If `true`, the content cache provides content to the clients in the union of the `ListenRanges`, `PeerListenRanges` and `Parents`. Deprecated: macOS 27+
- `LocalSubnetsOnly` (boolean): If `true`, the content cache offers content to clients only on the same immediate local network only. No content is offered to clients on other networks reachable by the content cache. If `LocalSubnetsOnly` is `true`, the system ignores `ListenRanges`. Deprecated: macOS 27+
- `LogClientIdentity` (boolean): If `true`, the Content Cache logs the IP address and port number of the clients that request content. Deprecated: macOS 27+
- `Parents` ([string]): An array of the local IP addresses of other content caches that this cache should download from or upload to, instead of downloading from or uploading to Apple directly. The system ignores invalid addresses and addresses of computers that aren’t content caches. The system skips Parent caches that become unavailable. If all parent content caches become unavailable, the content cache downloads from or uploads to Apple directly, until a parent content cache becomes available again. Deprecated: macOS 27+
- `ParentSelectionPolicy` (string): The policy to implement when choosing among more than one configured parent content cache. With every policy, the system skips parent caches that are temporarily unavailable. Allowed values: - `first-available`: Always use the first available parent in the Parents list. Use this policy to designate permanent primary, secondary, and subsequent parents.
- `url-path-hash`: Hash the path part of the requested URL so that the same parent is always used for the same URL. This is useful for maximizing the size of the combined caches of     the parents.
- `random`: Choose a parent at random. Use this policy for load balancing.
- `round-robin`: Rotate through the parents in order. Use this policy for load balancing.
- `sticky-available`: Use the first available parent in the Parents list until it becomes unavailable, then advance to the next one. Use this policy for designating floating primary, secondary, and subsequent parents. Deprecated: macOS 27+
- `PeerFilterRanges` ([ContentCachingService.Ranges]): An array of dictionaries describing a range of peer IP addresses that the content cache uses to filter its list of peers to query for content. The content cache only queries peers in `PeerFilterRanges`. When `PeerFilterRanges` is an empty array, the content cache doesn’t query any peers. Deprecated: macOS 27+
- `PeerListenRanges` ([ContentCachingService.Ranges]): An array of dictionaries describing a range of peer IP addresses the content cache responds to. When `PeerListenRanges` is an empty array, the content cache responds with an error to all cache queries. Deprecated: macOS 27+
- `PeerLocalSubnetsOnly` (boolean): If `true`, the content cache only peers with other content caches on the same immediate local network, rather than with content caches that use the same public IP address as the device. When `PeerLocalSubnetsOnly` is `true`, it overrides the configuration of `PeerFilterRanges` and `PeerListenRanges`. If the network changes, the local network peering restrictions update appropriately. If `false`, the content cache defers to `PeerFilterRanges` and `PeerListenRanges` for configuring the peering restrictions. Deprecated: macOS 27+
- `Port` (integer): The TCP port number on which the content cache accepts requests for uploads or downloads. Set to `0` to pick a random, available port. Deprecated: macOS 27+
- `PublicRanges` ([ContentCachingService.Ranges]): An array of dictionaries describing a range of public IP addresses that the cloud servers should use for matching clients to content caches. Deprecated: macOS 27+

## See Also

- [object Cellular](cellular.md)
  The payload that configures cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object DNSSettings](dnssettings.md)
  The payload that configures encrypted DNS settings.
- [object Domains](domains.md)
  The payload that configures the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload that configures the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object Relay](relay.md)
  The payload that configures relay settings.
- [object WiFi](wifi.md)
  The payload that configures Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcachingservice)*