# ContentCaching

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure the Content Caching service.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ContentCaching
```

#### Discussion

Specify `com.apple.configuration.content-cache.settings` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |
| Apply | Only a single configuration is applied |

##### Configuration Examples

**Basic caching**:

This configuration enables content caching for both personal and shared content with automatic activation.

```json
{
    "Type": "com.apple.configuration.content-cache.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "AutoActivation": true,
        "AllowPersonalCaching": true,
        "AllowSharedCaching": true,
        "KeepAwake": true,
        "Port": 0
    }
}
```

**Advanced caching**:

This configuration sets up content caching with a parent cache server, a restricted listen range, and a fixed port.

```json
{
    "Type": "com.apple.configuration.content-cache.settings",
    "Identifier": "2A3B4C5D-6E7F-8A9B-0C1D-2E3F4A5B6C7D",
    "ServerToken": "F1E2D3C4-B5A6-7890-ABCD-EF1234567890",
    "Payload": {
        "AutoActivation": true,
        "AllowPersonalCaching": false,
        "AllowSharedCaching": true,
        "LocalSubnetsOnly": false,
        "ListenRangesOnly": true,
        "ListenRanges": [
            {
                "type": "IPv4",
                "first": "192.168.1.1",
                "last": "192.168.1.254"
            }
        ],
        "Parents": ["10.0.0.1"],
        "ParentSelectionPolicy": "first-available",
        "Port": 8080
    }
}
```

## Topics

### Objects
- [object ContentCachingRangesItemObject](contentcachingrangesitemobject.md)
  A range of IP addresses to cache.

## Properties

- `AllowCacheDelete` (boolean): If `true`, the system purges content from the cache automatically when it needs disk space for other apps when free disk space runs low on the computer. Set to `false` to maximize effectiveness of Content Caching.
- `AllowPersonalCaching` (boolean): If `true`, the system caches the user’s iCloud data. Changes to this value don’t have an immediate effect. Clients may take some time to react to changes. > **Note**:  At least one of the `AllowPersonalCaching` or `AllowSharedCaching` keys need to be `true`.
- `AllowSharedCaching` (boolean): If `true`, the system caches non-iCloud content, such as apps and software updates. Changes to this value don’t have an immediate effect. Clients may take some time to react to changes. > **Note**:  At least one of the `AllowPersonalCaching` or `AllowSharedCaching` keys need to be `true`.
- `AutoActivation` (boolean): If `true`, the system automatically activates the content cache when possible and prevents disabling it. If `allowContentCaching` is `false`, `AutoActivation` is also `false`. Removing a profile that set `AutoActivation` to `true` doesn’t deactivate the Content Cache.
- `AutoEnableTetheredCaching` (boolean): If `true`, the system automatically enables Internet connection sharing when possible and prevent disabling Internet connection sharing. `DenyTetheredCaching` overrides `AutoEnableTetheredCaching`. Tethered caching requires Content Caching.
- `CacheLimit` (integer): The maximum number of bytes of disk space to use for the content cache. Set to `0` for unlimited disk space. Also serves as the upper bound to the `PersonalCacheLimit`.
- `DataPath` (string): The path to the directory used to store cached content. Changing this setting manually doesn’t automatically move cached content from the old location to the new one. To move content automatically, use the Sharing preference’s Content Caching pane. The value must be (or end with) `/Library/Application Support/Apple/AssetCache/Data`. The system creates a directory and its intermediates for the given data path if it doesn’t already exist. The directory is owned by `_assetcache:_assetcache` and has mode 0750. Its immediate parent directory (`.../Library/Application Support/Apple/AssetCache`) is owned by `_assetcache:_assetcache` and has mode `0755`.
- `DeclarativeStatusInterval` (integer): The time interval in seconds the system uses to update the [`StatusContentCacheInfo`](statuscontentcacheinfo.md) declarative status item. The reporting interval can’t be less than 60 (1 per minute) or larger than 86400 (1 per day), defaults to 0  (off)
- `DenyActivation` (boolean): If `true`, the system disables Content Caching. This is the inverse of the `allowContentCaching` restriction in MDM. It overrides the `AutoActivation` key. Use this key to prevent launching the Content Caching service.
- `DenyTetheredCaching` (boolean): If `true`, the system disables tethered caching.
- `DisplayAlerts` (boolean): If `true`, Content Caching displays exceptional conditions (alerts) as system notifications in the upper corner of the screen.
- `KeepAwake` (boolean): If `true`, the system prevents the computer from sleeping as long as Content Caching is on (System Preferences > Sharing > Content Caching is on). Customers who want Content Caching to be as available as much as possible should turn this setting on.
- `ListenRanges` ([ContentCachingRangesItemObject]): An array of dictionaries that describe a range of client IP addresses to serve.
- `ListenRangesOnly` (boolean): If `true`, the content cache provides content to the clients in the `ListenRanges`.
- `ListenWithPeersAndParents` (boolean): If `true`, the content cache provides content to the clients in the union of the `ListenRanges`, `PeerListenRanges` and `Parents`.
- `LocalSubnetsOnly` (boolean): If `true`, the content cache offers content to clients only on the same immediate local network only. The content cache offers no content to clients on other networks reachable by the content cache. If `LocalSubnetsOnly` is `true`, the system ignores `ListenRanges`.
- `LogClientIdentity` (boolean): If `true`, the Content Cache logs the IP address and port number of the clients that request content.
- `ManagementReportingInterval` (integer): The reporting interval in seconds the system uses when `ManagementStatusTarget` is present. The reporting interval can’t be less than 60 (1 per minute) or larger than 86400 (1 per day), and defaults to 300 (1 per 5 min).
- `ManagementSecurityConfig` (string): If the `ManagementStatusTarget` is an https URL, the system uses this field to determine how the connection is secured. - `no-cert`: The system uses regular https processing using the built-in anchor certificates.
- `signedByCACert`: The system requires the https connection’s certificate to be signed by the certificate provided in the `ManagementStatusCertificateReference` field. If your organization has a CA infrastructure this is the best choice.
- `specificServerCert`: The system requires the https connection’s certificate to match the certificate provided in the `ManagementStatusCertificateReference` field.
- `ManagementStatusCertificateReference` (string): The identifier of an asset declaration that contains the certificate the system uses to verify the security of the status reporting https connection. Required when `ManagementSecurityConfig` is set to `signedByCACert` or `specificServerCert`.
- `ManagementStatusTarget` (string): The target URL the system uses to send management statistics using an HTTP PUT request with a json dictionary as the payload. If the URL is an https URL (recommended) the `ManagementSecurityConfig` defines how the system secures the connection. The system sends the management statistics report to the target URL at an interval set by the `ManagementReportingInterval` value.
- `Parents` ([string]): An array of the local IP addresses of other content caches that this cache should download from or upload to, instead of downloading from or uploading to Apple directly. The system ignores invalid addresses and addresses of computers that aren’t content caches. The system skips Parent caches that become unavailable. If all parent content caches become unavailable, the content cache downloads from or uploads to Apple directly, until a parent content cache becomes available again.
- `ParentSelectionPolicy` (string): The policy to implement when choosing among more than one configured parent content cache. With every policy, the system skips parent caches that are temporarily unavailable. Allowed values: - `first-available`: Always use the first available parent in the Parents list. Use this policy to designate permanent primary, secondary, and subsequent parents.
- `url-path-hash`: Hash the path part of the requested URL so that the same parent is always used for the same URL. This is useful for maximizing the size of the combined caches of     the parents.
- `random`: Choose a parent at random. Use this policy for load balancing.
- `round-robin`: Rotate through the parents in order. Use this policy for load balancing.
- `sticky-available`: Use the first available parent in the Parents list until it becomes unavailable, then advance to the next one. Use this policy for designating floating primary, secondary, and subsequent parents.
- `PeerFilterRanges` ([ContentCachingRangesItemObject]): An array of dictionaries describing a range of peer IP addresses that the content cache uses to filter its list of peers to query for content. The content cache only queries peers in `PeerFilterRanges`. When `PeerFilterRanges` is an empty array, the content cache doesn’t query any peers.
- `PeerListenRanges` ([ContentCachingRangesItemObject]): An array of dictionaries describing a range of peer IP addresses the content cache responds to. When `PeerListenRanges` is an empty array, the content cache responds with an error to all cache queries.
- `PeerLocalSubnetsOnly` (boolean): If `true`, the content cache only peers with other content caches on the same immediate local network, rather than with content caches that use the same public IP address as the device. When `PeerLocalSubnetsOnly` is `true`, it overrides the configuration of `PeerFilterRanges` and `PeerListenRanges`. If the network changes, the local network peering restrictions update appropriately. If `false`, the content cache defers to `PeerFilterRanges` and `PeerListenRanges` for configuring the peering restrictions.
- `PersonalCacheLimit` (integer): The maximum number of bytes of disk space to use for the personal content cache. The content cache limits the maximum value to the `CacheLimit` value. Set to `0` to use the overall `CacheLimit`.
- `Port` (integer): The TCP port number on which the content cache accepts requests for uploads or downloads. Set to `0` to pick a random, available port.
- `PublicRanges` ([ContentCachingRangesItemObject]): An array of dictionaries describing a range of public IP addresses that the cloud servers should use for matching clients to content caches.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/contentcaching)*