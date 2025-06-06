# CFBundleCopyResourceURLForLocalization(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the location of a localized resource in a bundle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFBundleCopyResourceURLForLocalization(_ bundle: CFBundle!, _ resourceName: CFString!, _ resourceType: CFString!, _ subDirName: CFString!, _ localizationName: CFString!) -> CFURL!
```

#### Return Value

The location of a localized resource in `bundle`, or `NULL` if the resource could not be found. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note that file names are case-sensitive, even on file systems (such as HFS+) that are not case sensitive with regards to file names.

You should typically have little reason to use this function (see Getting the Current Language and Locale)—CFBundle’s interfaces automatically apply the user’s preferences to determine which localized resource files to return in response to a programmatic request. See also [`CFBundleCopyBundleLocalizations(_:)`](cfbundlecopybundlelocalizations(_:).md) for how to determine what localizations are available

## Parameters

- `bundle`: The bundle to examine.
- `resourceName`: The name of the requested resource.
- `resourceType`: The abstract type of the resource to locate. The type is expressed as a filename extension, such as  .
- `subDirName`: The name of the subdirectory of the bundle’s resources directory to search. Pass   to search the standard CFBundle resource locations.
- `localizationName`: The name of the localization. This value should correspond to the name of one of the bundle’s language-specific resource directories without the   extension. (This parameter is treated literally: If you pass  , the function will not match resources in a   directory in the bundle.)

## See Also

- [func CFBundleCloseBundleResourceMap(CFBundle!, CFBundleRefNum)](cfbundleclosebundleresourcemap(_:_:).md)
  Closes an open resource map for a bundle.
- [func CFBundleCopyResourceURL(CFBundle!, CFString!, CFString!, CFString!) -> CFURL!](cfbundlecopyresourceurl(_:_:_:_:).md)
  Returns the location of a resource contained in the specified bundle.
- [func CFBundleCopyResourceURLInDirectory(CFURL!, CFString!, CFString!, CFString!) -> CFURL!](cfbundlecopyresourceurlindirectory(_:_:_:_:).md)
  Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [func CFBundleCopyResourceURLsOfType(CFBundle!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftype(_:_:_:).md)
  Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [func CFBundleCopyResourceURLsOfTypeInDirectory(CFURL!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftypeindirectory(_:_:_:).md)
  Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [func CFBundleCopyResourceURLsOfTypeForLocalization(CFBundle!, CFString!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftypeforlocalization(_:_:_:_:).md)
  Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [func CFBundleOpenBundleResourceFiles(CFBundle!, UnsafeMutablePointer<CFBundleRefNum>!, UnsafeMutablePointer<CFBundleRefNum>!) -> Int32](cfbundleopenbundleresourcefiles(_:_:_:).md)
  Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.
- [func CFBundleOpenBundleResourceMap(CFBundle!) -> CFBundleRefNum](cfbundleopenbundleresourcemap(_:).md)
  Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyresourceurlforlocalization(_:_:_:_:_:))*