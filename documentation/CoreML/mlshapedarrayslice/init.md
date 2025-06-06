# init(_:)

**Framework**: Core ML  
**Kind**: init

Creates a new MLShapedArraySlice using a `MLMultiArray` as a backing storage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init(_ multiArray: MLMultiArray)
```

#### Discussion

Use this initializer to access `MLMultiArray` through `MLShapedArray` interface.

Mutating operations trigger copy-on-write. Non-mutating operations access the `MLMultiArray`’s backing storage including the pixel buffer.

## Parameters

- `multiArray`: The   object.

## See Also

- [init<S>(concatenating: S, alongAxis: Int)](mlshapedarrayslice/init(concatenating:alongaxis:).md)
  Merges a sequence of shaped arrays into one shaped array along an axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/init(_:))*