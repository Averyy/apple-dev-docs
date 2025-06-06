# init(capacity:)

**Framework**: Foundation  
**Kind**: init

Returns an initialized mutable set with a given initial capacity.

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

An initialized mutable set with initial capacity to hold `numItems` members. The returned set might be different than the original receiver.

#### Discussion

Mutable sets allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer for `NSMutableSet`.

## Parameters

- `numItems`: The initial capacity of the set.

## See Also

- [init()](nsmutableset/init.md)
  Initializes a newly allocated set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableset/init(capacity:))*