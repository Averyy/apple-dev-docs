# ShapedData

**Framework**: TabularData  
**Kind**: struct

A collection type that represents multidimensional data in a data frame element.

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
struct ShapedData<Element>
```

## Topics

### Initializers
- [init(shape: [Int], strides: [Int], contents: [Element])](shapeddata/init(shape:strides:contents:).md)
  Creates a multidimensional shaped array from a one-dimensional array.
### Instance Properties
- [let contents: [Element]](shapeddata/contents.md)
  A linear array that stores the elements of the multidimensional array.
- [let shape: [Int]](shapeddata/shape.md)
  An integer array that stores the size of each dimension in the corresponding element.
- [let strides: [Int]](shapeddata/strides.md)
  An integer array that stores the number of memory locations that span the length of each dimension in the corresponding element.
### Subscripts
- [subscript(Int...) -> Element](shapeddata/subscript(_:).md)
  Retrieves an element using an index for each dimension.
### Default Implementations
- [Equatable Implementations](shapeddata/equatable-implementations.md)
- [Hashable Implementations](shapeddata/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(contentsOfSFrameDirectory: URL, columns: [String]?, rows: Range<Int>?) throws](dataframe/init(contentsofsframedirectory:columns:rows:).md)
  Creates a data frame from a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/shapeddata)*