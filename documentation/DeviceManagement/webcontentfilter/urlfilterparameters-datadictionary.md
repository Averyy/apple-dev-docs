# WebContentFilter.URLFilterParameters

**Framework**: Device Management  
**Kind**: dictionary

A dictionary containing URL filter parameters.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
object WebContentFilter.URLFilterParameters
```

## Properties

- `PIRAuthenticationToken` (string) *(required)*: The per-user authentication token string, which is an HTTP bearer token for the person using your app. The system uses this token to attest that it is a valid user when requesting anonymous authentication tokens for PIR exchanges.
- `PIRPrivacyPassIssuerURL` (string) *(required)*: The URL containing the domain name of Privacy Pass Issuer.
- `PIRServerURL` (string) *(required)*: The URL containing the domain name of the private information retrieval server.
- `URLFilterControlProviderBundleIdentifier` (string) *(required)*: The bundle identifier string of the URL filter control provider app extension. The system uses this string to identify the URL filter control provider when the filter starts running.
- `URLFilterControlProviderDesignatedRequirement` (string): The designated requirement string in the code signature of the URL filter control provider app extension. The system uses this string to identify the URL filter control provider when the filter starts running. Required in macOS.
- `URLFilterFailClosed` (boolean): If `true`, the system blocks URLs if the filter is enabled, but it fails to make any filtering decision; for example, if there’s a communication failure with the PIR server. If `false`, the system allows URLs if the filter is enabled, but it fails to make any filtering decision.
- `URLPrefilterFetchFrequency` (integer): The time interval in seconds that the system uses to periodically run the `NEURLFilterControlProvider` app extension. The default value is 86400 seconds (1 day). The minimum allowed value is 2700 seconds (45 minutes). The system allows `NEURLFilterControlProvider` implementations to download prefilter Bloom filter data onto the device periodically at the specified interval. Implementations need to allow for a slight difference between the scheduled time and the actual runtime of the task, due to the scheduling mechanism on the system.

## See Also

- [object WebContentFilter.AllowListBookmarksItem](webcontentfilter/allowlistbookmarksitem.md)
  The bookmark in the allow list of the web content filter.
- [object WebContentFilter.VendorConfig](webcontentfilter/vendorconfig-data.dictionary.md)
  A custom dictionary for the filtering service plug-in.
- [object WebContentFilter.WhitelistedBookmarksItem](webcontentfilter/whitelistedbookmarksitem.md)
  The bookmark in the allow list of the web content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilter/urlfilterparameters-data.dictionary)*