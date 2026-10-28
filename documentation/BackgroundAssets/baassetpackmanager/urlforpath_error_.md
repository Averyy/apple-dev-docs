# URLForPath:error:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns a URL for the specified relative path.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (NSURL *) URLForPath:(NSString *) path error:(NSError **) error;
```

## Return Value

The URL to the item or `nil` if an error occurred.

## Discussion

> ⚠️ **Warning**: Don’t persist the returned URL beyond the lifetime of the current process.

> **Note**: This method will return a well formed URL even if no item exists at the specified relative path in any asset pack, in which case any attempts to get its contents—whether it’s a file or a directory—will fail.

All asset packs share the same namespace, so you can treat the overall collection of downloaded asset packs as if it were a single root directory that contains all of your subdirectories and asset files, regardless of the specific asset pack in which any particular file resides. Unlike [`contentsAtPath:searchingInAssetPackWithIdentifier:options:error:`](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md) and [`fileDescriptorForPath:searchingInAssetPackWithIdentifier:error:`](./filedescriptorforpath_searchinginassetpackwithidentifier_error_.md), this method supports retrieving entire directories—including packages—in which case it merges the corresponding slices of the shared logical directory from all downloaded asset packs that contain such slices. If there’s a file-path collision across multiple asset packs, then it’s undefined from which asset pack an individual file will be resolved.

> ⚠️ **Warning**: This method is less efficient than are [`contentsAtPath:searchingInAssetPackWithIdentifier:options:error:`](./contentsatpath_searchinginassetpackwithidentifier_options_error_.md) and [`fileDescriptorForPath:searchingInAssetPackWithIdentifier:error:`](./filedescriptorforpath_searchinginassetpackwithidentifier_error_.md); use those methods instead if you can do so. In particular, this method shouldn’t be used to get the URL to the root of the shared asset-pack namespace. Don’t use this method to block the main thread.

## Parameters

- `path`: The relative file path.
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
- [- URLForPath:asLocalizedForLanguage:error:](./urlforpath_aslocalizedforlanguage_error_.md)
  Returns a URL for the specified relative path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/urlforpath:error:)*