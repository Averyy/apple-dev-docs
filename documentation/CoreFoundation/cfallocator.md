# CFAllocator

**Framework**: Core Foundation  
**Kind**: class

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
class CFAllocator
```

#### Overview

CFAllocator is an opaque type that allocates and deallocates memory for you. You never have to allocate, reallocate, or deallocate memory directly for Core Foundation objects—and rarely should you. You pass CFAllocator objects into functions that create objects; these functions have “Create” embedded in their names, for example, `CFStringCreateWithPascalString`. The creation functions use the allocators to allocate memory for the objects they create.

## Topics

### Creating an Allocator
- [func CFAllocatorCreate(CFAllocator!, UnsafeMutablePointer<CFAllocatorContext>!) -> Unmanaged<CFAllocator>!](cfallocatorcreate(_:_:).md)
  Creates an allocator object.
### Managing Memory with an Allocator
- [func CFAllocatorAllocate(CFAllocator!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorallocate(_:_:_:).md)
  Allocates memory using the specified allocator.
- [func CFAllocatorDeallocate(CFAllocator!, UnsafeMutableRawPointer!)](cfallocatordeallocate(_:_:).md)
  Deallocates a block of memory with a given allocator.
- [func CFAllocatorGetPreferredSizeForSize(CFAllocator!, CFIndex, CFOptionFlags) -> CFIndex](cfallocatorgetpreferredsizeforsize(_:_:_:).md)
  Obtains the number of bytes likely to be allocated upon a specific request.
- [func CFAllocatorReallocate(CFAllocator!, UnsafeMutableRawPointer!, CFIndex, CFOptionFlags) -> UnsafeMutableRawPointer!](cfallocatorreallocate(_:_:_:_:).md)
  Reallocates memory using the specified allocator.
### Getting and Setting the Default Allocator
- [func CFAllocatorGetDefault() -> Unmanaged<CFAllocator>!](cfallocatorgetdefault().md)
  Gets the default allocator object for the current thread.
- [func CFAllocatorSetDefault(CFAllocator!)](cfallocatorsetdefault(_:).md)
  Sets the given allocator as the default for the current thread.
### Getting an Allocator’s Context
- [func CFAllocatorGetContext(CFAllocator!, UnsafeMutablePointer<CFAllocatorContext>!)](cfallocatorgetcontext(_:_:).md)
  Obtains the context of the specified allocator or of the default allocator.
### Getting the CFAllocator Type ID
- [func CFAllocatorGetTypeID() -> CFTypeID](cfallocatorgettypeid().md)
  Returns the type identifier for the CFAllocator opaque type.
### Callbacks
- [typealias CFAllocatorAllocateCallBack](cfallocatorallocatecallback.md)
  A prototype for a function callback that allocates memory of a requested size.
- [typealias CFAllocatorCopyDescriptionCallBack](cfallocatorcopydescriptioncallback.md)
  A prototype for a function callback that provides a description of the specified data.
- [typealias CFAllocatorDeallocateCallBack](cfallocatordeallocatecallback.md)
  A prototype for a function callback that deallocates a block of memory.
- [typealias CFAllocatorPreferredSizeCallBack](cfallocatorpreferredsizecallback.md)
  A prototype for a function callback that gives the size of memory likely to be allocated, given a certain request.
- [typealias CFAllocatorReallocateCallBack](cfallocatorreallocatecallback.md)
  A prototype for a function callback that reallocates memory of a requested size for an existing block of memory.
- [typealias CFAllocatorReleaseCallBack](cfallocatorreleasecallback.md)
  A prototype for a function callback that releases the given data.
- [typealias CFAllocatorRetainCallBack](cfallocatorretaincallback.md)
  A prototype for a function callback that retains the given data.
### Data Types
- [struct CFAllocatorContext](cfallocatorcontext.md)
  A structure that defines the context or operating environment for an allocator (CFAllocator) object. Every Core Foundation allocator object must have a context defined for it.
### Constants
- [Predefined Allocators](predefined-allocators.md)
  CFAllocator provides the following predefined allocators. In general, you should use `kCFAllocatorDefault` unless one of the special circumstances exist below.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Memory Management Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocator)*