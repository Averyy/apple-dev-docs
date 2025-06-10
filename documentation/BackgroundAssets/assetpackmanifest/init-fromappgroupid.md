# init(from:appGroupID:)

**Framework**: Background Assets  
**Kind**: init

Creates a representation of a manifest in memory given JSON-encoded data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(from data: Data, appGroupID: String) throws
```

## Parameters

- `data`: JSON-encoded data.
- `appGroupID`: The ID of the app group in which to store unmanaged asset packs that are downloaded from this manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/init(from:appgroupid:))*