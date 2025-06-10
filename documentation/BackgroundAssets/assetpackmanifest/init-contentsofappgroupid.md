# init(contentsOf:appGroupID:)

**Framework**: Background Assets  
**Kind**: init

Creates a representation of a manifest in memory given a URL to the manifest’s representation as a JSON file on disk.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(contentsOf url: URL, appGroupID: String) throws
```

## Parameters

- `url`: A URL to a local JSON file.
- `appGroupID`: The ID of the app group in which to store unmanaged asset packs that are downloaded from this manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/init(contentsof:appgroupid:))*