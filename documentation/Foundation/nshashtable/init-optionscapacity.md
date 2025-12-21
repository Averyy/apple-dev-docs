# init(options:capacity:)

**Framework**: Foundation  
**Kind**: init

Returns a hash table initialized with the given attributes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(options: NSPointerFunctions.Options = [], capacity initialCapacity: Int)
```

#### Return Value

A hash table initialized with options specified by `options` and initial capacity of `capacity`.

## Parameters

- `options`: A bit field that specifies the options for the elements in the hash table. For possible values, see  .
- `initialCapacity`: The initial number of elements the hash table can hold.

## See Also

- [Collections Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [init(pointerFunctions: NSPointerFunctions, capacity: Int)](nshashtable/init(pointerfunctions:capacity:).md)
  Returns a hash table initialized with the given functions and capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/init(options:capacity:))*