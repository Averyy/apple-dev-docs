# CFURLCreateCopyAppendingPathComponent(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a copy of a given URL and appends a path component.

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
func CFURLCreateCopyAppendingPathComponent(_ allocator: CFAllocator!, _ url: CFURL!, _ pathComponent: CFString!, _ isDirectory: Bool) -> CFURL!
```

```c
extern CFURLRefCFURLCreateCopyAppendingPathComponent(CFAllocatorRef allocator, CFURLRef url, CFStringRef pathComponent, Boolean isDirectory);
```

## Return Value

A copy of `url` appended with `pathComponent`. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The `isDirectory` argument specifies whether or not the new path component points to a file or a to directory. Note that the URL syntax for a directory and for a file at otherwise the same location are slightly different—directory URLs must end in “/”. If you have the URL `http://www.apple.com/foo/` and you append the path component `bar`, then if `isDirectory` is [`true`](../Swift/true.md) then the resulting URL is `http://www.apple.com/foo/bar/`, whereas if `isDirectory` is [`false`](../Swift/false.md) then the resulting URL is `http://www.apple.com/foo/bar`. This difference is particularly important if you resolve another URL against this new URL. `file.html` relative to `http://www.apple.com/foo/bar` is `http://www.apple.com/foo/file.html`, whereas `file.html` relative to `http://www.apple.com/foo/bar/` is `http://www.apple.com/foo/bar/file.html`.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `url`: The `CFURL` object to which to append a path component.
- `pathComponent`: The path component to append to `url`.
- `isDirectory`: A Boolean value that specifies whether the string is treated as a directory path when resolving against relative path components. Pass `true` if the new component indicates a directory, `false` otherwise.

## See Also

### Creating a CFURL
- [func CFURLCopyAbsoluteURL(CFURL!) -> CFURL!](./cfurlcopyabsoluteurl%28_%29.md)
  Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [func CFURLCreateAbsoluteURLWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, CFURL!, Bool) -> CFURL!](./cfurlcreateabsoluteurlwithbytes%28_,_,_,_,_,_%29.md)
  Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [func CFURLCreateByResolvingBookmarkData(CFAllocator!, CFData!, CFURLBookmarkResolutionOptions, CFURL!, CFArray!, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!](./cfurlcreatebyresolvingbookmarkdata%28_,_,_,_,_,_,_%29.md)
  Returns a new URL made by resolving bookmark data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatecopyappendingpathcomponent(_:_:_:_:))*