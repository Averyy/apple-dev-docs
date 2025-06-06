# CFBundleGetVersionNumber(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a bundle’s version number.

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
func CFBundleGetVersionNumber(_ bundle: CFBundle!) -> UInt32
```

#### Return Value

A `vers` resource style version number. If it is a string, it is automatically converted to the numeric representation, where the major version number is restricted to 2 BCD digits (in other words, it must be in the range 0-99) and the minor and bug fix version numbers are each restricted to a single BCD digit (0-9).

#### Discussion

This function is only supported for the `vers` resource style version numbers. Where other version number styles—namely X, or X.Y, or X.Y.Z—are used, you can use [`CFBundleGetValueForInfoDictionaryKey(_:_:)`](cfbundlegetvalueforinfodictionarykey(_:_:).md) with the key `kCFBundleVersionKey` to extract the version number as a string from the bundle’s information dictionary.

Some version numbers of the form X, X.Y, and X.Y.Z may work with this function, if X <= 99, Y <= 9, and Z <= 9. Thus a version number 76.5.4 will work, but 76.12 will not work.

## Parameters

- `bundle`: The bundle to examine. The bundle’s version number can be number or a string of the standard form “2.5.3d5”.

## See Also

- [func CFBundleCopyBundleURL(CFBundle!) -> CFURL!](cfbundlecopybundleurl(_:).md)
  Returns the location of a bundle.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetversionnumber(_:))*