# CFURLCreateFilePathURL(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a new file path URL that refers to the same resource as a specified URL.

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
func CFURLCreateFilePathURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!
```

```c
extern CFURLRefCFURLCreateFilePathURL(CFAllocatorRef allocator, CFURLRef url, CFErrorRef*error);
```

## Return Value

The new file path URL, or `NULL` if an error occurs

## Discussion

If the original URL is a file reference URL, this function returns a copy of the URL converted to a file path URL. If the original URL is a file path URL, this function returns the original URL. If the original URL is not a file URL, or if the resource is not reachable or no longer exists, this function returns `nil`.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `url`: The URL.
- `error`: The error that occurred if the URL could not be created.

## See Also

### Creating a CFURL
- [func CFURLCopyAbsoluteURL(CFURL!) -> CFURL!](./cfurlcopyabsoluteurl%28_%29.md)
  Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [func CFURLCreateAbsoluteURLWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!, Bool) -> CFURL!](./cfurlcreateabsoluteurlwithbytes%28_,_,_,_,_,_%29.md)
  Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatefilepathurl(_:_:_:))*