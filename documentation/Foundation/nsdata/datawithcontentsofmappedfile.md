# dataWithContentsOfMappedFile(_:)

**Framework**: Foundation  
**Kind**: method

Creates a data object from the mapped file at a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func dataWithContentsOfMappedFile(_ path: String) -> Any?
```

#### Discussion

This method returns `nil` if the data object could not be created

Because of file mapping restrictions, this method should only be used if the file is guaranteed to exist for the duration of the data object’s existence. It is generally safer to use the [`dataWithContentsOfFile:`](nsdata/datawithcontentsoffile:.md) method.

This methods assumes mapped files are available from the underlying operating system. A mapped file uses virtual memory techniques to avoid copying pages of the file into memory until they are actually needed.

## Parameters

- `path`: The absolute path of the file from which to read data.

## See Also

- [convenience init?(contentsOfURL: URL)](nsdata/init(contentsofurl:)-6foqd.md)
  Creates a data object from the data at the specified file URL.
- [convenience init(contentsOfURL: URL, options: NSData.ReadingOptions) throws](nsdata/init(contentsofurl:options:)-95rht.md)
  Creates a data object from the data at the provided file URL using specific reading options.
- [init?(contentsOfFile: String)](nsdata/init(contentsoffile:).md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](nsdata/init(contentsoffile:options:).md)
  Initializes a data object with the content of the file at a given path.
- [init?(contentsOfURL: URL)](nsdata/init(contentsofurl:)-6rrnr.md)
  Creates a data object from the data at the specified file URL, or returns `nil` if the system can’t create one.
- [init(contentsOfURL: URL, options: NSData.ReadingOptions) throws](nsdata/init(contentsofurl:options:)-5abi3.md)
  Creates a data object from the data at the provided file URL using specific reading options.
- [NSData.ReadingOptions](nsdata/readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](nsdata/init(contentsofmappedfile:).md)
  Initializes a data object with the contents of the mapped file specified by a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsofmappedfile(_:))*