# url(forResource:withExtension:subdirectory:localization:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the file URL for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(forResource name: String?, withExtension ext: String?, subdirectory subpath: String?, localization localizationName: String?) -> URL?
```

```objc
- (NSURL *) URLForResource:(NSString *) name withExtension:(NSString *) ext subdirectory:(NSString *) subpath localization:(NSString *) localizationName;
```

## Return Value

The file URL for the resource file or `nil` if the file could not be located.

## Discussion

This method is equivalent to [`urls(forResourcesWithExtension:subdirectory:)`](./urls%28forresourceswithextension,subdirectory%29.md), except that only nonlocalized resources and those in the language-specific `.lproj` directory specified by `localizationName` are searched.

There should typically be little reason to use this method—see Getting the Current Language and Locale. See also [`preferredLocalizations(from:forPreferences:)`](./preferredlocalizations%28from,forpreferences%29.md) for how to determine what localizations are available.

## Parameters

- `name`: The name of the resource file.

  If you specify `nil`, the method returns the first resource file it finds that matches the remaining criteria.
- `ext`: The filename extension of the file to locate.

  If you specify an empty string or `nil`, the extension is assumed not to exist and the file URL is the first file encountered that exactly matches `name`.
- `subpath`: The name of the bundle subdirectory to search.
- `localizationName`: The language ID for the localization. This parameter should correspond to the name of one of the bundle’s language-specific resource directories without the `.lproj` extension.

## See Also

### Finding resource files
- [func url(forResource: String?, withExtension: String?, subdirectory: String?) -> URL?](./url%28forresource,withextension,subdirectory%29.md)
  Returns the file URL for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [func url(forResource: String?, withExtension: String?) -> URL?](./url%28forresource,withextension%29.md)
  Returns the file URL for the resource identified by the specified name and file extension.
- [func urls(forResourcesWithExtension: String?, subdirectory: String?) -> [URL]?](./urls%28forresourceswithextension,subdirectory%29.md)
  Returns an array of file URLs for all resources identified by the specified file extension and located in the specified bundle subdirectory.
- [func urls(forResourcesWithExtension: String?, subdirectory: String?, localization: String?) -> [URL]?](./urls%28forresourceswithextension,subdirectory,localization%29.md)
  Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [class func url(forResource: String?, withExtension: String?, subdirectory: String?, in: URL) -> URL?](./url%28forresource,withextension,subdirectory,in%29.md)
  Creates and returns a file URL for the resource with the specified name and extension in the specified bundle.
- [class func urls(forResourcesWithExtension: String?, subdirectory: String?, in: URL) -> [URL]?](./urls%28forresourceswithextension,subdirectory,in%29.md)
  Returns an array containing the file URLs for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, within the specified bundle.
- [func path(forResource: String?, ofType: String?) -> String?](./path%28forresource,oftype%29.md)
  Returns the full pathname for the resource identified by the specified name and file extension.
- [func path(forResource: String?, ofType: String?, inDirectory: String?) -> String?](./path%28forresource,oftype,indirectory%29-swift.method.md)
  Returns the full pathname for the resource identified by the specified name and file extension and located in the specified bundle subdirectory.
- [func path(forResource: String?, ofType: String?, inDirectory: String?, forLocalization: String?) -> String?](./path%28forresource,oftype,indirectory,forlocalization%29.md)
  Returns the full pathname for the resource identified by the specified name and file extension, located in the specified bundle subdirectory, and limited to global resources and those associated with the specified localization.
- [func paths(forResourcesOfType: String?, inDirectory: String?) -> [String]](./paths%28forresourcesoftype,indirectory%29-swift.method.md)
  Returns an array containing the pathnames for all bundle resources having the specified filename extension and residing in the resource subdirectory.
- [func paths(forResourcesOfType: String?, inDirectory: String?, forLocalization: String?) -> [String]](./paths%28forresourcesoftype,indirectory,forlocalization%29.md)
  Returns an array containing the file for all bundle resources having the specified filename extension, residing in the specified resource subdirectory, and limited to global resources and those associated with the specified localization.
- [class func path(forResource: String?, ofType: String?, inDirectory: String) -> String?](./path%28forresource,oftype,indirectory%29-swift.type.method.md)
  Returns the full pathname for the resource file identified by the specified name and extension and residing in a given bundle directory.
- [class func paths(forResourcesOfType: String?, inDirectory: String) -> [String]](./paths%28forresourcesoftype,indirectory%29-swift.type.method.md)
  Returns an array containing the pathnames for all bundle resources having the specified extension and residing in the bundle directory at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/url(forresource:withextension:subdirectory:localization:))*