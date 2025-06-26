# contents(at:searchingInAssetPackWithID:options:)

**Framework**: Background Assets  
**Kind**: method

Gets the contents of an asset file at the specified relative path.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func contents(at path: FilePath, searchingInAssetPackWithID assetPackID: String? = nil, options: Data.ReadingOptions = .mappedIfSafe) throws -> Data
```

## Mentions

- [Downloading asset packs hosted by Apple](downloading-asset-packs-hosted-by-apple.md)

#### Return Value

The file’s contents.

#### Discussion

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. If there’s a file-path collision across multiple asset packs, then it’s undefined from which asset pack the file will be read unless you explicitly limit the search to a particular asset pack by passing a non-`nil` ID to the `assetPackID` parameter.

> **Note**: [`ManagedBackgroundAssetsError.fileNotFound(at:)`](managedbackgroundassetserror/filenotfound(at:).md) when no file is found at `path`.

> **Note**: When the path is not relative or when some other error occurs while finding or reading the requested file.

## Parameters

- `path`: The relative path.
- `assetPackID`: The ID of the asset pack in which to search for the file. By default, all downloaded asset packs are searched.
- `options`: Options for how to read the contents of the file into a   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/contents(at:searchinginassetpackwithid:options:))*