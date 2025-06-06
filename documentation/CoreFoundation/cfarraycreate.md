# CFArrayCreate(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new immutable array with the given values.

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
func CFArrayCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>!) -> CFArray!
```

#### Return Value

A new immutable array containing `numValues` from `values`, or `NULL` if there was a problem creating the object. Ownership follows [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new array and its storage for values. Pass   or   to use the current default allocator.
- `values`: A C array of the pointer-sized values to be in the new array. The values in the new array are ordered in the same order in which they appear in this C array. This value may be   if   is  . This C array is not changed or freed by this function. If   is not a valid pointer to a C array of at least   elements, the behavior is undefined.
- `numValues`: The number of values to copy from the values C array into the new array. This number will be the count of the new array—it must not be negative or greater than the number of elements in  .
- `callBacks`: If the collection contains only CFType objects, then pass a pointer to   ( ) to use the default callback functions.

## See Also

- [func CFArrayCreateCopy(CFAllocator!, CFArray!) -> CFArray!](cfarraycreatecopy(_:_:).md)
  Creates a new immutable array with the values from another array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraycreate(_:_:_:_:))*