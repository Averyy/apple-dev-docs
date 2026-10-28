# CFURLCopyAbsoluteURL(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new `CFURL` object by resolving the relative portion of a URL against its base.

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
func CFURLCopyAbsoluteURL(_ relativeURL: CFURL!) -> CFURL!
```

```c
extern CFURLRefCFURLCopyAbsoluteURL(CFURLRef relativeURL);
```

## Return Value

A new `CFURL` object, or `NULL` if `relativeURL` cannot be made absolute. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `relativeURL`: The `CFURL` object to resolve.

## See Also

### Creating a CFURL
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcopyabsoluteurl(_:))*