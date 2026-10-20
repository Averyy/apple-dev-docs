# bookmarkData(withContentsOf:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.

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
static func bookmarkData(withContentsOf url: URL) throws -> Data
```

#### Discussion

If bookmarkFileURL refers to an alias file created prior to OS X 10.6 that contains Alias Manager information but no bookmark data, this method synthesizes bookmark data for the file.

## See Also

### Creating bookmarks
- [func bookmarkData(options: URL.BookmarkCreationOptions, includingResourceValuesForKeys: Set<URLResourceKey>?, relativeTo: URL?) throws -> Data](./bookmarkdata%28options,includingresourcevaluesforkeys,relativeto%29.md)
  Returns bookmark data for the URL, created with specified options and resource values.
- [static func writeBookmarkData(Data, to: URL) throws](./writebookmarkdata%28_,to%29.md)
  Creates an alias file on disk at a specified location with specified bookmark data.
- [static func resourceValues(forKeys: Set<URLResourceKey>, fromBookmarkData: Data) -> URLResourceValues?](./resourcevalues%28forkeys,frombookmarkdata%29.md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [typealias BookmarkCreationOptions](./bookmarkcreationoptions.md)
  An alias for bookmark creation options.
- [struct BookmarkCreationOptions](../nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/bookmarkdata(withcontentsof:))*