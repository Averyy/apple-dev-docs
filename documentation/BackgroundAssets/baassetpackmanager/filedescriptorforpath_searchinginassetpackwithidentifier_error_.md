# fileDescriptorForPath:searchingInAssetPackWithIdentifier:error:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Opens and returns a file descriptor for the asset file at the specified relative path.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (int) fileDescriptorForPath:(NSString *) path searchingInAssetPackWithIdentifier:(NSString *) assetPackIdentifier error:(NSError **) error;
```

## Return Value

A descriptor for the opened file. A return value of `-1` indicates that an error occurred.

## Discussion

> ❗ **Important**: It’s your responsibility to close the file descriptor when you’re done using it.

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. If there’s a file-path collision across multiple asset packs, then it’s undefined from which asset pack the file will be opened unless you explicitly limit the search to a particular asset pack by passing a non-`nil` identifier to the `assetPackIdentifier` parameter.

> **Remark**: Use this method if you need low-level access to the file descriptor. If you don’t, then use [`contentsAtPath:searchingInAssetPackWithIdentifier:options:error:`](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md) instead.

## Parameters

- `path`: The relative file path.
- `assetPackIdentifier`: The identifier of the asset pack in which you want to search for the file or `nil` if you want to search in all asset packs.
- `error`: A pointer to an error that will be set if an error occurs. If no file is found at `path`, then it will point to an `NSError` object with [`BAManagedErrorCodeFileNotFound`](../bamanagederrorcode/bamanagederrorcodefilenotfound.md) as its code.

## See Also

### Accessing asset contents
- [- contentsAtPath:searchingInAssetPackWithIdentifier:options:error:](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md)
  Returns the contents of an asset file at the specified relative path.
- [- contentsAtPath:asLocalizedForLanguage:options:error:](./contentsatpath_aslocalizedforlanguage_options_error_.md)
  Returns the contents of a localized asset file at the specified relative path.
- [- fileDescriptorForPath:asLocalizedForLanguage:error:](./filedescriptorforpath_aslocalizedforlanguage_error_.md)
  Opens and returns a file descriptor for a localized asset file at the specified relative path.
- [- URLForPath:error:](./urlforpath_error_.md)
  Returns a URL for the specified relative path.
- [- URLForPath:asLocalizedForLanguage:error:](./urlforpath_aslocalizedforlanguage_error_.md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/filedescriptorforpath:searchinginassetpackwithidentifier:error:)*