# URLWithString:relativeToURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an NSURL object initialized with a base URL and a relative string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) URLWithString:(NSString *) URLString relativeToURL:(NSURL *) baseURL;
```

## Return Value

An NSURL object initialized with `URLString` and `baseURL`. If `URLString` was malformed or `nil`, returns `nil`.

## Discussion

This method allows you to create a URL relative to a base path or URL. For example, if you have the URL for a folder on disk and the name of a file within that folder, you can construct a URL for the file by providing the folder’s URL as the base path (with a trailing slash) and the filename as the string part.

> ❗ **Important**:  For apps linked on or after iOS 17 and aligned OS versions, [`NSURL`](../nsurl.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) parsing as [`NSURLComponents`](../nsurlcomponents.md). This unifies the parsing behaviors of the `NSURL` and `NSURLComponents` APIs. Now, `NSURL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

To check if `URLString` is strictly valid according to the RFC, use the new `[NSURL URLWithString:URLString encodingInvalidCharacters:NO]` method. This method leaves all characters as they are and returns `nil` if `URLString` is explicitly invalid.

For apps linked before iOS 17, this method expects `URLString` to contain only characters that are allowed in a properly formed URL. All other characters must be properly percent encoded. Any percent-encoded characters are interpreted using UTF-8 encoding.

## Parameters

- `URLString`: The URL string with which to initialize the NSURL object. May not be `nil`. Linked on or after iOS 17, this method parses `URLString` according to RFC 3986. Linked before iOS 17, this method parses `URLString` according to RFCs 1738 and 1808. `URLString` is interpreted relative to `baseURL`.
- `baseURL`: The base URL for the NSURL object.

## See Also

### Creating a URL object
- [+ URLWithString:](./urlwithstring_.md)
  Creates and returns an NSURL object initialized with a provided URL string.
- [convenience init?(string: String)](./init%28string%29.md)
  Initializes an NSURL object with a provided URL string.
- [+ URLWithString:encodingInvalidCharacters:](./urlwithstring_encodinginvalidcharacters_.md)
  Creates and returns an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/urlwithstring:relativetourl:)*