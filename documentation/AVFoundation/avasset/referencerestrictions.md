# referenceRestrictions

**Framework**: AVFoundation  
**Kind**: property

The restrictions that an asset places on how it resolves references to external media.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var referenceRestrictions: AVAssetReferenceRestrictions { get }
```

#### Discussion

For [`AVURLAsset`](avurlasset.md), this property reflects the value passed in for [`AVURLAssetReferenceRestrictionsKey`](avurlassetreferencerestrictionskey.md), if any.

The default value for this property is [`defaultPolicy`](avassetreferencerestrictions/defaultpolicy.md). See [`AVURLAssetReferenceRestrictionsKey`](avurlassetreferencerestrictionskey.md) for more information about reference restrictions.

## See Also

- [struct AVAssetReferenceRestrictions](avassetreferencerestrictions.md)
  Restrictions to use when resolving references to external media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/referencerestrictions)*