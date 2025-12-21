# AVURLAssetReferenceRestrictionsKey

**Framework**: AVFoundation  
**Kind**: var

A value that represents the restrictions used by the asset when resolving references to external media data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let AVURLAssetReferenceRestrictionsKey: String
```

#### Discussion

The corresponding value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that wraps an [`AVAssetReferenceRestrictions`](avassetreferencerestrictions.md) enum value, or the logical combination of multiple enum values, that indicate the restrictions the asset uses when resolving references to external media data.

Some assets can contain references to media data stored outside the asset’s container file, for example in another file. Use this key to specify the policy to use when the asset encounters these references. If an asset contains one or more references to a type forbidden by the reference restriction, loading of asset properties fails, and you can’t use this asset with other AVFoundation objects, such as [`AVPlayerItem`](avplayeritem.md) or [`AVAssetExportSession`](avassetexportsession.md).

## Topics

### Data types
- [struct AVAssetReferenceRestrictions](avassetreferencerestrictions.md)
  Restrictions to use when resolving references to external media data.

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
- [let AVURLAssetShouldSupportAliasDataReferencesKey: String](avurlassetshouldsupportaliasdatareferenceskey.md)
  A Boolean value that indicates whether the system parses and resolves alias data references in the asset.
- [let AVURLAssetURLRequestAttributionKey: String](avurlasseturlrequestattributionkey.md)
  A value that specifies the attribution of the URLs that this asset requests.
- [let AVURLAssetShouldParseExternalSphericalTagsKey: String](avurlassetshouldparseexternalsphericaltagskey.md)
  Indicates whether additional projected media signaling in the asset should be parsed and resolved as format description extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlassetreferencerestrictionskey)*