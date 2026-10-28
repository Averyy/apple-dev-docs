# fileURL(withFileSystemRepresentation:isDirectory:relativeTo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a new URL object initialized with a C string representing a local file system path.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func fileURL(withFileSystemRepresentation path: UnsafePointer<CChar>, isDirectory isDir: Bool, relativeTo baseURL: URL?) -> URL
```

```objc
+ (NSURL *) fileURLWithFileSystemRepresentation:(const char *) path isDirectory:(BOOL) isDir relativeToURL:(NSURL *) baseURL;
```

## Return Value

Returns the new object.

## Discussion

The file system representation format is described in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

## Parameters

- `path`: A null-terminated C string in file system representation containing the path to represent as a URL. If this path is a relative path, it is treated as being relative to the current working directory.
- `isDir`: [`true`](../../Swift/true.md) if the last path part is a directory, otherwise [`false`](../../Swift/false.md).
- `baseURL`: The base URL for the new URL object. This must be a file URL. If `path` is absolute, this URL is ignored.

## See Also

### Creating a URL object
- [convenience init?(string: String)](./init%28string%29.md)
  Initializes an NSURL object with a provided URL string.
- [convenience init?(string: String, encodingInvalidCharacters: Bool)](./init%28string,encodinginvalidcharacters%29.md)
  Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(string: String, relativeTo: URL?)](./init%28string,relativeto%29.md)
  Initializes an NSURL object with a base URL and a relative string.
- [class func fileURL(withPath: String, isDirectory: Bool) -> URL](./fileurl%28withpath,isdirectory%29.md)
  Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [init(fileURLWithPath: String, isDirectory: Bool)](./init%28fileurlwithpath,isdirectory%29.md)
  Initializes a newly created NSURL referencing the local file or directory at `path`.
- [class func fileURL(withPath: String, relativeTo: URL?) -> URL](./fileurl%28withpath,relativeto%29.md)
  Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [init(fileURLWithPath: String, relativeTo: URL?)](./init%28fileurlwithpath,relativeto%29.md)
  Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [class func fileURL(withPath: String, isDirectory: Bool, relativeTo: URL?) -> URL](./fileurl%28withpath,isdirectory,relativeto%29.md)
  Initializes and returns a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [init(fileURLWithPath: String, isDirectory: Bool, relativeTo: URL?)](./init%28fileurlwithpath,isdirectory,relativeto%29.md)
  Initializes a newly created file NSURL referencing the local file or directory at path, relative to a base URL.
- [class func fileURL(withPath: String) -> URL](./fileurl%28withpath%29.md)
  Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [init(fileURLWithPath: String)](./init%28fileurlwithpath%29.md)
  Initializes a newly created NSURL referencing the local file or directory at `path`.
- [class func fileURL(withPathComponents: [String]) -> URL?](./fileurl%28withpathcomponents%29.md)
  Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [convenience init(resolvingAliasFileAt: URL, options: NSURL.BookmarkResolutionOptions) throws](./init%28resolvingaliasfileat,options%29.md)
  Returns a new URL made by resolving the alias file at `url`.
- [convenience init(resolvingBookmarkData: Data, options: NSURL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>?) throws](./init%28resolvingbookmarkdata,options,relativeto,bookmarkdataisstale%29.md)
  Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](./getfilesystemrepresentation%28_,maxlength%29.md)
  Fills the provided buffer with a C string representing a local file system path.
- [+ URLWithString:](./urlwithstring_.md)
  Creates and returns an NSURL object initialized with a provided URL string.
- [+ URLWithString:encodingInvalidCharacters:](./urlwithstring_encodinginvalidcharacters_.md)
  Creates and returns an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [+ URLWithString:relativeToURL:](./urlwithstring_relativetourl_.md)
  Creates and returns an NSURL object initialized with a base URL and a relative string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/fileurl(withfilesystemrepresentation:isdirectory:relativeto:))*