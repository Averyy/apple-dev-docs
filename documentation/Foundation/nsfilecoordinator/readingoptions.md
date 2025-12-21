# NSFileCoordinator.ReadingOptions

**Framework**: Foundation  
**Kind**: struct

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

## Topics

### Constants
- [static var withoutChanges: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/withoutchanges.md)
- [static var resolvesSymbolicLink: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/resolvessymboliclink.md)
- [static var immediatelyAvailableMetadataOnly: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md)
  Specify this constant if you want to read an item’s metadata without triggering a download.
- [static var forUploading: NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions/foruploading.md)
  Specify this content when reading an item for the purpose of uploading its contents.
### Initializers
- [init(rawValue: UInt)](nsfilecoordinator/readingoptions/init(rawvalue:).md)
  Instantiates a reading option using an unsigned integer.

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

- [NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions.md)
  Options to use when changing the contents or attributes of a file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions)*