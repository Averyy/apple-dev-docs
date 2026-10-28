# URLForPath:asLocalizedForLanguage:error:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns a URL for the specified relative path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (NSURL *) URLForPath:(NSString *) path asLocalizedForLanguage:(NSString *) languageIdentifier error:(NSError **) error;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Return Value

The URL to the item or `nil` if an error occurred.

## Discussion

> ❗ **Important**: Don’t persist the returned URL beyond the lifetime of the current process.

> **Note**: This method will return a well formed URL even if no item exists at the specified relative path in any relevant asset pack, in which case any attempts to get its contents—whether it’s a file or a directory—will fail.

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. Unlike [`contentsAtPath:asLocalizedForLanguage:options:error:`](./contentsatpath_aslocalizedforlanguage_options_error_.md) and [`fileDescriptorForPath:asLocalizedForLanguage:error:`](./filedescriptorforpath_aslocalizedforlanguage_error_.md), this method supports retrieving entire directories—including packages—in which case it merges the corresponding slices of the shared logical directory from all downloaded asset packs that are localized in the specified language and that contain such slices. If there’s a path collision across multiple such asset packs, then it’s undefined from which asset pack an individual file will be resolved.

> ⚠️ **Warning**: This method is less efficient than are [`contentsAtPath:asLocalizedForLanguage:options:error:`](./contentsatpath_aslocalizedforlanguage_options_error_.md) and [`fileDescriptorForPath:asLocalizedForLanguage:error:`](./filedescriptorforpath_aslocalizedforlanguage_error_.md); use those methods instead if you can do so. In particular, this method shouldn’t be used to get the URL to the root of the shared asset-pack namespace. Don’t use this method to block the main thread.

This method is most useful if you intentionally induce a file-path collision across multiple differently localized asset packs. For example, you may include an English-localized version of `Videos/Introduction.m4v` in an `en` asset pack, a Hebrew-localized version of `Videos/Introduction.m4v` in a `he` asset pack, and an American Spanish–localized version of `Videos/Introduction.m4v` in an `es-US` asset pack. If you offer split-language functionality to users, then you may want to download two or more of those asset packs on the same device. In that scenario, the specific choice of item the URL to which [`URLForPath:error:`](./urlforpath_error_.md) returns would be undefined. With this method, merely passing a language identifier to the `languageIdentifier` parameter is sufficient to resolve the ambiguity. [`URLForPath:error:`](./urlforpath_error_.md) is more suitable in most other situations.

> **Note**: Language matching considers implicit script and region tags per Unicode’s Common Locale Data Repository. For example, `en` is equivalent to `en-US` and `en-Latn-US` but not `en-CA`.

## Parameters

- `path`: The relative path.
- `languageIdentifier`: The language, represented as a BCP-47 identifier, that the framework uses to limit the search within localized asset packs.
- `error`: A pointer to an error that will be set if an error occurs.

## See Also

### Accessing asset contents
- [- contentsAtPath:searchingInAssetPackWithIdentifier:options:error:](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md)
  Returns the contents of an asset file at the specified relative path.
- [- contentsAtPath:asLocalizedForLanguage:options:error:](./contentsatpath_aslocalizedforlanguage_options_error_.md)
  Returns the contents of a localized asset file at the specified relative path.
- [- fileDescriptorForPath:searchingInAssetPackWithIdentifier:error:](./filedescriptorforpath_searchinginassetpackwithidentifier_error_.md)
  Opens and returns a file descriptor for the asset file at the specified relative path.
- [- fileDescriptorForPath:asLocalizedForLanguage:error:](./filedescriptorforpath_aslocalizedforlanguage_error_.md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [- URLForPath:error:](./urlforpath_error_.md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/urlforpath:aslocalizedforlanguage:error:)*