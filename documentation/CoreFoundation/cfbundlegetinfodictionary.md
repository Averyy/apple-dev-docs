# CFBundleGetInfoDictionary(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a bundle’s information dictionary.

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
func CFBundleGetInfoDictionary(_ bundle: CFBundle!) -> CFDictionary!
```

#### Return Value

A CFDictionary object containing the data stored in the bundle’s information property list (the `Info.plist` file). This is a global information dictionary. CFBundle may add extra keys to this dictionary for its own use. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

You should typically use [`CFBundleGetValueForInfoDictionaryKey(_:_:)`](cfbundlegetvalueforinfodictionarykey(_:_:).md) rather than retrieving values directly from the info dictionary because the function will return localized values if any are available. Use `CFBundleGetInfoDictionary` only if you know that the key you are interested in will not be localized.

To retrieve an info dictionary without creating a CFBundle object, see [`CFBundleCopyInfoDictionaryInDirectory(_:)`](cfbundlecopyinfodictionaryindirectory(_:).md) and [`CFBundleCopyInfoDictionaryForURL(_:)`](cfbundlecopyinfodictionaryforurl(_:).md).

## Parameters

- `bundle`: The bundle to examine.

## See Also

- [func CFBundleCopyBundleURL(CFBundle!) -> CFURL!](cfbundlecopybundleurl(_:).md)
  Returns the location of a bundle.
- [func CFBundleGetDevelopmentRegion(CFBundle!) -> CFString!](cfbundlegetdevelopmentregion(_:).md)
  Returns the bundle’s development region from the bundle’s information property list.
- [func CFBundleGetIdentifier(CFBundle!) -> CFString!](cfbundlegetidentifier(_:).md)
  Returns the bundle identifier from a bundle’s information property list.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetinfodictionary(_:))*