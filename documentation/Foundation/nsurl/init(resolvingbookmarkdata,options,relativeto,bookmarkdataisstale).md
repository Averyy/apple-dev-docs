# init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly created NSURL that points to a location specified by resolving bookmark data.

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
convenience init(resolvingBookmarkData bookmarkData: Data, options: NSURL.BookmarkResolutionOptions = [], relativeTo relativeURL: URL?, bookmarkDataIsStale isStale: UnsafeMutablePointer<ObjCBool>?) throws
```

```objc
- (instancetype) initByResolvingBookmarkData:(NSData *) bookmarkData options:(NSURLBookmarkResolutionOptions) options relativeToURL:(NSURL *) relativeURL bookmarkDataIsStale:(BOOL *) isStale error:(NSError **) error;
```

## Return Value

An NSURL initialized by resolving `bookmarkData`.

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `bookmarkData`: The bookmark data the URL is derived from.
- `options`: Options taken into account when resolving the bookmark data.
- `relativeURL`: The base URL that the bookmark data is relative to.
- `isStale`: If [`true`](../../Swift/true.md), the bookmark data is stale.

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
- [class func fileURL(withFileSystemRepresentation: UnsafePointer<CChar>, isDirectory: Bool, relativeTo: URL?) -> URL](./fileurl%28withfilesystemrepresentation,isdirectory,relativeto%29.md)
  Returns a new URL object initialized with a C string representing a local file system path.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](./getfilesystemrepresentation%28_,maxlength%29.md)
  Fills the provided buffer with a C string representing a local file system path.
- [+ URLWithString:](./urlwithstring_.md)
  Creates and returns an NSURL object initialized with a provided URL string.
- [+ URLWithString:encodingInvalidCharacters:](./urlwithstring_encodinginvalidcharacters_.md)
  Creates and returns an instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [+ URLWithString:relativeToURL:](./urlwithstring_relativetourl_.md)
  Creates and returns an NSURL object initialized with a base URL and a relative string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:))*