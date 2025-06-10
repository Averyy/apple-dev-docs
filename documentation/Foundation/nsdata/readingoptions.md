# NSData.ReadingOptions

**Framework**: Foundation  
**Kind**: struct

Options for methods used to read data objects.

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
struct ReadingOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](nsdata/readingoptions/init(rawvalue:).md)
### Constants
- [static var mappedIfSafe: NSData.ReadingOptions](nsdata/readingoptions/mappedifsafe.md)
  A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [static var uncached: NSData.ReadingOptions](nsdata/readingoptions/uncached.md)
  A hint indicating the file should not be stored in the file-system caches.
- [static var alwaysMapped: NSData.ReadingOptions](nsdata/readingoptions/alwaysmapped.md)
  Hint to map the file in if possible.
- [static var mappedIfSafe: NSData.ReadingOptions](nsdata/readingoptions/mappedifsafe.md)
  A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [static var uncached: NSData.ReadingOptions](nsdata/readingoptions/uncached.md)
  A hint indicating the file should not be stored in the file-system caches.
- [static var alwaysMapped: NSData.ReadingOptions](nsdata/readingoptions/alwaysmapped.md)
  Hint to map the file in if possible.
### Legacy Constants
- [static var dataReadingMapped: NSData.ReadingOptions](nsdata/readingoptions/datareadingmapped.md)
  Deprecated name for [`mappedIfSafe`](nsdata/readingoptions/mappedifsafe.md).
- [static var mappedRead: NSData.ReadingOptions](nsdata/readingoptions/mappedread.md)
  Deprecated name for [`dataReadingMapped`](nsdata/readingoptions/datareadingmapped.md).
- [static var uncachedRead: NSData.ReadingOptions](nsdata/readingoptions/uncachedread.md)
  Deprecated name for [`uncached`](nsdata/readingoptions/uncached.md).
- [static var dataReadingMapped: NSData.ReadingOptions](nsdata/readingoptions/datareadingmapped.md)
  Deprecated name for [`mappedIfSafe`](nsdata/readingoptions/mappedifsafe.md).
- [static var mappedRead: NSData.ReadingOptions](nsdata/readingoptions/mappedread.md)
  Deprecated name for [`dataReadingMapped`](nsdata/readingoptions/datareadingmapped.md).
- [static var uncachedRead: NSData.ReadingOptions](nsdata/readingoptions/uncachedread.md)
  Deprecated name for [`uncached`](nsdata/readingoptions/uncached.md).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [init?(contentsOfMappedFile: String)](nsdata/init(contentsofmappedfile:).md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](nsdata/datawithcontentsofmappedfile(_:).md)
  Creates a data object from the mapped file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/readingoptions)*