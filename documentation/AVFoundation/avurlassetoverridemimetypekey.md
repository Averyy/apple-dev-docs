# AVURLAssetOverrideMIMETypeKey

**Framework**: AVFoundation  
**Kind**: var

A key that specifies the MIME type to use to identify the format of a media resource.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
let AVURLAssetOverrideMIMETypeKey: String
```

#### Discussion

If you specify a value for this key, the system uses it to determine how to handle or parse the media resource, and ignores any other information that may be available, such as the URL path extension or a server-provided MIME type.

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
- [let AVURLAssetPreferPreciseDurationAndTimingKey: String](avurlassetpreferprecisedurationandtimingkey.md)
  A Boolean value that indicates whether the asset should provide accurate duration and precise random access by time.
- [let AVURLAssetPrimarySessionIdentifierKey: String](avurlassetprimarysessionidentifierkey.md)
  Specifies a UUID to set as the session identifier for HTTP requests that the asset makes.
- [let AVURLAssetReferenceRestrictionsKey: String](avurlassetreferencerestrictionskey.md)
  A value that represents the restrictions used by the asset when resolving references to external media data.
- [let AVURLAssetShouldSupportAliasDataReferencesKey: String](avurlassetshouldsupportaliasdatareferenceskey.md)
  A Boolean value that indicates whether the system parses and resolves alias data references in the asset.
- [let AVURLAssetURLRequestAttributionKey: String](avurlasseturlrequestattributionkey.md)
  A value that specifies the attribution of the URLs that this asset requests.
- [let AVURLAssetShouldParseExternalSphericalTagsKey: String](avurlassetshouldparseexternalsphericaltagskey.md)
  Indicates whether additional projected media signaling in the asset should be parsed and resolved as format description extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlassetoverridemimetypekey)*