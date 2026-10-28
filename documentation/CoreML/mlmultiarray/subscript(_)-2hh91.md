# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the multiarray by using a linear offset.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
subscript(idx: Int) -> NSNumber { get set }
```

```objc
- (NSNumber *) objectAtIndexedSubscript:(NSInteger) idx;
```

**Other overloads**:

```swift
subscript(key: [NSNumber]) -> NSNumber { get set }
```

## Return Value

A number.

## Discussion

Use the subscript to linearly index a one-dimensional multiarray in the same way as a conventional array.

```swift
let oneDimensionalArray = try MLMultiArray(shape: [42], dataType: .int32)
let numberValue = oneDimensionalArray[7]
```

Multiarrays with more than one dimension order their elements in row-major order. In these cases, calculate a linear offset by summing the products of each dimension’s index with the dimension’s stride (See [`strides`](./strides.md)).

```swift
let multiArray = try MLMultiArray(shape: [5, 22, 17], dataType: .double)

let dimension0 = 3
let dimension1 = 5
let dimension2 = 7

var linearIndex = 0
linearIndex += dimension0 * multiArray.strides[0].intValue
linearIndex += dimension1 * multiArray.strides[1].intValue
linearIndex += dimension2 * multiArray.strides[2].intValue

let previousNumberValue = multiArray[linearIndex]
multiArray[linearIndex] = 2.718_28
```

## Parameters

- `idx`: A linear offset index that represents a position the multiarray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/subscript(_:)-2hh91)*