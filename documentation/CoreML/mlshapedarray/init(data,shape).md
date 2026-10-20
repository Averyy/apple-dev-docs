# init(data:shape:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array from a block of data and a shape.

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
init(data: Data, shape: [Int])
```

Available when `Scalar` conforms to `MLShapedArrayScalar`.

## Parameters

- `data`: The block of data that holds the contents of the shaped array.
- `shape`: The shape of the array.

## See Also

### Creating a shaped array from data
- [init(data: Data, shape: [Int], strides: [Int])](./init%28data,shape,strides%29.md)
  Creates a shaped array from a block of data, a shape, and strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/init(data:shape:))*