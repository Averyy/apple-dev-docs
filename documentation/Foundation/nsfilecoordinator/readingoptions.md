# NSFileCoordinator.ReadingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options to use when reading the contents or attributes of a file or directory.

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
enum NSFileCoordinatorReadingOptions : NSUInteger;
```

## Topics

### Constants
- [static var withoutChanges: NSFileCoordinator.ReadingOptions](./readingoptions/withoutchanges.md)
- [static var resolvesSymbolicLink: NSFileCoordinator.ReadingOptions](./readingoptions/resolvessymboliclink.md)
- [static var immediatelyAvailableMetadataOnly: NSFileCoordinator.ReadingOptions](./readingoptions/immediatelyavailablemetadataonly.md)
  Specify this constant if you want to read an item’s metadata without triggering a download.
- [static var forUploading: NSFileCoordinator.ReadingOptions](./readingoptions/foruploading.md)
  Specify this content when reading an item for the purpose of uploading its contents.
### Initializers
- [init(rawValue: UInt)](./readingoptions/init%28rawvalue%29.md)
  Instantiates a reading option using an unsigned integer.

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

### Constants
- [NSFileCoordinator.WritingOptions](./writingoptions.md)
  Options to use when changing the contents or attributes of a file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions)*