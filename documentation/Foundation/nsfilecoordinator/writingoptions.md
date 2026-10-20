# NSFileCoordinator.WritingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSFileCoordinatorWritingOptions : NSUInteger;
```

#### Overview

You must specify only one constant at a time for a given write operation.

## Topics

### Constants
- [static var forDeleting: NSFileCoordinator.WritingOptions](./writingoptions/fordeleting.md)
- [static var forMoving: NSFileCoordinator.WritingOptions](./writingoptions/formoving.md)
- [static var forMerging: NSFileCoordinator.WritingOptions](./writingoptions/formerging.md)
- [static var forReplacing: NSFileCoordinator.WritingOptions](./writingoptions/forreplacing.md)
- [static var contentIndependentMetadataOnly: NSFileCoordinator.WritingOptions](./writingoptions/contentindependentmetadataonly.md)
  Select this option when writing to change the file’s metadata only and not its contents.
### Initializers
- [init(rawValue: UInt)](./writingoptions/init%28rawvalue%29.md)
  Instantiates a writing option using an unsigned integer.

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
- [NSFileCoordinator.ReadingOptions](./readingoptions.md)
  Options to use when reading the contents or attributes of a file or directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions)*