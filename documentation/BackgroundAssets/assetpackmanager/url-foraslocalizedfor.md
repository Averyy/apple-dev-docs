# url(for:asLocalizedFor:)

**Framework**: Background Assets  
**Kind**: method

Returns a URL for the specified relative path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func url(for path: FilePath, asLocalizedFor language: Locale.Language) throws -> URL
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Return Value

The URL to the item.

#### Discussion

> ⚠️ **Warning**: Don’t persist the returned URL beyond the lifetime of the current process.

> **Note**: This method will return a well formed URL even if no item exists at the specified relative path in any relevant asset pack, in which case any attempts to get its contents—whether it’s a file or a directory—will fail.

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. Unlike [`contents(at:asLocalizedFor:options:)`](assetpackmanager/contents(at:aslocalizedfor:options:).md) and [`descriptor(for:asLocalizedFor:)`](assetpackmanager/descriptor(for:aslocalizedfor:).md), this method supports retrieving entire directories—including packages—in which case it merges the corresponding slices of the shared logical directory from all downloaded asset packs that are localized in the specified language and that contain such slices. If there’s a path collision across multiple such asset packs, then it’s undefined from which asset pack an individual file will be resolved.

> ⚠️ **Warning**: This method is less efficient than are [`contents(at:asLocalizedFor:options:)`](assetpackmanager/contents(at:aslocalizedfor:options:).md) and [`descriptor(for:asLocalizedFor:)`](assetpackmanager/descriptor(for:aslocalizedfor:).md); use those methods instead if you can do so. In particular, this method shouldn’t be used to get the URL to the root of the shared asset-pack namespace. Don’t use this method to block the main thread.

This method is most useful if you intentionally induce a file-path collision across multiple differently localized asset packs. For example, you may include an English-localized version of `Videos/Introduction.m4v` in an `en` asset pack, a Hebrew-localized version of `Videos/Introduction.m4v` in a `he` asset pack, and an American Spanish–localized version of `Videos/Introduction.m4v` in an `es-US` asset pack. If you offer split-language functionality to users, then you may want to download two or more of those asset packs on the same device. In that scenario, the specific choice of item the URL to which [`url(for:)`](assetpackmanager/url(for:).md) returns would be undefined. With this method, merely passing a `Locale.Language` instance to the `language` parameter is sufficient to resolve the ambiguity. [`url(for:)`](assetpackmanager/url(for:).md) is more suitable in most other situations.

> **Note**: Language matching considers implicit script and region tags per Unicode’s Common Locale Data Repository. For example, `en` is equivalent to `en-US` and `en-Latn-US` but not `en-CA`.

> **Note**: When the path isn’t relative or when some other error occurs while finding the requested item.

## Parameters

- `path`: The relative path.
- `language`: The language that the framework uses to limit the search within localized asset packs.

## See Also

- [func contents(at: FilePath, searchingInAssetPackWithID: String?, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:searchinginassetpackwithid:options:).md)
  Returns the contents of an asset file at the specified relative path.
- [func contents(at: FilePath, asLocalizedFor: Locale.Language, options: Data.ReadingOptions) throws -> Data](assetpackmanager/contents(at:aslocalizedfor:options:).md)
  Returns the contents of a localized asset file at the specified relative path.
- [func descriptor(for: FilePath, searchingInAssetPackWithID: String?) throws -> FileDescriptor](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md)
  Opens and returns a file descriptor for an asset file at the specified relative path.
- [func descriptor(for: FilePath, asLocalizedFor: Locale.Language) throws -> FileDescriptor](assetpackmanager/descriptor(for:aslocalizedfor:).md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/url(for:aslocalizedfor:))*