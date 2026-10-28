# contentsAtPath:asLocalizedForLanguage:options:error:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns the contents of a localized asset file at the specified relative path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (NSData *) contentsAtPath:(NSString *) path asLocalizedForLanguage:(NSString *) languageIdentifier options:(NSDataReadingOptions) options error:(NSError **) error;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

## Return Value

The file’s contents or `nil` if an error occurred.

## Discussion

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. This method searches in only the downloaded asset packs that are localized in the specified language. If there’s a file-path collision across multiple such asset packs, then it’s undefined from which asset pack the file will be read.

This method is most useful if you intentionally induce a file-path collision across multiple differently localized asset packs. For example, you may include an English-localized version of `Videos/Introduction.m4v` in an `en` asset pack, a Hebrew-localized version of `Videos/Introduction.m4v` in a `he` asset pack, and an American Spanish–localized version of `Videos/Introduction.m4v` in an `es-US` asset pack. If you offer split-language functionality to users, then you may want to download two or more of those asset packs on the same device. In that scenario, the specific choice of file that [`contentsAtPath:searchingInAssetPackWithIdentifier:options:error:`](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md) reads would be undefined unless you determine the appropriate asset pack’s identifier and pass it to that method’s `assetPackIdentifier` parameter. With this method, merely passing a language identifier to the `languageIdentifier` parameter is sufficient to resolve the ambiguity without requiring that you determine the asset pack’s identifier. [`contentsAtPath:searchingInAssetPackWithIdentifier:options:error:`](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md) is more suitable in most other situations.

> **Note**: Language matching considers implicit script and region tags per Unicode’s Common Locale Data Repository. For example, `en` is equivalent to `en-US` and `en-Latn-US` but not `en-CA`.

## Parameters

- `path`: The relative path.
- `languageIdentifier`: The language, represented as a BCP-47 identifier, that the framework uses to limit the search within localized asset packs.
- `options`: Options for how to read the file’s contents into a data object.
- `error`: A pointer to an error that will be set if an error occurs. If no file is found at `path`, then `error` will point to an `NSError` object with [`BAManagedErrorCodeFileNotFound`](../bamanagederrorcode/bamanagederrorcodefilenotfound.md) as its code.

## See Also

### Accessing asset contents
- [- contentsAtPath:searchingInAssetPackWithIdentifier:options:error:](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md)
  Returns the contents of an asset file at the specified relative path.
- [- fileDescriptorForPath:searchingInAssetPackWithIdentifier:error:](./filedescriptorforpath_searchinginassetpackwithidentifier_error_.md)
  Opens and returns a file descriptor for the asset file at the specified relative path.
- [- fileDescriptorForPath:asLocalizedForLanguage:error:](./filedescriptorforpath_aslocalizedforlanguage_error_.md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [- URLForPath:error:](./urlforpath_error_.md)
  Returns a URL for the specified relative path.
- [- URLForPath:asLocalizedForLanguage:error:](./urlforpath_aslocalizedforlanguage_error_.md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/contentsatpath:aslocalizedforlanguage:options:error:)*