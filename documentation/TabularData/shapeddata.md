# ShapedData

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

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
- [init(shape: [Int], strides: [Int], contents: [Element])](./shapeddata/init%28shape,strides,contents%29.md)
  Creates a multidimensional shaped array from a one-dimensional array.
### Instance Properties
- [let contents: [Element]](./shapeddata/contents.md)
  A linear array that stores the elements of the multidimensional array.
- [let shape: [Int]](./shapeddata/shape.md)
  An integer array that stores the size of each dimension in the corresponding element.
- [let strides: [Int]](./shapeddata/strides.md)
  An integer array that stores the number of memory locations that span the length of each dimension in the corresponding element.
### Subscripts
- [subscript(Int...) -> Element](./shapeddata/subscript%28_%29.md)
  Retrieves an element using an index for each dimension.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Data Frame from Turi Create Types
- [init(contentsOfSFrameDirectory: URL, columns: [String]?, rows: Range<Int>?) throws](./dataframe/init%28contentsofsframedirectory,columns,rows%29.md)
  Creates a data frame from a Turi Create scalable data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/shapeddata)*