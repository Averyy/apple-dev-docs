# url(for:)

**Framework**: Background Assets  
**Kind**: method

Gets the URL for the specified relative path.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func url(for path: FilePath) throws -> URL
```

#### Return Value

The URL to the item.

#### Discussion

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. Unlike [`contents(at:searchingInAssetPackWithID:options:)`](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md) and [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md), this method supports retrieving entire directories—including packages—in which case it merges the corresponding slices of the shared logical directory from all downloaded asset packs that contain such slices. If there’s a path collision across multiple asset packs, then it’s undefined from which asset pack an individual file will be resolved.

> **Note**: When the path isn’t relative or when some other error occurs while finding the requested item.

> ⚠️ **Warning**: Don’t persist the returned URL beyond the lifetime of the current process.

> ⚠️ **Warning**: This method is less efficient than are [`contents(at:searchingInAssetPackWithID:options:)`](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md) and [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md); use those methods instead if you can do so. In particular, this method shouldn’t be used to get the URL to the root of the shared asset-pack namespace. Don’t use this method to block the main thread.

> **Note**: This method will return a well formed URL even if no item exists at the specified relative path in any asset pack, in which case any attempts to get its contents—whether it’s a file or a directory—will fail.

## Parameters

- `path`: The relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/url(for:))*