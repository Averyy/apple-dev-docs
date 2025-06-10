# CMMemoryPool APIs

**Framework**: Core Media

An object that optimizes memory allocation when working with large blocks of memory.

#### Overview

An instance of `CMMemoryPool` is a memory allocation service that holds a pool of recently deallocated memory. Its purpose is to speed up subsequent allocations of the same size. Use this API in cases where you need to repeatedly allocate large blocks of memory, such as a video encoding app that outputs compressed data.

This object allocates memory by page. It doesn’t suballocate memory within pages, so don’t use it to allocate small blocks. For example, when calling the [`CMBlockBufferCreateWithMemoryBlock(allocator:memoryBlock:blockLength:blockAllocator:customBlockSource:offsetToData:dataLength:flags:blockBufferOut:)`](cmblockbuffercreatewithmemoryblock(allocator:memoryblock:blocklength:blockallocator:customblocksource:offsettodata:datalength:flags:blockbufferout:).md) function, you can use it as the `blockAllocator` argument, but not as the `structureAllocator` argument (use [`kCFAllocatorDefault`](https://developer.apple.com/documentation/CoreFoundation/kCFAllocatorDefault) instead).

When you no longer need to allocate memory from the pool, invalidate it by calling the [`CMMemoryPoolInvalidate(_:)`](cmmemorypoolinvalidate(_:).md) function, which tells the pool to stop holding memory for reuse.

> **Note**:  A pool’s [`CFAllocator`](https://developer.apple.com/documentation/CoreFoundation/CFAllocator) can outlive the pool itself. After you invalidate a memory pool, its [`CFAllocator`](https://developer.apple.com/documentation/CoreFoundation/CFAllocator) instance allocates and deallocates with no pooling behavior.

A memory pool deallocates memory if it isn’t reused in `0.5` seconds, so that short-term peak usage doesn’t cause persistent bloat. You can override this period by specifying a value for [`kCMMemoryPoolOption_AgeOutPeriod`](kcmmemorypooloption_ageoutperiod.md). The system does this “aging out” during the pool’s [`CFAllocatorAllocate(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFAllocatorAllocate(_:_:_:)) and [`CFAllocatorDeallocate(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFAllocatorDeallocate(_:_:)) calls.

## Topics

### Creating a Memory Pool
- [func CMMemoryPoolCreate(options: CFDictionary?) -> CMMemoryPool](cmmemorypoolcreate(options:).md)
  Creates a memory pool.
### Managing a Memory Pool
- [func CMMemoryPoolGetAllocator(CMMemoryPool) -> CFAllocator](cmmemorypoolgetallocator(_:).md)
  Returns the allocator for the memory pool.
- [func CMMemoryPoolFlush(CMMemoryPool)](cmmemorypoolflush(_:).md)
  Deallocates all memory the pool holds.
- [func CMMemoryPoolInvalidate(CMMemoryPool)](cmmemorypoolinvalidate(_:).md)
  Invalidates the memory pool, which causes its allocator to stop recycling memory.
### Accessing the Type Identifier
- [func CMMemoryPoolGetTypeID() -> CFTypeID](cmmemorypoolgettypeid().md)
  Returns the type identifier of memory pool objects.
### Data Types
- [class CMMemoryPool](cmmemorypool.md)
  An instance that optimizes memory allocation when working with large blocks of memory.
### Errors
- [var kCMMemoryPoolError_AllocationFailed: OSStatus](kcmmemorypoolerror_allocationfailed.md)
  An error that indicates the system failed to allocate an internal data structure.
- [var kCMMemoryPoolError_InvalidParameter: OSStatus](kcmmemorypoolerror_invalidparameter.md)
  An error that indicates you called an API with an invalid parameter.

## See Also

- [CMSimpleQueue APIs](cmsimplequeue-api.md)
  A simple, lockless FIFO queue of elements.
- [CMBufferQueue APIs](cmbufferqueue-api.md)
  A queue of timed buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmemorypool-api)*