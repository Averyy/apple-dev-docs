# NSData.ReadingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSDataReadingOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./readingoptions/init%28rawvalue%29.md)
### Constants
- [static var mappedIfSafe: NSData.ReadingOptions](./readingoptions/mappedifsafe.md)
  A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [static var uncached: NSData.ReadingOptions](./readingoptions/uncached.md)
  A hint indicating the file should not be stored in the file-system caches.
- [static var alwaysMapped: NSData.ReadingOptions](./readingoptions/alwaysmapped.md)
  Hint to map the file in if possible.
### Legacy Constants
- [static var dataReadingMapped: NSData.ReadingOptions](./readingoptions/datareadingmapped.md)
  Deprecated name for [`mappedIfSafe`](./readingoptions/mappedifsafe.md).
- [static var mappedRead: NSData.ReadingOptions](./readingoptions/mappedread.md)
  Deprecated name for [`dataReadingMapped`](./readingoptions/datareadingmapped.md).
- [static var uncachedRead: NSData.ReadingOptions](./readingoptions/uncachedread.md)
  Deprecated name for [`uncached`](./readingoptions/uncached.md).

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Reading Data from a File
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](./init%28contentsoffile,options%29.md)
  Initializes a data object with the content of the file at a given path.
- [init?(contentsOfMappedFile: String)](./init%28contentsofmappedfile%29.md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](./datawithcontentsofmappedfile%28_%29.md)
  Creates a data object from the mapped file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/readingoptions)*