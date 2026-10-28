# CFBundleCloseBundleResourceMap(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Closes an open resource map for a bundle.

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

> **Deprecated**: The Carbon Resource Manager is deprecated. This should only be used to access Resource Manager-style resources in old bundles.

## Declaration

```swift
func CFBundleCloseBundleResourceMap(_ bundle: CFBundle!, _ refNum: CFBundleRefNum)
```

```c
extern void CFBundleCloseBundleResourceMap(CFBundleRef bundle, CFBundleRefNum refNum);
```

## Discussion

You open a resource map using either [`CFBundleOpenBundleResourceFiles(_:_:_:)`](./cfbundleopenbundleresourcefiles%28_,_,_%29.md) or [`CFBundleOpenBundleResourceMap(_:)`](./cfbundleopenbundleresourcemap%28_%29.md).

## Parameters

- `bundle`: The bundle whose resource map is referenced by `refNum`.
- `refNum`: The reference number for a resource map to close.

## See Also

### Locating Bundle Resources
- [func CFBundleCopyResourceURL(CFBundle!, CFString!, CFString!, CFString!) -> CFURL!](./cfbundlecopyresourceurl%28_,_,_,_%29.md)
  Returns the location of a resource contained in the specified bundle.
- [func CFBundleCopyResourceURLInDirectory(CFURL!, CFString!, CFString!, CFString!) -> CFURL!](./cfbundlecopyresourceurlindirectory%28_,_,_,_%29.md)
  Returns the location of a resource contained in the specified bundle directory without requiring the creation of a CFBundle object.
- [func CFBundleCopyResourceURLsOfType(CFBundle!, CFString!, CFString!) -> CFArray!](./cfbundlecopyresourceurlsoftype%28_,_,_%29.md)
  Assembles an array of URLs specifying all of the resources of the specified type found in a bundle.
- [func CFBundleCopyResourceURLsOfTypeInDirectory(CFURL!, CFString!, CFString!) -> CFArray!](./cfbundlecopyresourceurlsoftypeindirectory%28_,_,_%29.md)
  Returns an array of CFURL objects describing the locations of all resources in a bundle of the specified type without needing to create a CFBundle object.
- [func CFBundleCopyResourceURLForLocalization(CFBundle!, CFString!, CFString!, CFString!, CFString!) -> CFURL!](./cfbundlecopyresourceurlforlocalization%28_,_,_,_,_%29.md)
  Returns the location of a localized resource in a bundle.
- [func CFBundleCopyResourceURLsOfTypeForLocalization(CFBundle!, CFString!, CFString!, CFString!) -> CFArray!](./cfbundlecopyresourceurlsoftypeforlocalization%28_,_,_,_%29.md)
  Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [func CFBundleOpenBundleResourceFiles(CFBundle!, UnsafeMutablePointer<CFBundleRefNum>!, UnsafeMutablePointer<CFBundleRefNum>!) -> Int32](./cfbundleopenbundleresourcefiles%28_,_,_%29.md)
  Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.
- [func CFBundleOpenBundleResourceMap(CFBundle!) -> CFBundleRefNum](./cfbundleopenbundleresourcemap%28_%29.md)
  Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleclosebundleresourcemap(_:_:))*