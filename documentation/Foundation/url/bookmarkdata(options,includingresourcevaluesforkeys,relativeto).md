# bookmarkData(options:includingResourceValuesForKeys:relativeTo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns bookmark data for the URL, created with specified options and resource values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func bookmarkData(options: URL.BookmarkCreationOptions = [], includingResourceValuesForKeys keys: Set<URLResourceKey>? = nil, relativeTo url: URL? = nil) throws -> Data
```

## See Also

### Creating bookmarks
- [static func bookmarkData(withContentsOf: URL) throws -> Data](./bookmarkdata%28withcontentsof%29.md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [static func writeBookmarkData(Data, to: URL) throws](./writebookmarkdata%28_,to%29.md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [static func resourceValues(forKeys: Set<URLResourceKey>, fromBookmarkData: Data) -> URLResourceValues?](./resourcevalues%28forkeys,frombookmarkdata%29.md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [typealias BookmarkCreationOptions](./bookmarkcreationoptions.md)
  An alias for bookmark creation options.
- [struct BookmarkCreationOptions](../nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:))*