# init(scalars:shape:)

**Framework**: Core ML  
**Kind**: init

Initialize with a sequence and the shape.

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
init<S>(scalars: S, shape: [Int]) where Scalar == S.Element, S : Sequence
```

#### Discussion

The length of the sequence must not be less than the number of scalars in the shaped array.

## Parameters

- `scalars`: The initializing sequence.
- `shape`: The shape

## See Also

- [init(scalar: Scalar)](mlshapedarray/init(scalar:).md)
  Creates a shaped array with exactly one value and zero dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/init(scalars:shape:))*