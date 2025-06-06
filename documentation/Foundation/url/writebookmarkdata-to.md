# writeBookmarkData(_:to:)

**Framework**: Foundation  
**Kind**: method

Creates an alias file on disk at a specified location with specified bookmark data.

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
static func writeBookmarkData(_ data: Data, to url: URL) throws
```

#### Discussion

The `data` must have been created with the [`suitableForBookmarkFile`](nsurl/bookmarkcreationoptions/suitableforbookmarkfile.md) option. The `url` must either refer to an existing file (which will be overwritten), or to location in an existing directory.

## See Also

- [func bookmarkData(options: URL.BookmarkCreationOptions, includingResourceValuesForKeys: Set<URLResourceKey>?, relativeTo: URL?) throws -> Data](url/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:).md)
  Returns bookmark data for the URL, created with specified options and resource values.
- [static func bookmarkData(withContentsOf: URL) throws -> Data](url/bookmarkdata(withcontentsof:).md)
  Initializes and returns bookmark data derived from an alias file pointed to by a specified URL.
- [static func resourceValues(forKeys: Set<URLResourceKey>, fromBookmarkData: Data) -> URLResourceValues?](url/resourcevalues(forkeys:frombookmarkdata:).md)
  Returns the resource values for properties identified by a specified array of keys contained in specified bookmark data.
- [typealias BookmarkCreationOptions](url/bookmarkcreationoptions.md)
  An alias for bookmark creation options.
- [struct BookmarkCreationOptions](nsurl/bookmarkcreationoptions.md)
  Options used when creating bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/writebookmarkdata(_:to:))*