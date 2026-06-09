# StatusContentCacheServiceContentCacheStatusObject

**Framework**: Device Management  
**Kind**: dictionary

The basic set of AssetCache status items

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCacheServiceContentCacheStatusObject
```

## Properties

- `activated` (boolean): If `true`, the device has enabled the Content Cache. Enabling the Content Caching doesn’t guarantee service. See the `Active` key for the readiness of the Content Cache to serve requests.
- `active` (boolean): If `true`, the Content Cache is ready to serve requests.
- `cache-status` (string): The level of cache pressure. `LOWSPACE` means cache pressure is high.
- `port` (integer): The IP port number the Content Cache listens to for requests from clients, peers, and children.
- `private-addresses` ([string]): An array of the Content Cache’s local IP addresses.
- `public-address` (string): The public IP address of the Content Cache.
- `registration-error` (string): If present, the reason the Content Cache failed to register itself with Apple.
- `registration-response-code` (integer): If present, the HTTP response code that the Content Cache received when it failed to register itself with Apple.
- `registration-started` (string): The RFC 3339 timestamp for when the Content Cache began registering itself with Apple. This value is only available during registration attempts.
- `registration-status` (integer): The status of the Content Cache’s registration with Apple, which is one of the following values: - `-1`: The registration failed.
- `0`: The registration is pending.
- `1`: The registration succeeded.
- `report-error` (string): When present, indicates why the Content Cache failed to send the metrics.
- `report-response-code` (integer): When present, contains the HTTP response code that the Content Cache received when it failed to send the metrics report to the target URL.
- `sending-reports` (boolean): When present, a value of `true` indicates that the cache is sending metrics reports to the URL specified in the `ManagementStatusTarget` key in the installed [`ContentCaching`](contentcaching.md) configuration.
- `server-guid` (string) *(required)*: The unique identifier of the Content Cache.
- `startup-status` (string): The status of the Content Cache’s registration with Apple.
- `tetherator-status` (integer): The status of tethered caching, which is the Content Cache with a shared internet connection, which is one of the following values: - ‘-1’ : Unknown
- ‘0’ : Disabled
- ‘1’ : Enabled
- `version` (string) *(required)*: The version number of the Content Cache software.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcacheservicecontentcachestatusobject)*