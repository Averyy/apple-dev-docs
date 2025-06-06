# CFURLCreateCopyDeletingLastPathComponent(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a copy of a given URL with the last path component deleted.

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
func CFURLCreateCopyDeletingLastPathComponent(_ allocator: CFAllocator!, _ url: CFURL!) -> CFURL!
```

#### Return Value

A copy of `url` with the last path component deleted. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `url`: The   object whose last path component you want to delete.

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
- [func CFURLCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!) -> CFURL!](cfurlcreatewithbytes(_:_:_:_:_:).md)
  Creates a `CFURL` object using a given character bytes.
- [func CFURLCreateWithFileSystemPath(CFAllocator!, CFString!, CFURLPathStyle, Bool) -> CFURL!](cfurlcreatewithfilesystempath(_:_:_:_:).md)
  Creates a `CFURL` object using a local file system path string.
- [func CFURLCreateWithFileSystemPathRelativeToBase(CFAllocator!, CFString!, CFURLPathStyle, Bool, CFURL!) -> CFURL!](cfurlcreatewithfilesystempathrelativetobase(_:_:_:_:_:).md)
  Creates a `CFURL` object using a local file system path string relative to a base URL.
- [func CFURLCreateWithString(CFAllocator!, CFString!, CFURL!) -> CFURL!](cfurlcreatewithstring(_:_:_:).md)
  Creates a `CFURL` object using a given `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatecopydeletinglastpathcomponent(_:_:))*