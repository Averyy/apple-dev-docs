# fragmentedAssetWithURL:options:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a fragmented asset for the media at the specified URL.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) fragmentedAssetWithURL:(NSURL *) URL options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

A fragmented asset that models the media at the specified URL.

## Parameters

- `URL`: A URL that points to the desired media resource.
- `options`: A dictionary of keys for specifying initialization options. Valid values are [`AVURLAssetPreferPreciseDurationAndTimingKey`](../avurlassetpreferprecisedurationandtimingkey.md) and [`AVURLAssetReferenceRestrictionsKey`](../avurlassetreferencerestrictionskey.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/fragmentedassetwithurl:options:)*