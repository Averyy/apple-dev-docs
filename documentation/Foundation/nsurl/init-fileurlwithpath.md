# init(fileURLWithPath:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly created NSURL referencing the local file or directory at `path`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(fileURLWithPath path: String)
```

## Mentions

- [Improving performance and stability when accessing the file system](improving-performance-and-stability-when-accessing-the-file-system.md)

#### Return Value

An NSURL object initialized with `path`.

#### Discussion

Invoking this method is equivalent to invoking [`init(scheme:host:path:)`](nsurl/init(scheme:host:path:).md) with scheme [`NSURLFileScheme`](nsurlfilescheme.md), a `nil` host, and `path`.

This method assumes that `path` is a directory if it ends with a slash. If `path` does not end with a slash, the method examines the file system to determine if `path` is a file or a directory. If `path` exists in the file system and is a directory, the method appends a trailing slash. If `path` does not exist in the file system, the method assumes that it represents a file and does not append a trailing slash.

As an alternative, consider using [`init(fileURLWithPath:isDirectory:)`](nsurl/init(fileurlwithpath:isdirectory:).md), which allows you to explicitly specify whether the returned `NSURL` object represents a file or directory.

## Parameters

- `path`: The path that the NSURL object will represent.   should be a valid system path, and must not be an empty path. If   begins with a tilde, it must first be expanded with  . If   is a relative path, it is treated as being relative to the current working directory.

## See Also

- [convenience init?(string: String)](nsurl/init(string:).md)
  Initializes an NSURL object with a provided URL string.
- [convenience init?(string: String, encodingInvalidCharacters: Bool)](nsurl/init(string:encodinginvalidcharacters:).md)
  Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init?(string: String, relativeTo: URL?)](nsurl/init(string:relativeto:).md)
  Initializes an NSURL object with a base URL and a relative string.
- [class func fileURL(withPath: String, isDirectory: Bool) -> URL](nsurl/fileurl(withpath:isdirectory:).md)
  Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [init(fileURLWithPath: String, isDirectory: Bool)](nsurl/init(fileurlwithpath:isdirectory:).md)
  Initializes a newly created NSURL referencing the local file or directory at `path`.
- [class func fileURL(withPath: String, relativeTo: URL?) -> URL](nsurl/fileurl(withpath:relativeto:).md)
- [init(fileURLWithPath: String, relativeTo: URL?)](nsurl/init(fileurlwithpath:relativeto:).md)
- [class func fileURL(withPath: String, isDirectory: Bool, relativeTo: URL?) -> URL](nsurl/fileurl(withpath:isdirectory:relativeto:).md)
- [init(fileURLWithPath: String, isDirectory: Bool, relativeTo: URL?)](nsurl/init(fileurlwithpath:isdirectory:relativeto:).md)
- [class func fileURL(withPath: String) -> URL](nsurl/fileurl(withpath:).md)
  Initializes and returns a newly created NSURL object as a file URL with a specified path.
- [class func fileURL(withPathComponents: [String]) -> URL?](nsurl/fileurl(withpathcomponents:).md)
  Initializes and returns a newly created NSURL object as a file URL with specified path components.
- [convenience init(resolvingAliasFileAt: URL, options: NSURL.BookmarkResolutionOptions) throws](nsurl/init(resolvingaliasfileat:options:).md)
  Returns a new URL made by resolving the alias file at `url`.
- [convenience init(resolvingBookmarkData: Data, options: NSURL.BookmarkResolutionOptions, relativeTo: URL?, bookmarkDataIsStale: UnsafeMutablePointer<ObjCBool>?) throws](nsurl/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:).md)
  Initializes a newly created NSURL that points to a location specified by resolving bookmark data.
- [class func fileURL(withFileSystemRepresentation: UnsafePointer<CChar>, isDirectory: Bool, relativeTo: URL?) -> URL](nsurl/fileurl(withfilesystemrepresentation:isdirectory:relativeto:).md)
  Returns a new URL object initialized with a C string representing a local file system path.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](nsurl/getfilesystemrepresentation(_:maxlength:).md)
  Fills the provided buffer with a C string representing a local file system path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(fileurlwithpath:))*