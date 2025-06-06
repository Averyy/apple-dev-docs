# Core Foundation Functions

**Framework**: Core Foundation

## Topics

### Functions
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
- [func CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t?>!) -> Bool](cffilesecuritycopyaccesscontrollist(_:_:).md)
  Copies the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopygroupuuid(_:_:).md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopyowneruuid(_:_:).md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!](cffilesecuritycreate(_:).md)
  Creates a `CFFileSecurityRef` object.
- [func CFFileSecurityCreateCopy(CFAllocator!, CFFileSecurity!) -> CFFileSecurity!](cffilesecuritycreatecopy(_:_:).md)
  Creates a copy of a `CFFileSecurityRef` object.
- [func CFFileSecurityGetGroup(CFFileSecurity!, UnsafeMutablePointer<gid_t>!) -> Bool](cffilesecuritygetgroup(_:_:).md)
  Gets the group ID associated with a `CFFileSecurityRef` object
- [func CFFileSecurityGetMode(CFFileSecurity!, UnsafeMutablePointer<mode_t>!) -> Bool](cffilesecuritygetmode(_:_:).md)
  Gets the file mode associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityGetOwner(CFFileSecurity!, UnsafeMutablePointer<uid_t>!) -> Bool](cffilesecuritygetowner(_:_:).md)
  Gets the owner ID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityGetTypeID() -> CFTypeID](cffilesecuritygettypeid().md)
  Returns the type identifier for the `CFFileSecurityRef` opaque type.
- [func CFFileSecuritySetAccessControlList(CFFileSecurity!, acl_t!) -> Bool](cffilesecuritysetaccesscontrollist(_:_:).md)
  Sets the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetGroup(CFFileSecurity!, gid_t) -> Bool](cffilesecuritysetgroup(_:_:).md)
  Sets the group ID associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetGroupUUID(CFFileSecurity!, CFUUID!) -> Bool](cffilesecuritysetgroupuuid(_:_:).md)
  Sets the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetMode(CFFileSecurity!, mode_t) -> Bool](cffilesecuritysetmode(_:_:).md)
  Sets the file mode associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetOwner(CFFileSecurity!, uid_t) -> Bool](cffilesecuritysetowner(_:_:).md)
  Sets the owner ID associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetOwnerUUID(CFFileSecurity!, CFUUID!) -> Bool](cffilesecuritysetowneruuid(_:_:).md)
  Sets the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFReadStreamCopyDispatchQueue(CFReadStream!) -> dispatch_queue_t!](cfreadstreamcopydispatchqueue(_:).md)
- [func CFReadStreamSetDispatchQueue(CFReadStream!, dispatch_queue_t!)](cfreadstreamsetdispatchqueue(_:_:).md)
- [func CFRunLoopTimerGetTolerance(CFRunLoopTimer!) -> CFTimeInterval](cfrunlooptimergettolerance(_:).md)
- [func CFRunLoopTimerSetTolerance(CFRunLoopTimer!, CFTimeInterval)](cfrunlooptimersettolerance(_:_:).md)
- [func CFURLEnumeratorCreateForDirectoryURL(CFAllocator!, CFURL!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!](cfurlenumeratorcreatefordirectoryurl(_:_:_:_:).md)
  Creates and returns a directory enumerator with provided enumerator behavior options and properties to be prefetched.
- [func CFURLEnumeratorCreateForMountedVolumes(CFAllocator!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!](cfurlenumeratorcreateformountedvolumes(_:_:_:).md)
  Creates and returns a volume enumerator with provided enumerator behavior options and properties to be prefetched.
- [func CFURLEnumeratorGetDescendentLevel(CFURLEnumerator!) -> CFIndex](cfurlenumeratorgetdescendentlevel(_:).md)
  Returns the number of levels a recursive directory enumerator has descended.
- [func CFURLEnumeratorGetNextURL(CFURLEnumerator!, UnsafeMutablePointer<Unmanaged<CFURL>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFURLEnumeratorResult](cfurlenumeratorgetnexturl(_:_:_:).md)
  Advances an enumerator to the next URL.
- [func CFURLEnumeratorGetSourceDidChange(CFURLEnumerator!) -> Bool](cfurlenumeratorgetsourcedidchange(_:).md)
  This function is unimplemented, so it performs no operation.
- [func CFURLEnumeratorGetTypeID() -> CFTypeID](cfurlenumeratorgettypeid().md)
  Returns the opaque type identifier for the CFURLEnumerator opaque type.
- [func CFURLEnumeratorSkipDescendents(CFURLEnumerator!)](cfurlenumeratorskipdescendents(_:).md)
  Tells a recursive enumerator not to descend into the directory at the URL that was returned by the most recent call to the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function.
- [func CFURLIsFileReferenceURL(CFURL!) -> Bool](cfurlisfilereferenceurl(_:).md)
- [func CFWriteStreamCopyDispatchQueue(CFWriteStream!) -> dispatch_queue_t!](cfwritestreamcopydispatchqueue(_:).md)
- [func CFWriteStreamSetDispatchQueue(CFWriteStream!, dispatch_queue_t!)](cfwritestreamsetdispatchqueue(_:_:).md)

## See Also

- [CFStream](cfstream.md)
- [Core Foundation Structures](core-foundation-structures.md)
- [Core Foundation Enumerations](core-foundation-enumerations.md)
- [Core Foundation Constants](core-foundation-constants.md)
- [Core Foundation Data Types](core-foundation-data-types.md)
- [Core Foundation Macros](corefoundation-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/core-foundation-functions)*