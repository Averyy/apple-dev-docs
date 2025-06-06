# init(capacity:)

**Framework**: Foundation  
**Kind**: init

Returns a counted set object initialized with enough memory to hold a given number of objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(capacity numItems: Int)
```

#### Return Value

A counted set object initialized with enough memory to hold `numItems` objects

#### Discussion

The method is the designated initializer for [`NSCountedSet`](nscountedset.md).

Note that the capacity is simply a hint to help initial memory allocation—the initial count of the object is `0`, and the set still grows and shrinks as you add and remove objects. The hint is typically useful if the set will become large.

## Parameters

- `numItems`: The initial capacity of the new counted set.

## See Also

- [init(capacity: Int)](nsmutableset/init(capacity:).md)
  Returns an initialized mutable set with a given initial capacity.
- [convenience init(array: [Any])](nscountedset/init(array:).md)
  Returns a counted set object initialized with the contents of a given array.
- [convenience init(set: Set<AnyHashable>)](nscountedset/init(set:).md)
  Returns a counted set object initialized with the contents of a given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/init(capacity:))*