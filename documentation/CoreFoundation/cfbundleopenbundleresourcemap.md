# CFBundleOpenBundleResourceMap(_:)

**Framework**: Core Foundation  
**Kind**: func

Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFBundleOpenBundleResourceMap(_ bundle: CFBundle!) -> CFBundleRefNum
```

#### Return Value

A distinct reference number for the resource map.

#### Discussion

Creates and makes current a single read-only resource map containing the non-localized and localized resource files. If this function is called multiple times, it opens the files multiple times and returns distinct reference numbers for each. Use [`CFBundleCloseBundleResourceMap(_:_:)`](cfbundleclosebundleresourcemap(_:_:).md) to close a resource map.

## Parameters

- `bundle`: The bundle whose resource map you want to open.

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
- [func CFBundleCopyResourceURLForLocalization(CFBundle!, CFString!, CFString!, CFString!, CFString!) -> CFURL!](cfbundlecopyresourceurlforlocalization(_:_:_:_:_:).md)
  Returns the location of a localized resource in a bundle.
- [func CFBundleCopyResourceURLsOfTypeForLocalization(CFBundle!, CFString!, CFString!, CFString!) -> CFArray!](cfbundlecopyresourceurlsoftypeforlocalization(_:_:_:_:).md)
  Returns an array containing copies of the URL locations for a specified bundle, resource, and localization name.
- [func CFBundleOpenBundleResourceFiles(CFBundle!, UnsafeMutablePointer<CFBundleRefNum>!, UnsafeMutablePointer<CFBundleRefNum>!) -> Int32](cfbundleopenbundleresourcefiles(_:_:_:).md)
  Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleopenbundleresourcemap(_:))*