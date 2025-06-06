# CFURLEnumeratorGetNextURL(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Advances an enumerator to the next URL.

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
func CFURLEnumeratorGetNextURL(_ enumerator: CFURLEnumerator!, _ url: UnsafeMutablePointer<Unmanaged<CFURL>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFURLEnumeratorResult
```

#### Return Value

The result of advancing the enumerator.

#### Discussion

If this function returns [`CFURLEnumeratorResult.end`](cfurlenumeratorresult/end.md), the enumeration has finished.

A return value of [`CFURLEnumeratorResult.error`](cfurlenumeratorresult/error.md) does not imply that the enumeration has finished.

If this function returns [`CFURLEnumeratorResult.error`](cfurlenumeratorresult/error.md), the user info dictionary of `error` is populated with the following entries (when possible):

- The [`kCFErrorUnderlyingErrorKey`](kcferrorunderlyingerrorkey.md) entry is populated with the underlying error if the underlying error is not in the [`kCFErrorDomainCocoa`](kcferrordomaincocoa.md) domain.
- The [`NSURLErrorKey`](https://developer.apple.com/documentation/Foundation/NSURLErrorKey) entry is populated with the URL that caused the error, as a [`CFURL`](cfurl.md) object.
- The [`NSFilePathErrorKey`](https://developer.apple.com/documentation/Foundation/NSFilePathErrorKey) entry is populated with the file path that caused the error, as a [`CFString`](cfstring.md) object.

## Parameters

- `enumerator`: The enumerator.
- `url`: Contains the next URL if this function returns  .
- `error`: Contains error information if this function returns  . Error information is retained and must be released. Can be  .

## See Also

- [enum CFURLEnumeratorResult](cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorgetnexturl(_:_:_:))*