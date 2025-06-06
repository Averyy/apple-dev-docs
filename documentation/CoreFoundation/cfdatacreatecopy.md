# CFDataCreateCopy(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates an immutable copy of a CFData object.

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
func CFDataCreateCopy(_ allocator: CFAllocator!, _ theData: CFData!) -> CFData!
```

#### Return Value

An immutable copy of `theData`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The resulting object has the same byte contents as the original object, but it is always immutable. If the specified allocator and the allocator of the original object are the same, and the string is already immutable, this function may simply increment the retain count without making a true copy. To the caller, however, the resulting object is a true immutable copy, except the operation was more efficient.

Use this function when you need to pass a CFData object into another function by value (not reference).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `theData`: The CFData object to copy.

## See Also

- [func CFDataCreate(CFAllocator!, UnsafePointer<UInt8>!, CFIndex) -> CFData!](cfdatacreate(_:_:_:).md)
  Creates an immutable CFData object using data copied from a specified byte buffer.
- [func CFDataCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFAllocator!) -> CFData!](cfdatacreatewithbytesnocopy(_:_:_:_:).md)
  Creates an immutable CFData object from an external (client-owned) byte buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatacreatecopy(_:_:))*