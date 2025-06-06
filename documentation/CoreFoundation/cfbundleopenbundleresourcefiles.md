# CFBundleOpenBundleResourceFiles(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Opens the non-localized and localized resource files (if any) for a bundle in separate resource maps.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func CFBundleOpenBundleResourceFiles(_ bundle: CFBundle!, _ refNum: UnsafeMutablePointer<CFBundleRefNum>!, _ localizedRefNum: UnsafeMutablePointer<CFBundleRefNum>!) -> Int32
```

#### Return Value

An error code. The function returns `0` (`noErr`) if successful. If the bundle contains more than one resource file, the function returns an error code only if none was opened. The most common error is `resFNotFound`, but the function may also pass through other errors returned from the Resource Manager.

## Parameters

- `bundle`: The bundle whose resource map you want to open.
- `refNum`: On return, the reference number of the non-localized resource map.
- `localizedRefNum`: On return, the reference number of the localized resource map.

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
- [func CFBundleOpenBundleResourceMap(CFBundle!) -> CFBundleRefNum](cfbundleopenbundleresourcemap(_:).md)
  Opens the non-localized and localized resource files (if any) for a bundle in a single resource map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleopenbundleresourcefiles(_:_:_:))*