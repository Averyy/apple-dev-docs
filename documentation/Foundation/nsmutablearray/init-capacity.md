# init(capacity:)

**Framework**: Foundation  
**Kind**: init

Returns an array, initialized with enough memory to initially hold a given number of objects.

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

An array initialized with enough memory to hold `numItems` objects. The returned object might be different than the original receiver.

#### Discussion

Mutable arrays expand as needed; `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer.

## Parameters

- `numItems`: The initial capacity of the new array.

## See Also

- [init?(contentsOfURL: URL)](nsmutablearray/init(contentsofurl:).md)
  Creates and returns a mutable array containing the contents specified by a given URL.
- [init()](nsmutablearray/init.md)
  Initializes a newly allocated array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/init(capacity:))*