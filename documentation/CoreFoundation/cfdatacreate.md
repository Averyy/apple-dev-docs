# CFDataCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable CFData object using data copied from a specified byte buffer.

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
func CFDataCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex) -> CFData!
```

#### Return Value

A new CFData object, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You must supply a count of the bytes in the buffer. This function always copies the bytes in the provided buffer into internal storage.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `bytes`: A pointer to the byte buffer that contains the raw data to be copied into  .
- `length`: The number of bytes in the buffer ( ).

## See Also

- [func CFDataCreateCopy(CFAllocator!, CFData!) -> CFData!](cfdatacreatecopy(_:_:).md)
  Creates an immutable copy of a CFData object.
- [func CFDataCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFAllocator!) -> CFData!](cfdatacreatewithbytesnocopy(_:_:_:_:).md)
  Creates an immutable CFData object from an external (client-owned) byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatacreate(_:_:_:))*