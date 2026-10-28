# CFFileSecurityClearProperties(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Clears properties from a `CFFileSecurityRef` object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFFileSecurityClearProperties(_ fileSec: CFFileSecurity!, _ clearPropertyMask: CFFileSecurityClearOptions) -> Bool
```

```c
extern Boolean CFFileSecurityClearProperties(CFFileSecurityRef fileSec, CFFileSecurityClearOptions clearPropertyMask);
```

## Return Value

Returns `true` if the file security properties were successfully cleared, or `false` otherwise.

## Discussion

One common use for `CFFileSecurityRef` objects is to clone the permissions from one file to another. In this use, you may want to copy only a subset of the permissions. This function lets you delete the specific permissions that you do not want to change prior to applying the set of permissions to a different file.

## Parameters

- `fileSec`: The file security properties to clear.
- `clearPropertyMask`: The file security properties to clear.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearproperties(_:_:))*