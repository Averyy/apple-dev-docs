# CFBundleCopyResourceURLsOfTypeInDirectory(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFBundleCopyResourceURLsOfTypeInDirectory(_ bundleURL: CFURL!, _ resourceType: CFString!, _ subDirName: CFString!) -> CFArray!
```

```c
extern CFArrayRefCFBundleCopyResourceURLsOfTypeInDirectory(CFURLRef bundleURL, CFStringRef resourceType, CFStringRef subDirName);
```

## Return Value

A CFArray object containing the CFURL objects of the requested resources. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function provides a means to obtain an array containing the locations of all of the requested resources without first creating a CFBundle object. However, since CFBundle objects cache search results, it is faster to create a CFBundle object if you need to repeatedly access resources.

Note that file names are case-sensitive, even on file systems (such as HFS+) that are not case sensitive with regards to file names.

## Parameters

- `bundleURL`: The location of a bundle to examine.
- `resourceType`: The abstract type of the resources to locate. The type is expressed as a filename extension, such as `jpg`.
- `subDirName`: The name of the subdirectory of the bundle’s resources directory to search. Pass `NULL` to search the standard CFBundle resource locations.

## See Also

### Locating Bundle Resources
- [func CFBundleCloseBundleResourceMap(CFBundle!, CFBundleRefNum)](./cfbundleclosebundleresourcemap%28_,_%29.md)
  Closes an open resource map for a bundle.
- [func CFBundleCopyResourceURL(CFBundle!, CFString!, CFString!, CFString!) -> CFURL!](./cfbundlecopyresourceurl%28_,_,_,_%29.md)
  Returns the location of a resource contained in the specified bundle.
- [func CFBundleCopyResourceURLInDirectory(CFURL!, CFString!, CFString!, CFString!) -> CFURL!](./cfbundlecopyresourceurlindirectory%28_,_,_,_%29.md)
  Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [func CFBundleCopyResourceURLsOfType(CFBundle!, CFString!, CFString!) -> CFArray!](./cfbundlecopyresourceurlsoftype%28_,_,_%29.md)
  Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [func CFBundleCopyResourceURLForLocalization(CFBundle!, CFString!, CFString!, CFString!, CFString!) -> CFURL!](./cfbundlecopyresourceurlforlocalization%28_,_,_,_,_%29.md)
  Returns the location of a localized resource in a bundle.
- [func CFBundleCopyResourceURLsOfTypeForLocalization(CFBundle!, CFString!, CFString!, CFString!) -> CFArray!](./cfbundlecopyresourceurlsoftypeforlocalization%28_,_,_,_%29.md)
  Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [func CFBundleOpenBundleResourceFiles(CFBundle!, UnsafeMutablePointer<CFBundleRefNum>!, UnsafeMutablePointer<CFBundleRefNum>!) -> Int32](./cfbundleopenbundleresourcefiles%28_,_,_%29.md)
  Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.
- [func CFBundleOpenBundleResourceMap(CFBundle!) -> CFBundleRefNum](./cfbundleopenbundleresourcemap%28_%29.md)
  Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyresourceurlsoftypeindirectory(_:_:_:))*