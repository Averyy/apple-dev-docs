# Core Foundation Functions

**Framework**: Core Foundation  
**Role**: API Collection

## Topics

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
- [func CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t?>!) -> Bool](./cffilesecuritycopyaccesscontrollist%28_,_%29.md)
  Copies the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](./cffilesecuritycopygroupuuid%28_,_%29.md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](./cffilesecuritycopyowneruuid%28_,_%29.md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCreate(CFAllocator!) -> CFFileSecurity!](./cffilesecuritycreate%28_%29.md)
  Creates a `CFFileSecurityRef` object.
- [func CFFileSecurityCreateCopy(CFAllocator!, CFFileSecurity!) -> CFFileSecurity!](./cffilesecuritycreatecopy%28_,_%29.md)
  Creates a copy of a `CFFileSecurityRef` object.
- [func CFFileSecurityGetGroup(CFFileSecurity!, UnsafeMutablePointer<gid_t>!) -> Bool](./cffilesecuritygetgroup%28_,_%29.md)
  Gets the group ID associated with a `CFFileSecurityRef` object
- [func CFFileSecurityGetMode(CFFileSecurity!, UnsafeMutablePointer<mode_t>!) -> Bool](./cffilesecuritygetmode%28_,_%29.md)
  Gets the file mode associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityGetOwner(CFFileSecurity!, UnsafeMutablePointer<uid_t>!) -> Bool](./cffilesecuritygetowner%28_,_%29.md)
  Gets the owner ID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityGetTypeID() -> CFTypeID](./cffilesecuritygettypeid%28%29.md)
  Returns the type identifier for the `CFFileSecurityRef` opaque type.
- [func CFFileSecuritySetAccessControlList(CFFileSecurity!, acl_t!) -> Bool](./cffilesecuritysetaccesscontrollist%28_,_%29.md)
  Sets the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetGroup(CFFileSecurity!, gid_t) -> Bool](./cffilesecuritysetgroup%28_,_%29.md)
  Sets the group ID associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetGroupUUID(CFFileSecurity!, CFUUID!) -> Bool](./cffilesecuritysetgroupuuid%28_,_%29.md)
  Sets the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetMode(CFFileSecurity!, mode_t) -> Bool](./cffilesecuritysetmode%28_,_%29.md)
  Sets the file mode associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetOwner(CFFileSecurity!, uid_t) -> Bool](./cffilesecuritysetowner%28_,_%29.md)
  Sets the owner ID associated with a `CFFileSecurityRef` object.
- [func CFFileSecuritySetOwnerUUID(CFFileSecurity!, CFUUID!) -> Bool](./cffilesecuritysetowneruuid%28_,_%29.md)
  Sets the owner UUID associated with a `CFFileSecurityRef` object.
- [func CFReadStreamCopyDispatchQueue(CFReadStream!) -> dispatch_queue_t!](./cfreadstreamcopydispatchqueue%28_%29.md)
- [func CFReadStreamSetDispatchQueue(CFReadStream!, dispatch_queue_t!)](./cfreadstreamsetdispatchqueue%28_,_%29.md)
- [func CFRunLoopTimerGetTolerance(CFRunLoopTimer!) -> CFTimeInterval](./cfrunlooptimergettolerance%28_%29.md)
- [func CFRunLoopTimerSetTolerance(CFRunLoopTimer!, CFTimeInterval)](./cfrunlooptimersettolerance%28_,_%29.md)
- [func CFURLEnumeratorCreateForDirectoryURL(CFAllocator!, CFURL!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!](./cfurlenumeratorcreatefordirectoryurl%28_,_,_,_%29.md)
  Creates and returns a directory enumerator with provided enumerator behavior options and properties to be prefetched.
- [func CFURLEnumeratorCreateForMountedVolumes(CFAllocator!, CFURLEnumeratorOptions, CFArray!) -> CFURLEnumerator!](./cfurlenumeratorcreateformountedvolumes%28_,_,_%29.md)
  Creates and returns a volume enumerator with provided enumerator behavior options and properties to be prefetched.
- [func CFURLEnumeratorGetDescendentLevel(CFURLEnumerator!) -> CFIndex](./cfurlenumeratorgetdescendentlevel%28_%29.md)
  Returns the number of levels a recursive directory enumerator has descended.
- [func CFURLEnumeratorGetNextURL(CFURLEnumerator!, UnsafeMutablePointer<Unmanaged<CFURL>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFURLEnumeratorResult](./cfurlenumeratorgetnexturl%28_,_,_%29.md)
  Advances an enumerator to the next URL.
- [func CFURLEnumeratorGetSourceDidChange(CFURLEnumerator!) -> Bool](./cfurlenumeratorgetsourcedidchange%28_%29.md)
  This function is unimplemented, so it performs no operation.
- [func CFURLEnumeratorGetTypeID() -> CFTypeID](./cfurlenumeratorgettypeid%28%29.md)
  Returns the opaque type identifier for the CFURLEnumerator opaque type.
- [func CFURLEnumeratorSkipDescendents(CFURLEnumerator!)](./cfurlenumeratorskipdescendents%28_%29.md)
  Tells a recursive enumerator not to descend into the directory at the URL that was returned by the most recent call to the [`CFURLEnumeratorGetNextURL(_:_:_:)`](./cfurlenumeratorgetnexturl%28_,_,_%29.md) function.
- [func CFURLIsFileReferenceURL(CFURL!) -> Bool](./cfurlisfilereferenceurl%28_%29.md)
- [func CFWriteStreamCopyDispatchQueue(CFWriteStream!) -> dispatch_queue_t!](./cfwritestreamcopydispatchqueue%28_%29.md)
- [func CFWriteStreamSetDispatchQueue(CFWriteStream!, dispatch_queue_t!)](./cfwritestreamsetdispatchqueue%28_,_%29.md)
- [CFAutorelease](./cfautorelease.md)
- [CFStringCreateStringWithValidatedFormat](./cfstringcreatestringwithvalidatedformat.md)
- [CFStringCreateStringWithValidatedFormatAndArguments](./cfstringcreatestringwithvalidatedformatandarguments.md)

## See Also

### Reference
- [CFStream](./cfstream.md)
- [Core Foundation Structures](./core-foundation-structures.md)
- [Core Foundation Enumerations](./core-foundation-enumerations.md)
- [Core Foundation Constants](./core-foundation-constants.md)
- [Core Foundation Data Types](./core-foundation-data-types.md)
- [Core Foundation Macros](./corefoundation-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/core-foundation-functions)*