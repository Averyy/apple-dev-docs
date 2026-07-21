# descriptor(for:asLocalizedFor:)

**Framework**: Background Assets  
**Kind**: method

Opens and returns a file descriptor for a localized asset file at the specified relative path.

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
func descriptor(for path: FilePath, asLocalizedFor language: Locale.Language) throws -> FileDescriptor
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Return Value

A descriptor for the opened file.

#### Discussion

> ❗ **Important**: It’s your responsibility to close the file descriptor when you’re done using it.

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. This method searches in only the downloaded asset packs that are localized in the specified language. If there’s a file-path collision across multiple such asset packs, then it’s undefined from which asset pack the file will be read.

This method is most useful if you intentionally induce a file-path collision across multiple differently localized asset packs. For example, you may include an English-localized version of `Videos/Introduction.m4v` in an `en` asset pack, a Hebrew-localized version of `Videos/Introduction.m4v` in a `he` asset pack, and an American Spanish–localized version of `Videos/Introduction.m4v` in an `es-US` asset pack. If you offer split-language functionality to users, then you may want to download two or more of those asset packs on the same device. In that scenario, the specific choice of file that [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md) opens would be undefined unless you determine the appropriate asset pack’s ID and pass it to that method’s `assetPackID` parameter. With this method, merely passing a `Locale.Language` instance to the `language` parameter is sufficient to resolve the ambiguity without requiring that you determine the asset pack’s ID. [`descriptor(for:searchingInAssetPackWithID:)`](assetpackmanager/descriptor(for:searchinginassetpackwithid:).md) is more suitable in most other situations.

> **Note**: Language matching considers implicit script and region tags per Unicode’s Common Locale Data Repository. For example, `en` is equivalent to `en-US` and `en-Latn-US` but not `en-CA`.

> **Note**: [`ManagedBackgroundAssetsError.fileNotFound(at:)`](managedbackgroundassetserror/filenotfound(at:).md) when no file is found at `path`.

> **Note**: When the path is not relative or when some other error occurs while finding or opening the requested file.

> **Note**: Use this method if you need low-level access to the file descriptor. If you don’t, then use [`contents(at:asLocalizedFor:options:)`](assetpackmanager/contents(at:aslocalizedfor:options:).md) instead.

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
- [func url(for: FilePath) throws -> URL](assetpackmanager/url(for:).md)
  Returns a URL for the specified relative path.
- [func url(for: FilePath, asLocalizedFor: Locale.Language) throws -> URL](assetpackmanager/url(for:aslocalizedfor:).md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/descriptor(for:aslocalizedfor:))*