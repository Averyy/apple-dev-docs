# CFDataCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates an immutable CFData object using data copied from a specified byte buffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDataCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex) -> CFData!
```

```c
extern CFDataRefCFDataCreate(CFAllocatorRef allocator, const UInt8 *bytes, CFIndex length);
```

## Return Value

A new CFData object, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You must supply a count of the bytes in the buffer. This function always copies the bytes in the provided buffer into internal storage.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `bytes`: A pointer to the byte buffer that contains the raw data to be copied into `theData`.
- `length`: The number of bytes in the buffer (`bytes`).

## See Also

### Creating a CFData Object
- [func CFDataCreateCopy(CFAllocator!, CFData!) -> CFData!](./cfdatacreatecopy%28_,_%29.md)
  Creates an immutable copy of a CFData object.
- [func CFDataCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFAllocator!) -> CFData!](./cfdatacreatewithbytesnocopy%28_,_,_,_%29.md)
  Creates an immutable CFData object from an external (client-owned) byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatacreate(_:_:_:))*