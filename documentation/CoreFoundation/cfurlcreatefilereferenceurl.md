# CFURLCreateFileReferenceURL(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a new file reference URL that points to the same resource as a specified URL.

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
func CFURLCreateFileReferenceURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!
```

#### Return Value

The new file reference URL, or `NULL` if an error occurs.

#### Discussion

File reference URLs use a URL path syntax that identifies a file system object by reference, not by path. This form of file URL remains valid when the file system path of the URL’s underlying resource changes.

If the original URL is a file path URL, this function returns a copy of the URL converted into a file reference URL. If the original URL is a file reference URL, this function returns the original. If the original URL is not a file URL, this function returns `nil`.

File reference URLs cannot be created to file system objects which do not exist or are not reachable. This function returns `nil` instead.

In some areas of the file system hierarchy, file reference URLs cannot be generated to the leaf node of the URL path.

> ❗ **Important**:  A file reference URL’s path should never be persistently stored, because it is not valid across system restarts or remounts of volumes. If you need to store a persistent reference to a file system object, use a bookmark instead. You can create a bookmark by calling [`CFURLCreateBookmarkData(_:_:_:_:_:_:)`](cfurlcreatebookmarkdata(_:_:_:_:_:_:).md).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `url`: The URL.
- `error`: The error that occurred if the URL could not be created.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatefilereferenceurl(_:_:_:))*