# fill(with:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Assigns the shaped array’s elements to the elements in a collection, repeatedly, if necessary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func fill<C>(with collection: C) where C : Collection, Self.Scalar == C.Element
```

**Other overloads**:

```swift
mutating func fill(with value: Self.Scalar)
```

## Discussion

The shaped array assigns the collection’s elements in first-major order, which is equivalent to row-major order for two-dimensional arrays.

## Parameters

- `collection`: A collection of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/fill(with:)-6a5k1)*