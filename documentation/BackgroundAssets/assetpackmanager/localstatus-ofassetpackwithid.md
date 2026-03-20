# localStatus(ofAssetPackWithID:)

**Framework**: Background Assets  
**Kind**: method

Checks an asset pack’s local status.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
func localStatus(ofAssetPackWithID assetPackID: String) async -> AssetPack.Status
```

#### Return Value

The asset pack’s local status.

#### Discussion

This method checks only status values that are determinable offline. It doesn’t induce any network traffic or automatically trigger any downloads, updates, or removals. The following status values are determinable offline:

- [`outOfDate`](assetpack/status/outofdate.md) (in some situations)
- [`obsolete`](assetpack/status/obsolete.md) (in some situations)
- [`downloaded`](assetpack/status/downloaded.md)

Because this method doesn’t communicate with the server, it can’t determine whether a particular asset pack exists in the first place. Instead, it returns an empty status value when provided a nonexistent asset-pack ID, which is indistinguishable from the situation in which the asset pack does indeed exist but hasn’t yet been downloaded. Use [`status(ofAssetPackWithID:)`](assetpackmanager/status(ofassetpackwithid:).md) to get a full view of an asset pack’s status.

## Parameters

- `assetPackID`: The asset pack’s ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localstatus(ofassetpackwithid:))*