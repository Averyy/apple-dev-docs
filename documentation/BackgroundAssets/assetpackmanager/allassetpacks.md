# allAssetPacks

**Framework**: Background Assets  
**Kind**: property

The asset packs that are available to download.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var allAssetPacks: Set<AssetPack> { get async throws }
```

#### Discussion

Accessing this property might cause an attempt to get the latest asset-pack information from the server.

## See Also

- [func assetPack(withID: String) async throws -> AssetPack](assetpackmanager/assetpack(withid:).md)
  Returns the asset pack with the given ID.
- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Returns the contents of an asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/allassetpacks)*