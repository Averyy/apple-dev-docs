# init(arrayLiteral:)

**Framework**: Accelerate  
**Kind**: init

Returns a new shape with the specified size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
init(arrayLiteral: BNNS.Shape.ArrayLiteralElement...)
```

#### Discussion

This initializer returns a shape with the default layout for the rank that’s equal to the count of `arrayLiteral`. The default layouts for each dimensionality are:

## Parameters

- `arrayLiteral`: An array that specifies the number of values in each dimension.

## See Also

- [init([Int], dataLayout: BNNS.DataLayout?, stride: [Int]?)](bnns/shape/init(_:datalayout:stride:).md)
  Returns a new shape with the specified size, data layout, and stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape/init(arrayliteral:))*