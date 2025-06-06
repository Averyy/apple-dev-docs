# NSURL.BookmarkFileCreationOptions

**Framework**: Foundation  
**Kind**: typealias

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

#### Discussion

See [`NSURL.BookmarkCreationOptions`](nsurl/bookmarkcreationoptions.md) for more information.

## See Also

- [class func bookmarkData(withContentsOf: URL) throws -> Data](nsurl/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [func bookmarkData(options: NSURL.BookmarkCreationOptions, includingResourceValuesForKeys: [URLResourceKey]?, relativeTo: URL?) throws -> Data](nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns a bookmark for the URL, created with specified options and resource values.
- [class func resourceValues(forKeys: [URLResourceKey], fromBookmarkData: Data) -> [URLResourceKey : Any]?](nsurl/resourcevalues(forkeys:frombookmarkdata:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [class func writeBookmarkData(Data, to: URL, options: NSURL.BookmarkFileCreationOptions) throws](nsurl/writebookmarkdata(_:to:options:).md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [func startAccessingSecurityScopedResource() -> Bool](nsurl/startaccessingsecurityscopedresource.md)
  In an app that has adopted App Sandbox, makes the resource pointed to by a security-scoped URL available to the app.
- [func stopAccessingSecurityScopedResource()](nsurl/stopaccessingsecurityscopedresource.md)
  In an app that adopts App Sandbox, revokes access to the resource pointed to by a security-scoped URL.
- [struct BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.
- [struct BookmarkResolutionOptions](nsurl/bookmarkresolutionoptions.md)
  Options used when resolving bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/bookmarkfilecreationoptions)*