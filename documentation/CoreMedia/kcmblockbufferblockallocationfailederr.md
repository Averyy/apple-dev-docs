# kCMBlockBufferBlockAllocationFailedErr

**Framework**: Core Media  
**Kind**: var

An error code that indicates the block allocator failed to allocate a memory block.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCMBlockBufferBlockAllocationFailedErr: OSStatus { get }
```

## See Also

- [var kCMBlockBufferBadCustomBlockSourceErr: OSStatus](kcmblockbufferbadcustomblocksourceerr.md)
  An error code that indicates the custom block source is invalid.
- [var kCMBlockBufferBadLengthParameterErr: OSStatus](kcmblockbufferbadlengthparametererr.md)
  An error code that indicates the block length is zero or doesn’t equal the size of the memory block.
- [var kCMBlockBufferBadOffsetParameterErr: OSStatus](kcmblockbufferbadoffsetparametererr.md)
  An error code that indicates the offset doesn’t point to the location of data in the memory block.
- [var kCMBlockBufferBadPointerParameterErr: OSStatus](kcmblockbufferbadpointerparametererr.md)
  An error code that indicates the block buffer reference is invalid.
- [var kCMBlockBufferEmptyBBufErr: OSStatus](kcmblockbufferemptybbuferr.md)
  An error code that indicates the block buffer is empty.
- [var kCMBlockBufferInsufficientSpaceErr: OSStatus](kcmblockbufferinsufficientspaceerr.md)
  An error code that indicates the system failed to create a new buffer because of insufficient space at the buffer out location.
- [var kCMBlockBufferStructureAllocationFailedErr: OSStatus](kcmblockbufferstructureallocationfailederr.md)
  An error code that indicates the structure allocator failed to allocate a block buffer.
- [var kCMBlockBufferUnallocatedBlockErr: OSStatus](kcmblockbufferunallocatedblockerr.md)
  An error code that indicates the system encountered an unallocated memory block.
- [var kCMBlockBufferNoErr: OSStatus](kcmblockbuffernoerr.md)
  A code that indicates the system successfully created a block buffer with no errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmblockbufferblockallocationfailederr)*