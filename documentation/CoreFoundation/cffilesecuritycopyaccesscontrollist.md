# CFFileSecurityCopyAccessControlList(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Copies the access control list associated with a `CFFileSecurityRef` object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFFileSecurityCopyAccessControlList(_ fileSec: CFFileSecurity!, _ accessControlList: UnsafeMutablePointer<acl_t?>!) -> Bool
```

#### Return Value

Returns `true` if the ACL was successfully copied, or `false` if there is no ACL property associated with the `CFFileSecurityRef` object.

#### Discussion

You can manipulate the `acl_t` object using the acl calls defined in `<sys/acl.h>`. For more information, see the acl manual page.

## Parameters

- `fileSec`: The   object.
- `accessControlList`: A pointer to an acl_t object. The resulting ACL can be freed by calling acl_free(3) macOS Manual Page.

## See Also

- [func CFAllocatorAllocateBytes(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocatebytes(_:_:_:).md)
- [func CFAllocatorAllocateTyped(CFAllocator!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocatetyped(_:_:_:_:).md)
- [func CFAllocatorReallocateBytes(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocatebytes(_:_:_:_:).md)
- [func CFAllocatorReallocateTyped(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocatetyped(_:_:_:_:_:).md)
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
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopygroupuuid(_:_:).md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopyowneruuid(_:_:).md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!](cffilesecuritycreate(_:).md)
  Creates a `CFFileSecurityRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecuritycopyaccesscontrollist(_:_:))*