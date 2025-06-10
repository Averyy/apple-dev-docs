# init(contentsOfURL:)

**Framework**: Foundation  
**Kind**: init

Creates a data object from the data at the specified file URL, or returns `nil` if the system can’t create one.

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
init?(contentsOf url: URL)
```

#### Discussion

> ❗ **Important**:  As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead. For more information, see [`Improving performance and stability when accessing the file system`](improving-performance-and-stability-when-accessing-the-file-system.md).

If you specify a malformed URL or the referenced location doesn’t exist on disk, the initializer fails and returns [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0). To handle such errors, use [`init(contentsOfURL:options:)`](nsdata/init(contentsofurl:options:)-5abi3.md) instead.

## Parameters

- `url`: The location on disk of the data to read.

## See Also

- [convenience init?(contentsOfURL: URL)](nsdata/init(contentsofurl:)-6foqd.md)
  Creates a data object from the data at the specified file URL.
- [convenience init(contentsOfURL: URL, options: NSData.ReadingOptions) throws](nsdata/init(contentsofurl:options:)-95rht.md)
  Creates a data object from the data at the provided file URL using specific reading options.
- [init?(contentsOfFile: String)](nsdata/init(contentsoffile:).md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](nsdata/init(contentsoffile:options:).md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfURL: URL, options: NSData.ReadingOptions) throws](nsdata/init(contentsofurl:options:)-5abi3.md)
  Creates a data object from the data at the provided file URL using specific reading options.
- [NSData.ReadingOptions](nsdata/readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](nsdata/init(contentsofmappedfile:).md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](nsdata/datawithcontentsofmappedfile(_:).md)
  Creates a data object from the mapped file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(contentsofurl:)-6rrnr)*