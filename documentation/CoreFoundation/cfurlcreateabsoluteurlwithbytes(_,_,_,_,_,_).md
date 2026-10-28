# CFURLCreateAbsoluteURLWithBytes(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Bool) -> CFURL!
```

```c
extern CFURLRefCFURLCreateAbsoluteURLWithBytes(CFAllocatorRef alloc, const UInt8 *relativeURLBytes, CFIndex length, CFStringEncoding encoding, CFURLRef baseURL, Boolean useCompatibilityMode);
```

## Return Value

A new `CFURL` object, or `NULL` if `relativeURLBytes` cannot be made absolute. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function interprets the provided bytes using the specified string encoding to create the relative portion of the URL’s address.

> **Note**:  This function does not support string encoding which isn’t a superset of ASCII encoding. Both [`CFURLGetBytes(_:_:_:)`](./cfurlgetbytes%28_,_,_%29.md) and [`CFURLGetByteRangeForComponent(_:_:_:)`](./cfurlgetbyterangeforcomponent%28_,_,_%29.md) require 7-bit ASCII characters to be stored in a single 8-bit byte. The following [`CFStringEncodings`](./cfstringencodings.md) can be used: [`CFStringBuiltInEncodings.macRoman`](./cfstringbuiltinencodings/macroman.md), [`CFStringBuiltInEncodings.windowsLatin1`](./cfstringbuiltinencodings/windowslatin1.md), [`CFStringBuiltInEncodings.isoLatin1`](./cfstringbuiltinencodings/isolatin1.md), [`CFStringBuiltInEncodings.nextStepLatin`](./cfstringbuiltinencodings/nextsteplatin.md), [`CFStringBuiltInEncodings.ASCII`](./cfstringbuiltinencodings/ascii.md) and [`CFStringBuiltInEncodings.UTF8`](./cfstringbuiltinencodings/utf8.md).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `relativeURLBytes`: The character bytes that represent a relative URL to convert into a `CFURL` object.
- `length`: The number of bytes in `relativeURLBytes`.
- `encoding`: The string encoding of the `relativeURLBytes` string. This encoding is also used to interpret percent escape sequences.
- `baseURL`: The URL to which `relativeURLBytes` is relative.
- `useCompatibilityMode`: If `true`, the rules historically used on the web are used to resolve the string specified by the `relativeURLBytes` parameter against `baseURL`. These rules are generally listed in the RFC as optional or alternate interpretations. Otherwise, the strict rules from the RFC are used.

## See Also

### Creating a CFURL
- [func CFURLCopyAbsoluteURL(CFURL!) -> CFURL!](./cfurlcopyabsoluteurl%28_%29.md)
  Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [func CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](./cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md)
  Returns a new URL made by resolving bookmark data.
- [func CFURLCreateCopyAppendingPathComponent(CFAllocator!, CFURL!, CFString!, Bool) -> CFURL!](./cfurlcreatecopyappendingpathcomponent%28_,_,_,_%29.md)
  Creates a copy of a given URL and appends a path component.
- [func CFURLCreateCopyAppendingPathExtension(CFAllocator!, CFURL!, CFString!) -> CFURL!](./cfurlcreatecopyappendingpathextension%28_,_,_%29.md)
  Creates a copy of a given URL and appends a path extension.
- [func CFURLCreateCopyDeletingLastPathComponent(CFAllocator!, CFURL!) -> CFURL!](./cfurlcreatecopydeletinglastpathcomponent%28_,_%29.md)
  Creates a copy of a given URL with the last path component deleted.
- [func CFURLCreateCopyDeletingPathExtension(CFAllocator!, CFURL!) -> CFURL!](./cfurlcreatecopydeletingpathextension%28_,_%29.md)
  Creates a copy of a given URL with its last path extension removed.
- [func CFURLCreateFilePathURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](./cfurlcreatefilepathurl%28_,_,_%29.md)
  Returns a new file path URL that refers to the same resource as a specified URL.
- [func CFURLCreateFileReferenceURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](./cfurlcreatefilereferenceurl%28_,_,_%29.md)
  Returns a new file reference URL that points to the same resource as a specified URL.
- [func CFURLCreateFromFileSystemRepresentation(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, Bool) -> CFURL!](./cfurlcreatefromfilesystemrepresentation%28_,_,_,_%29.md)
  Creates a new `CFURL` object for a file system entity using the native representation.
- [func CFURLCreateFromFileSystemRepresentationRelativeToBase(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, Bool, CFURL!) -> CFURL!](./cfurlcreatefromfilesystemrepresentationrelativetobase%28_,_,_,_,_%29.md)
  Creates a `CFURL` object from a native character string path relative to a base URL.
- [func CFURLCreateFromFSRef(CFAllocator!, OpaquePointer!) -> CFURL!](./cfurlcreatefromfsref%28_,_%29.md)
  Creates a URL from a given directory or file.
- [func CFURLCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!) -> CFURL!](./cfurlcreatewithbytes%28_,_,_,_,_%29.md)
  Creates a `CFURL` object using a given character bytes.
- [func CFURLCreateWithFileSystemPath(CFAllocator!, CFString!, CFURLPathStyle, Bool) -> CFURL!](./cfurlcreatewithfilesystempath%28_,_,_,_%29.md)
  Creates a `CFURL` object using a local file system path string.
- [func CFURLCreateWithFileSystemPathRelativeToBase(CFAllocator!, CFString!, CFURLPathStyle, Bool, CFURL!) -> CFURL!](./cfurlcreatewithfilesystempathrelativetobase%28_,_,_,_,_%29.md)
  Creates a `CFURL` object using a local file system path string relative to a base URL.
- [func CFURLCreateWithString(CFAllocator!, CFString!, CFURL!) -> CFURL!](./cfurlcreatewithstring%28_,_,_%29.md)
  Creates a `CFURL` object using a given `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreateabsoluteurlwithbytes(_:_:_:_:_:_:))*