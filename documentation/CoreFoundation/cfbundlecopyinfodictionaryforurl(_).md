# CFBundleCopyInfoDictionaryForURL(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the information dictionary for a given URL location.

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
func CFBundleCopyInfoDictionaryForURL(_ url: CFURL!) -> CFDictionary!
```

```c
extern CFDictionaryRefCFBundleCopyInfoDictionaryForURL(CFURLRef url);
```

## Return Value

A CFDictionary object containing `url`’s information dictionary. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

For a directory URL, this is equivalent to [`CFBundleCopyInfoDictionaryInDirectory(_:)`](./cfbundlecopyinfodictionaryindirectory%28_%29.md). For a plain file URL representing an unbundled application, this function will attempt to read an information dictionary either from the `(__TEXT, __info_plist)` section of the file (for a Mach-O file) or from a `plst` resource.

## Parameters

- `url`: A CFURL object describing the location of a file.

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
- [func CFBundleGetPackageInfo(CFBundle!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!)](./cfbundlegetpackageinfo%28_,_,_%29.md)
  Returns a bundle’s package type and creator.
- [func CFBundleGetPackageInfoInDirectory(CFURL!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!) -> Bool](./cfbundlegetpackageinfoindirectory%28_,_,_%29.md)
  Returns a bundle’s package type and creator without having to create a CFBundle object.
- [func CFBundleCopyExecutableArchitectures(CFBundle!) -> CFArray!](./cfbundlecopyexecutablearchitectures%28_%29.md)
  Returns an array of CFNumbers representing the architectures a given bundle provides.
- [func CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!](./cfbundlecopyexecutablearchitecturesforurl%28_%29.md)
  Returns an array of CFNumbers representing the architectures a given URL provides.
- [func CFBundleGetVersionNumber(CFBundle!) -> UInt32](./cfbundlegetversionnumber%28_%29.md)
  Returns a bundle’s version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyinfodictionaryforurl(_:))*