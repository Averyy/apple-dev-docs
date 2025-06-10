# init(string:)

**Framework**: Foundation  
**Kind**: init

Initializes an NSURL object with a provided URL string.

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
convenience init?(string URLString: String)
```

#### Return Value

An NSURL object initialized with `URLString`. If the URL string was malformed, returns `nil`.

#### Discussion

> ❗ **Important**:  For apps linked on or after iOS 17 and aligned OS versions, [`NSURL`](nsurl.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [`RFC 3986`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc3986.txt) parsing as [`NSURLComponents`](nsurlcomponents.md). This unifies the parsing behaviors of the `NSURL` and `NSURLComponents` APIs. Now, `NSURL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

To check if `URLString` is strictly valid according to the RFC, use the new `[NSURL URLWithString:URLString encodingInvalidCharacters:NO]` method. This method leaves all characters as they are and returns `nil` if `URLString` is explicitly invalid.

For apps linked before iOS 17, this method expects `URLString` to contain only characters that are allowed in a properly formed URL. All other characters must be properly percent encoded. Any percent-encoded characters are interpreted using UTF-8 encoding.

## Parameters

- `URLString`: The URL string with which to initialize the NSURL object. Linked on or after iOS 17, this method parses   according to RFC 3986. Linked before iOS 17, this method parses   according to RFCs 1738 and 1808.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(string:))*