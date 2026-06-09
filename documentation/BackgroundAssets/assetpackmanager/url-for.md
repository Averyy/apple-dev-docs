# url(for:)

**Framework**: Background Assets  
**Kind**: method

Returns a URL for the specified relative path.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func url(for path: FilePath) throws -> URL
```

#### Return Value

The URL to the item.

#### Discussion

> ⚠️ **Warning**: Don’t persist the returned URL beyond the lifetime of the current process.

> **Note**: This method will return a well formed URL even if no item exists at the specified relative path in any asset pack, in which case any attempts to get its contents—whether it’s a file or a directory—will fail.

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. Unlike [`contents(at:searchingInAssetPackWithID:options:)`](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md) and [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md), this method supports retrieving entire directories—including packages—in which case it merges the corresponding slices of the shared logical directory from all downloaded asset packs that contain such slices. If there’s a path collision across multiple asset packs, then it’s undefined from which asset pack an individual file will be resolved.

> ⚠️ **Warning**: This method is less efficient than are [`contents(at:searchingInAssetPackWithID:options:)`](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md) and [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md); use those methods instead if you can do so. In particular, this method shouldn’t be used to get the URL to the root of the shared asset-pack namespace. Don’t use this method to block the main thread.

> **Note**: When the path isn’t relative or when some other error occurs while finding the requested item.

## Parameters

- `path`: The relative path.

## See Also

- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Returns the contents of an asset file at the specified relative path.
- [func contents(at: FilePath, asLocalizedFor: Locale.Language, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:aslocalizedfor:options:).md)
  Returns the contents of a localized asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func descriptor(for: FilePath, asLocalizedFor: Locale.Language) throws -> FileDescriptor](assetpackmanager/descriptor(for:aslocalizedfor:).md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [func url(for: FilePath, asLocalizedFor: Locale.Language) throws -> URL](assetpackmanager/url(for:aslocalizedfor:).md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/url(for:))*