# init(shape:strides:contents:)

**Framework**: TabularData  
**Kind**: init

Creates a multidimensional shaped array from a one-dimensional array.

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
init(shape: [Int], strides: [Int], contents: [Element])
```

## Parameters

- `shape`: An integer array that stores the size of each dimension in the corresponding element.
- `strides`: An integer array that stores the number of memory locations   that span the length of each dimension in the corresponding element.
- `contents`: A linear array that stores the elements of the multidimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/shapeddata/init(shape:strides:contents:))*