# AVURLAssetURLRequestAttributionKey

**Framework**: AVFoundation  
**Kind**: var

A value that specifies the attribution of the URLs that this asset requests.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let AVURLAssetURLRequestAttributionKey: String
```

#### Discussion

The value is a number that represents an [`NSURLRequest.Attribution`](https://developer.apple.com/documentation/foundation/nsurlrequest/attribution). URL requests that the system issues on behalf of the asset attribute this value and follow the App Privacy Policy accordingly.

The default value is [`NSURLRequest.Attribution.developer`](https://developer.apple.com/documentation/foundation/nsurlrequest/attribution/developer).

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
- [let AVURLAssetPrimarySessionIdentifierKey: String](avurlassetprimarysessionidentifierkey.md)
  Specifies a UUID to set as the session identifier for HTTP requests that the asset makes.
- [let AVURLAssetReferenceRestrictionsKey: String](avurlassetreferencerestrictionskey.md)
  A value that represents the restrictions used by the asset when resolving references to external media data.
- [let AVURLAssetShouldSupportAliasDataReferencesKey: String](avurlassetshouldsupportaliasdatareferenceskey.md)
  A Boolean value that indicates whether the system parses and resolves alias data references in the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasseturlrequestattributionkey)*