# CFBundleCopyBundleURL(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the location of a bundle.

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
func CFBundleCopyBundleURL(_ bundle: CFBundle!) -> CFURL!
```

#### Return Value

A CFURL object describing the location of `bundle`, or `NULL` if the specified bundle does not exist. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `bundle`: The bundle to examine.

## See Also

- [func CFBundleGetDevelopmentRegion(CFBundle!) -> CFString!](cfbundlegetdevelopmentregion(_:).md)
  Returns the bundle’s development region from the bundle’s information property list.
- [func CFBundleGetIdentifier(CFBundle!) -> CFString!](cfbundlegetidentifier(_:).md)
  Returns the bundle identifier from a bundle’s information property list.
- [func CFBundleGetInfoDictionary(CFBundle!) -> CFDictionary!](cfbundlegetinfodictionary(_:).md)
  Returns a bundle’s information dictionary.
- [func CFBundleGetLocalInfoDictionary(CFBundle!) -> CFDictionary!](cfbundlegetlocalinfodictionary(_:).md)
  Returns a bundle’s localized information dictionary.
- [func CFBundleGetValueForInfoDictionaryKey(CFBundle!, CFString!) -> CFTypeRef!](cfbundlegetvalueforinfodictionarykey(_:_:).md)
  Returns a value (localized if possible) from a bundle’s information dictionary.
- [func CFBundleCopyInfoDictionaryInDirectory(CFURL!) -> CFDictionary!](cfbundlecopyinfodictionaryindirectory(_:).md)
  Returns a bundle’s information dictionary.
- [func CFBundleCopyInfoDictionaryForURL(CFURL!) -> CFDictionary!](cfbundlecopyinfodictionaryforurl(_:).md)
  Returns the information dictionary for a given URL location.
- [func CFBundleGetPackageInfo(CFBundle!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!)](cfbundlegetpackageinfo(_:_:_:).md)
  Returns a bundle’s package type and creator.
- [func CFBundleGetPackageInfoInDirectory(CFURL!, UnsafeMutablePointer<UInt32>!, UnsafeMutablePointer<UInt32>!) -> Bool](cfbundlegetpackageinfoindirectory(_:_:_:).md)
  Returns a bundle’s package type and creator without having to create a CFBundle object.
- [func CFBundleCopyExecutableArchitectures(CFBundle!) -> CFArray!](cfbundlecopyexecutablearchitectures(_:).md)
  Returns an array of CFNumbers representing the architectures a given bundle provides.
- [func CFBundleCopyExecutableArchitecturesForURL(CFURL!) -> CFArray!](cfbundlecopyexecutablearchitecturesforurl(_:).md)
  Returns an array of CFNumbers representing the architectures a given URL provides.
- [func CFBundleGetVersionNumber(CFBundle!) -> UInt32](cfbundlegetversionnumber(_:).md)
  Returns a bundle’s version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopybundleurl(_:))*