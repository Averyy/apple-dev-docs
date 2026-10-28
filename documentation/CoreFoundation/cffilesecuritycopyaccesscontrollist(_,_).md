# CFFileSecurityCopyAccessControlList(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CFFileSecurityCopyAccessControlList(CFFileSecurityRef fileSec, acl_t*accessControlList);
```

## Return Value

Returns `true` if the ACL was successfully copied, or `false` if there is no ACL property associated with the `CFFileSecurityRef` object.

## Discussion

You can manipulate the `acl_t` object using the acl calls defined in `<sys/acl.h>`. For more information, see the acl manual page.

## Parameters

- `fileSec`: The `CFFileSecurityRef` object.
- `accessControlList`: A pointer to an acl_t object. The resulting ACL can be freed by calling acl_free(3) macOS Manual Page.

## See Also

### Functions
- [func CFAllocatorAllocateBytes(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorallocatebytes%28_,_,_%29.md)
- [func CFAllocatorAllocateTyped(CFAllocator!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorallocatetyped%28_,_,_,_%29.md)
- [func CFAllocatorReallocateBytes(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorreallocatebytes%28_,_,_,_%29.md)
- [func CFAllocatorReallocateTyped(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFAllocatorTypeID, CFOptionFlags) -> UnsafeMutableRawPointer!](./cfallocatorreallocatetyped%28_,_,_,_,_%29.md)
- [func CFAttributedStringGetBidiLevelsAndResolvedDirections(CFAttributedString!, CFRange, Int8, UnsafeMutablePointer<UInt8>!, UnsafeMutablePointer<UInt8>!) -> Bool](./cfattributedstringgetbidilevelsandresolveddirections%28_,_,_,_,_%29.md)
- [func CFBundleCopyLocalizedStringForLocalizations(CFBundle!, CFString!, CFString!, CFString!, CFArray!) -> CFString!](./cfbundlecopylocalizedstringforlocalizations%28_,_,_,_,_%29.md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleIsArchitectureLoadable(cpu_type_t) -> Bool](./cfbundleisarchitectureloadable%28_%29.md)
- [func CFBundleIsExecutableLoadable(CFBundle!) -> Bool](./cfbundleisexecutableloadable%28_%29.md)
- [func CFBundleIsExecutableLoadableForURL(CFURL!) -> Bool](./cfbundleisexecutableloadableforurl%28_%29.md)
- [func CFCopyHomeDirectoryURL() -> CFURL!](./cfcopyhomedirectoryurl%28%29.md)
- [func CFDateFormatterCreateISO8601Formatter(CFAllocator!, CFISO8601DateFormatOptions) -> CFDateFormatter!](./cfdateformattercreateiso8601formatter%28_,_%29.md)
- [func CFFileSecurityClearProperties(CFFileSecurity!, CFFileSecurityClearOptions) -> Bool](./cffilesecurityclearproperties%28_,_%29.md)
  Clears properties from a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](./cffilesecuritycopygroupuuid%28_,_%29.md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](./cffilesecuritycopyowneruuid%28_,_%29.md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!](./cffilesecuritycreate%28_%29.md)
  Creates a `CFFileSecurityRef` object.
- [CFAutorelease](./cfautorelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecuritycopyaccesscontrollist(_:_:))*