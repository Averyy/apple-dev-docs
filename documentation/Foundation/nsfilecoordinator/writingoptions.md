# NSFileCoordinator.WritingOptions

**Framework**: Foundation  
**Kind**: struct

Options to use when changing the contents or attributes of a file or directory.

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
struct WritingOptions
```

#### Overview

You must specify only one constant at a time for a given write operation.

## Topics

### Constants
- [static var forDeleting: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/fordeleting.md)
- [static var forMoving: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formoving.md)
- [static var forMerging: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formerging.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.
### Createing a Writing Option
- [init(rawValue: UInt)](nsfilecoordinator/writingoptions/init(rawvalue:).md)
  Instantiates a writing option using an unsigned integer.
- [static var forDeleting: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/fordeleting.md)
- [static var forMoving: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formoving.md)
- [static var forMerging: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/formerging.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](nsfilecoordinator/writingoptions/contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSFileCoordinator.ReadingOptions](nsfilecoordinator/readingoptions.md)
  Options to use when reading the contents or attributes of a file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions)*