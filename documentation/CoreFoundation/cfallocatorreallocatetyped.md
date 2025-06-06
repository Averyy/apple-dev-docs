# CFAllocatorReallocateTyped(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func CFAllocatorReallocateTyped(_ allocator: CFAllocator!, _ ptr: UnsafeMutableRawPointer!, _ newsize: CFIndex, _ descriptor: CFAllocatorTypeID, _ hint: CFOptionFlags) -> UnsafeMutableRawPointer!
```

## See Also

- [func CFAllocatorAllocateBytes(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocatebytes(_:_:_:).md)
- [func CFAllocatorAllocateTyped(CFAllocator!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocatetyped(_:_:_:_:).md)
- [func CFAllocatorReallocateBytes(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocatebytes(_:_:_:_:).md)
- [func CFAttributedStringGetBidiLevelsAndResolvedDirections(CFAttributedString!, CFRange, Int8, UnsafeMutablePointer<UInt8>!, UnsafeMutablePointer<UInt8>!) -> Bool](cfattributedstringgetbidilevelsandresolveddirections(_:_:_:_:_:).md)
- [func CFBundleCopyLocalizedStringForLocalizations(CFBundle!, CFString!, CFString!, CFString!, CFArray!) -> CFString!](cfbundlecopylocalizedstringforlocalizations(_:_:_:_:_:).md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleIsArchitectureLoadable(cpu_type_t) -> Bool](cfbundleisarchitectureloadable(_:).md)
- [func CFBundleIsExecutableLoadable(CFBundle!) -> Bool](cfbundleisexecutableloadable(_:).md)
- [func CFBundleIsExecutableLoadableForURL(CFURL!) -> Bool](cfbundleisexecutableloadableforurl(_:).md)
- [func CFCopyHomeDirectoryURL() -> CFURL!](cfcopyhomedirectoryurl().md)
- [func CFDateFormatterCreateISO8601Formatter(CFAllocator!, CFISO8601DateFormatOptions) -> CFDateFormatter!](cfdateformattercreateiso8601formatter(_:_:).md)
- [func CFFileSecurityClearProperties(CFFileSecurity!, CFFileSecurityClearOptions) -> Bool](cffilesecurityclearproperties(_:_:).md)
  Clears properties from a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t?>!) -> Bool](cffilesecuritycopyaccesscontrollist(_:_:).md)
  Copies the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopygroupuuid(_:_:).md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopyowneruuid(_:_:).md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!](cffilesecuritycreate(_:).md)
  Creates a `CFFileSecurityRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorreallocatetyped(_:_:_:_:_:))*