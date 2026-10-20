# NSURL.BookmarkFileCreationOptions

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

Options used when creating file bookmark data

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
typealias BookmarkFileCreationOptions = Int
```

```c
typedef NSUInteger NSURLBookmarkFileCreationOptions;
```

#### Discussion

See [`NSURL.BookmarkCreationOptions`](./bookmarkcreationoptions.md) for more information.

## See Also

### Working with Bookmark Data
- [class func bookmarkData(withContentsOf: URL) throws -> Data](./bookmarkdata%28withcontentsof%29.md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [func bookmarkData(options: NSURL.BookmarkCreationOptions, includingResourceValuesForKeys: [URLResourceKey]?, relativeTo: URL?) throws -> Data](./bookmarkdata%28options,includingresourcevaluesforkeys,relativeto%29.md)
  Returns a bookmark for the URL, created with specified options and resource values.
- [class func resourceValues(forKeys: [URLResourceKey], fromBookmarkData: Data) -> [URLResourceKey : Any]?](./resourcevalues%28forkeys,frombookmarkdata%29.md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [class func writeBookmarkData(Data, to: URL, options: NSURL.BookmarkFileCreationOptions) throws](./writebookmarkdata%28_,to,options%29.md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func startAccessingSecurityScopedResource() -> Bool](./startaccessingsecurityscopedresource%28%29.md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func stopAccessingSecurityScopedResource()](./stopaccessingsecurityscopedresource%28%29.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [struct BookmarkCreationOptions](./bookmarkcreationoptions.md)
  Options used when creating bookmark data.
- [struct BookmarkResolutionOptions](./bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkfilecreationoptions)*