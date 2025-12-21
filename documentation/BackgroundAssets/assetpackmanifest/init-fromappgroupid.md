# init(from:appGroupID:)

**Framework**: Background Assets  
**Kind**: init

Creates a representation of a manifest in memory given JSON-encoded data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(from data: Data, appGroupID: String) throws
```

## Parameters

- `data`: JSON-encoded data.
- `appGroupID`: The ID of the app group in which to store unmanaged asset packs that are downloaded from this manifest.

## See Also

- [init(contentsOf: URL, appGroupID: String) throws](assetpackmanifest/init(contentsof:appgroupid:).md)
  Creates a representation of a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/init(from:appgroupid:))*