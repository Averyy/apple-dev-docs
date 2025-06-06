# CFURLEnumeratorSkipDescendents(_:)

**Framework**: Core Foundation  
**Kind**: func

Tells a recursive enumerator not to descend into the directory at the URL that was returned by the most recent call to the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLEnumeratorSkipDescendents(_ enumerator: CFURLEnumerator!)
```

#### Discussion

A call to this function is ignored in the following cases:

- The [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function has never been called with this enumerator.
- The last URL returned by the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function is not a directory.
- The enumerator is not a directory enumerator that was created with the [`descendRecursively`](cfurlenumeratoroptions/descendrecursively.md) option.

## Parameters

- `enumerator`: The enumerator.

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
- [func CFFileSecurityCopyAccessControlList(CFFileSecurity!, UnsafeMutablePointer<acl_t?>!) -> Bool](cffilesecuritycopyaccesscontrollist(_:_:).md)
  Copies the access control list associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyGroupUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopygroupuuid(_:_:).md)
  Copies the group UUID associated with a `CFFileSecurityRef` object.
- [func CFFileSecurityCopyOwnerUUID(CFFileSecurity!, UnsafeMutablePointer<Unmanaged<CFUUID>?>!) -> Bool](cffilesecuritycopyowneruuid(_:_:).md)
  Copies the owner UUID associated with a `CFFileSecurityRef` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorskipdescendents(_:))*