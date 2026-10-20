# CMBlockBuffer.Error

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that defines block buffer errors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Error
```

## Topics

### Errors
- [static let badCustomBlockSource: NSError](./error/badcustomblocksource.md)
  An error that indicates an attempt to create a block buffer without a valid source.
- [static let badLengthParameter: NSError](./error/badlengthparameter.md)
  An error that indicates you called a function with an invalid length parameter.
- [static let badOffsetParameter: NSError](./error/badoffsetparameter.md)
  An error that indicates you called a function with offset value is out of range.
- [static let badPointerParameter: NSError](./error/badpointerparameter.md)
  An error that indicates a parameter is invalid.
- [static let blockAllocationFailed: NSError](./error/blockallocationfailed.md)
  An error that indicates you specified an invalid allocation block.
- [static let emptyBlockBuffer: NSError](./error/emptyblockbuffer.md)
  An error that indicates you passed an empty block buffer to a function.
- [static let insufficientSpace: NSError](./error/insufficientspace.md)
  An error that indicates there’s insufficient space to perform the operation.
- [static let structureAllocationFailed: NSError](./error/structureallocationfailed.md)
  An error that indicates the allocation of a structure failed.
- [static let unallocatedBlock: NSError](./error/unallocatedblock.md)
  An error that indicates a function encountered an unallocated block of memory.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Data Types
- [CMBlockBuffer.Flags](./flags.md)
  A structure that defines feature and control flags.
- [CMBlockBuffer.Slice](./slice.md)
  A slice of a `CMBlockBuffer` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmblockbuffer/error)*