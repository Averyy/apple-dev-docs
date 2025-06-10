# init(pointerFunctions:capacity:)

**Framework**: Foundation  
**Kind**: init

Returns a hash table initialized with the given functions and capacity.

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
init(pointerFunctions functions: NSPointerFunctions, capacity initialCapacity: Int)
```

#### Return Value

A hash table initialized with the given functions and capacity.

#### Discussion

Hash tables allocate additional memory as needed, so `initialCapacity` simply establishes the object’s initial capacity.

## Parameters

- `functions`: The pointer functions for the new hash table.
- `initialCapacity`: The initial capacity of the hash table.

## See Also

- [init(options: NSPointerFunctions.Options, capacity: Int)](nshashtable/init(options:capacity:).md)
  Returns a hash table initialized with the given attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/init(pointerfunctions:capacity:))*