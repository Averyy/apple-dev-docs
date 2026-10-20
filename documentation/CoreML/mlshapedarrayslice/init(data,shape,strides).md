# init(data:shape:strides:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a shaped array with defined data, shape, and strides.

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
init(data: Data, shape: [Int], strides: [Int])
```

## Parameters

- `data`: A block of data that initializes the array.
- `shape`: The shape of the array.
- `strides`: The strides of the array.

## See Also

### Creating a shaped array slice with data
- [init(data: Data, shape: [Int])](./init%28data,shape%29.md)
  Creates a shaped array with a defined data and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice/init(data:shape:strides:))*