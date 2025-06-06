# init(concatenating:alongAxis:)

**Framework**: Core ML  
**Kind**: init

Merges a sequence of shaped arrays into one shaped array along an axis.

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
init<S>(concatenating shapedArrays: S, alongAxis: Int) where Scalar == S.Element.Scalar, S : Sequence, S.Element : MLShapedArrayProtocol
```

#### Discussion

All shaped arrays in the sequence must have the following:

- The same underlying data type
- The same number of dimensions
- The same size for each corresponding dimension, except for the concatenation axis

For example, this code concatenates two shaped arrays along their second dimension:

```swift
// A 2x3 shaped array.
// 0 1 2
// 5 6 7
let shapedArray1 = MLShapedArray<Int32>(scalars: [0, 1, 2, 5, 6, 7],
                                        shape: [2, 3])

// A 2x2 shaped array.
// 3 4
// 8 9
let shapedArray2 = MLShapedArray<Int32>(scalars: [3, 4, 8, 9],
                                        shape: [2, 2])

// A 2x5 shaped array.
// 0 1 2 3 4
// 5 6 7 8 9
let shapedArray3 = MLShapedArray(concatenating: [shapedArray1,shapedArray2],
                                 alongAxis: 1)
```

## Parameters

- `alongAxis`: A zero-based axis number the shaped arrays in   merge along.

## See Also

- [init(MLMultiArray)](mlshapedarray/init(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/init(concatenating:alongaxis:))*