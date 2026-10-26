# CFBundleCopyLocalizedStringForLocalizations(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a localized string from a bundle’s strings file.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func CFBundleCopyLocalizedStringForLocalizations(_ bundle: CFBundle!, _ key: CFString!, _ value: CFString!, _ tableName: CFString!, _ localizations: CFArray!) -> CFString!
```

```c
extern CFStringRefCFBundleCopyLocalizedStringForLocalizations(CFBundleRef bundle, CFStringRef key, CFStringRef value, CFStringRef tableName, CFArrayRef localizations);
```

#### Return Value

A CFString object that contains the localized string. If no value exists for `key`, returns `value` unless `value` is `NULL` or an empty string, in which case `key` is returned instead. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Returns a localized string given a list of possible localizations. The one most suitable to use with the given `bundle` is returned.

## Parameters

- `bundle`: The bundle to examine.
- `key`: The key for the localized string to retrieve. This key will be used to look up the localized string in the strings file. Typically the key is identical to the value of the localized string in the development language.
- `value`: A default value to return if no value exists for `key`.
- `tableName`: The name of the strings file to search. The name should not include the `strings` filename extension. The case of the string must match that of the file name, even on file systems (such as HFS+) that are not case sensitive with regards to file names
- `localizations`: An array of BCP 47 language codes corresponding to available localizations. Bundle compares the array against its available localizations, and uses the best result to retrieve the localized string. If empty, we treat it as no localization is available, and may return a fallback.

## See Also

### Functions
- [func CFAllocatorAllocateBytes(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorallocatebytes%28_,_,_%29.md)
- [func CFAllocatorAllocateTyped(CFAllocator!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorallocatetyped%28_,_,_,_%29.md)
- [func CFAllocatorReallocateBytes(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorreallocatebytes%28_,_,_,_%29.md)
- [func CFAllocatorReallocateTyped(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorreallocatetyped%28_,_,_,_,_%29.md)
- [func CFAttributedStringGetBidiLevelsAndResolvedDirections(CFAttributedString!, CFRange, Int8, UnsafeMutablePointer<UInt8>!, UnsafeMutablePointer<UInt8>!) -> Bool](./cfattributedstringgetbidilevelsandresolveddirections%28_,_,_,_,_%29.md)
- [func CFBundleIsArchitectureLoadable(cpu_type_t) -> Bool](./cfbundleisarchitectureloadable%28_%29.md)
- [func CFBundleIsExecutableLoadable(CFBundle!) -> Bool](./cfbundleisexecutableloadable%28_%29.md)
- [func CFBundleIsExecutableLoadableForURL(CFURL!) -> Bool](./cfbundleisexecutableloadableforurl%28_%29.md)
- [func CFCopyHomeDirectoryURL() -> CFURL!](./cfcopyhomedirectoryurl%28%29.md)
- [func CFDateFormatterCreateISO8601Formatter(CFAllocator!, CFISO8601DateFormatOptions) -> CFDateFormatter!](./cfdateformattercreateiso8601formatter%28_,_%29.md)
- [func CFFileSecurityClearProperties(CFFileSecurity!, CFFileSecurityClearOptions) -> Bool](./cffilesecurityclearproperties%28_,_%29.md)
  Clears properties from a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t?>!) -> Bool](./cffilesecuritycopyaccesscontrollist%28_,_%29.md)
  Copies the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](./cffilesecuritycopygroupuuid%28_,_%29.md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](./cffilesecuritycopyowneruuid%28_,_%29.md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!](./cffilesecuritycreate%28_%29.md)
  Creates a `CFFileSecurityRef` object.
- [CFAutorelease](./cfautorelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizedstringforlocalizations(_:_:_:_:_:))*