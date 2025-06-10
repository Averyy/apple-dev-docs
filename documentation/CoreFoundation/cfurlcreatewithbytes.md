# CFURLCreateWithBytes(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a `CFURL` object using a given character bytes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFURLCreateWithBytes(_ allocator: CFAllocator!, _ URLBytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!) -> CFURL!
```

#### Return Value

A new `CFURL` object. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The specified string encoding will be used both to interpret `URLBytes`, and to interpret any percent-escapes within the string.

> **Note**:  This function does not support string encoding which isn’t a superset of ASCII encoding. Both [`CFURLGetBytes(_:_:_:)`](cfurlgetbytes(_:_:_:).md) and [`CFURLGetByteRangeForComponent(_:_:_:)`](cfurlgetbyterangeforcomponent(_:_:_:).md) require 7-bit ASCII characters to be stored in a single 8-bit byte. The following [`CFStringEncodings`](cfstringencodings.md) can be used: [`CFStringBuiltInEncodings.macRoman`](cfstringbuiltinencodings/macroman.md), [`CFStringBuiltInEncodings.windowsLatin1`](cfstringbuiltinencodings/windowslatin1.md), [`CFStringBuiltInEncodings.isoLatin1`](cfstringbuiltinencodings/isolatin1.md), [`CFStringBuiltInEncodings.nextStepLatin`](cfstringbuiltinencodings/nextsteplatin.md), [`CFStringBuiltInEncodings.ASCII`](cfstringbuiltinencodings/ascii.md) and [`CFStringBuiltInEncodings.UTF8`](cfstringbuiltinencodings/utf8.md).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `URLBytes`: The character bytes to convert into a   object.
- `length`: The number of bytes in  .
- `encoding`: The string encoding of the   string. This encoding is also used to interpret percent escape sequences.
- `baseURL`: The URL to which   is relative. Pass   if   contains an absolute URL or if you want to create a relative URL. If   contains an absolute URL, this parameter is ignored.

## See Also

- [func CFURLCopyAbsoluteURL(CFURL!) -> CFURL!](cfurlcopyabsoluteurl(_:).md)
  Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [func CFURLCreateAbsoluteURLWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!, Bool) -> CFURL!](cfurlcreateabsoluteurlwithbytes(_:_:_:_:_:_:).md)
  Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [func CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatebyresolvingbookmarkdata(_:_:_:_:_:_:_:).md)
  Returns a new URL made by resolving bookmark data.
- [func CFURLCreateCopyAppendingPathComponent(CFAllocator!, CFURL!, CFString!, Bool) -> CFURL!](cfurlcreatecopyappendingpathcomponent(_:_:_:_:).md)
  Creates a copy of a given URL and appends a path component.
- [func CFURLCreateCopyAppendingPathExtension(CFAllocator!, CFURL!, CFString!) -> CFURL!](cfurlcreatecopyappendingpathextension(_:_:_:).md)
  Creates a copy of a given URL and appends a path extension.
- [func CFURLCreateCopyDeletingLastPathComponent(CFAllocator!, CFURL!) -> CFURL!](cfurlcreatecopydeletinglastpathcomponent(_:_:).md)
  Creates a copy of a given URL with the last path component deleted.
- [func CFURLCreateCopyDeletingPathExtension(CFAllocator!, CFURL!) -> CFURL!](cfurlcreatecopydeletingpathextension(_:_:).md)
  Creates a copy of a given URL with its last path extension removed.
- [func CFURLCreateFilePathURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatefilepathurl(_:_:_:).md)
  Returns a new file path URL that refers to the same resource as a specified URL.
- [func CFURLCreateFileReferenceURL(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](cfurlcreatefilereferenceurl(_:_:_:).md)
  Returns a new file reference URL that points to the same resource as a specified URL.
- [func CFURLCreateFromFileSystemRepresentation(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, Bool) -> CFURL!](cfurlcreatefromfilesystemrepresentation(_:_:_:_:).md)
  Creates a new `CFURL` object for a file system entity using the native representation.
- [func CFURLCreateFromFileSystemRepresentationRelativeToBase(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, Bool, CFURL!) -> CFURL!](cfurlcreatefromfilesystemrepresentationrelativetobase(_:_:_:_:_:).md)
  Creates a `CFURL` object from a native character string path relative to a base URL.
- [func CFURLCreateFromFSRef(CFAllocator!, OpaquePointer!) -> CFURL!](cfurlcreatefromfsref(_:_:).md)
  Creates a URL from a given directory or file.
- [func CFURLCreateWithFileSystemPath(CFAllocator!, CFString!, CFURLPathStyle, Bool) -> CFURL!](cfurlcreatewithfilesystempath(_:_:_:_:).md)
  Creates a `CFURL` object using a local file system path string.
- [func CFURLCreateWithFileSystemPathRelativeToBase(CFAllocator!, CFString!, CFURLPathStyle, Bool, CFURL!) -> CFURL!](cfurlcreatewithfilesystempathrelativetobase(_:_:_:_:_:).md)
  Creates a `CFURL` object using a local file system path string relative to a base URL.
- [func CFURLCreateWithString(CFAllocator!, CFString!, CFURL!) -> CFURL!](cfurlcreatewithstring(_:_:_:).md)
  Creates a `CFURL` object using a given `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatewithbytes(_:_:_:_:_:))*