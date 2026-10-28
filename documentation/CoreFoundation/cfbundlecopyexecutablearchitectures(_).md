# CFBundleCopyExecutableArchitectures(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns an array of CFNumbers representing the architectures a given bundle provides.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFBundleCopyExecutableArchitectures(_ bundle: CFBundle!) -> CFArray!
```

```c
extern CFArrayRefCFBundleCopyExecutableArchitectures(CFBundleRef bundle);
```

## Return Value

If the bundle’s executable exists and is a Mach-O file, returns an array of CFNumbers whose values are integers representing the architectures the file provides. Possible values are listed in [Architecture Types](./api-1537096-architecture-types.md). If the executable is not a Mach-O file, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `bundle`: The bundle to examine.

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
- [func CFBundleGetPackageInfo(CFBundle!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!)](./cfbundlegetpackageinfo%28_,_,_%29.md)
  Returns a bundle’s package type and creator.
- [func CFBundleGetPackageInfoInDirectory(CFURL!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!) -> Bool](./cfbundlegetpackageinfoindirectory%28_,_,_%29.md)
  Returns a bundle’s package type and creator without having to create a CFBundle object.
- [func CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!](./cfbundlecopyexecutablearchitecturesforurl%28_%29.md)
  Returns an array of CFNumbers representing the architectures a given URL provides.
- [func CFBundleGetVersionNumber(CFBundle!) -> UInt32](./cfbundlegetversionnumber%28_%29.md)
  Returns a bundle’s version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyexecutablearchitectures(_:))*