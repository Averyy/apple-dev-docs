# contents(at:searchingInAssetPackWithID:options:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns the contents of an asset file at the specified relative path.

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
func contents(at path: FilePath, searchingInAssetPackWithID assetPackID: String? = nil, options: Data.ReadingOptions = .mappedIfSafe) throws -> Data
```

## Mentions

- [Downloading Apple-hosted asset packs](../downloading-apple-hosted-asset-packs.md)

## Return Value

The file’s contents.

## Discussion

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. If there’s a file-path collision across multiple asset packs, then it’s undefined from which asset pack the file will be read unless you explicitly limit the search to a particular asset pack by passing a non-`nil` ID to the `assetPackID` parameter.

> **Throws**: [`ManagedBackgroundAssetsError.fileNotFound(at:)`](../managedbackgroundassetserror/filenotfound%28at%29.md) when no file is found at `path`.

> **Throws**: When the path is not relative or when some other error occurs while finding or reading the requested file.

## Parameters

- `path`: The relative path.
- `assetPackID`: The ID of the asset pack in which to search for the file. By default, all downloaded asset packs are searched.
- `options`: Options for how to read the file’s contents into a `Data` instance.

## See Also

### Accessing asset contents
- [func contents(at: FilePath, asLocalizedFor: Locale.Language, options: Data.ReadingOptions) throws -> Data](./contents%28at,aslocalizedfor,options%29.md)
  Returns the contents of a localized asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](./descriptor%28for,searchinginassetpackwithid%29.md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func descriptor(for: FilePath, asLocalizedFor: Locale.Language) throws -> FileDescriptor](./descriptor%28for,aslocalizedfor%29.md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [func url(for: FilePath) throws -> URL](./url%28for%29.md)
  Returns a URL for the specified relative path.
- [func url(for: FilePath, asLocalizedFor: Locale.Language) throws -> URL](./url%28for,aslocalizedfor%29.md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/contents(at:searchinginassetpackwithid:options:))*