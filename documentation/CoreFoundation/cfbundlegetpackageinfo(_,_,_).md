# CFBundleGetPackageInfo(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a bundle’s package type and creator.

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
func CFBundleGetPackageInfo(_ bundle: CFBundle!, _ packageType: UnsafeMutablePointer<UInt32>!, _ packageCreator: UnsafeMutablePointer<UInt32>!)
```

```c
extern void CFBundleGetPackageInfo(CFBundleRef bundle, UInt32 *packageType, UInt32 *packageCreator);
```

## Parameters

- `bundle`: The bundle to examine.
- `packageType`: On return, the four-letter type code for the bundle. This is `APPL` for applications, `FMWK` for frameworks, and `BNDL` for generic bundles. Or a more specific type code for generic bundles.
- `packageCreator`: On return, the four-letter “creator” code for the bundle.

## See Also

### Getting Bundle Properties
- [func CFBundleCopyBundleURL(CFBundle!) -> CFURL!](./cfbundlecopybundleurl%28_%29.md)
  Returns the location of a bundle.
- [func CFBundleGetDevelopmentRegion(CFBundle!) -> CFString!](./cfbundlegetdevelopmentregion%28_%29.md)
  Returns the bundle’s development region from the bundle’s information property list.
- [func CFBundleGetIdentifier(CFBundle!) -> CFString!](./cfbundlegetidentifier%28_%29.md)
  Returns the bundle identifier from a bundle’s information property list.
- [func CFBundleGetInfoDictionary(CFBundle!) -> CFDictionary!](./cfbundlegetinfodictionary%28_%29.md)
  Returns a bundle’s information dictionary.
- [func CFBundleGetLocalInfoDictionary(CFBundle!) -> CFDictionary!](./cfbundlegetlocalinfodictionary%28_%29.md)
  Returns a bundle’s localized information dictionary.
- [func CFBundleGetValueForInfoDictionaryKey(CFBundle!, CFString!) -> CFTypeRef!](./cfbundlegetvalueforinfodictionarykey%28_,_%29.md)
  Returns a value (localized if possible) from a bundle’s information dictionary.
- [func CFBundleCopyInfoDictionaryInDirectory(CFURL!) -> CFDictionary!](./cfbundlecopyinfodictionaryindirectory%28_%29.md)
  Returns a bundle’s information dictionary.
- [func CFBundleCopyInfoDictionaryForURL(CFURL!) -> CFDictionary!](./cfbundlecopyinfodictionaryforurl%28_%29.md)
  Returns the information dictionary for a given URL location.
- [func CFBundleGetPackageInfoInDirectory(CFURL!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!) -> Bool](./cfbundlegetpackageinfoindirectory%28_,_,_%29.md)
  Returns a bundle’s package type and creator without having to create a CFBundle object.
- [func CFBundleCopyExecutableArchitectures(CFBundle!) -> CFArray!](./cfbundlecopyexecutablearchitectures%28_%29.md)
  Returns an array of CFNumbers representing the architectures a given bundle provides.
- [func CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!](./cfbundlecopyexecutablearchitecturesforurl%28_%29.md)
  Returns an array of CFNumbers representing the architectures a given URL provides.
- [func CFBundleGetVersionNumber(CFBundle!) -> UInt32](./cfbundlegetversionnumber%28_%29.md)
  Returns a bundle’s version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetpackageinfo(_:_:_:))*