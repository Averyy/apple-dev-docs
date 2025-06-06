# AVURLAssetPrimarySessionIdentifierKey

**Framework**: AVFoundation  
**Kind**: var

Specifies a UUID to set as the session identifier for HTTP requests that the asset makes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let AVURLAssetPrimarySessionIdentifierKey: String
```

#### Discussion

The asset appends value as the value of the `_HLS_primary_id` query parameter. Only HTTP Live Streaming assets support this option.

## See Also

- [let AVURLAssetAllowsCellularAccessKey: String](avurlassetallowscellularaccesskey.md)
  A Boolean value that indicates whether the system can make network requests on behalf of the asset when connected to a cellular network.
- [let AVURLAssetAllowsConstrainedNetworkAccessKey: String](avurlassetallowsconstrainednetworkaccesskey.md)
  A Boolean value that indicates whether the system allows network requests on behalf of this asset to use the constrained interface.
- [let AVURLAssetAllowsExpensiveNetworkAccessKey: String](avurlassetallowsexpensivenetworkaccesskey.md)
  A Boolean value that indicates whether the system allows network requests on behalf of this asset to use the expensive interface.
- [let AVURLAssetHTTPCookiesKey: String](avurlassethttpcookieskey.md)
  The HTTP cookies that a URL asset may send with HTTP requests.
- [let AVURLAssetHTTPUserAgentKey: String](avurlassethttpuseragentkey.md)
  A key that specifies the user agent of requests that an asset makes.
- [let AVURLAssetOverrideMIMETypeKey: String](avurlassetoverridemimetypekey.md)
  A key that specifies the MIME type to use to identify the format of a media resource.
- [let AVURLAssetPreferPreciseDurationAndTimingKey: String](avurlassetpreferprecisedurationandtimingkey.md)
  A Boolean value that indicates whether the asset should provide accurate duration and precise random access by time.
- [let AVURLAssetReferenceRestrictionsKey: String](avurlassetreferencerestrictionskey.md)
  A value that represents the restrictions used by the asset when resolving references to external media data.
- [let AVURLAssetShouldSupportAliasDataReferencesKey: String](avurlassetshouldsupportaliasdatareferenceskey.md)
  A Boolean value that indicates whether the system parses and resolves alias data references in the asset.
- [let AVURLAssetURLRequestAttributionKey: String](avurlasseturlrequestattributionkey.md)
  A value that specifies the attribution of the URLs that this asset requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlassetprimarysessionidentifierkey)*