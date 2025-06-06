# init(data:shape:strides:)

**Framework**: Core ML  
**Kind**: init

Creates a shaped array from a block of data, a shape, and strides.

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

- `data`: The block of data that holds the contents of the shaped array.
- `shape`: The shape of the array.
- `strides`: The strides of the array.

## See Also

- [init(data: Data, shape: [Int])](mlshapedarray/init(data:shape:).md)
  Creates a shaped array from a block of data and a shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray/init(data:shape:strides:))*