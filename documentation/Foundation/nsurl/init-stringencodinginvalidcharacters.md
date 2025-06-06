# init(string:encodingInvalidCharacters:)

**Framework**: Foundation  
**Kind**: init

Creates an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
convenience init?(string URLString: String, encodingInvalidCharacters: Bool)
```

#### Discussion

If `encodingInvalidCharacters` is `true`, this initializer tries to encode the string to create a valid URL. If the URL string is still invalid after encoding, the initializer returns `nil`.

## Parameters

- `URLString`: A URL location.
- `encodingInvalidCharacters`: A Boolean value that indicates whether the initializer attempts to encode any invalid characters in  .

## See Also

- [convenience init?(string: String)](nsurl/init(string:).md)
  Initializes an NSURL object with a provided URL string.
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
- [init(fileURLWithPath: String)](nsurl/init(fileurlwithpath:).md)
  Initializes a newly created NSURL referencing the local file or directory at `path`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(string:encodinginvalidcharacters:))*