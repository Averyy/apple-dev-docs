# init(width:height:depth:)

**Framework**: Metal  
**Kind**: init

Creates a size instance with values for its width, height, and depth properties.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(width: Int, height: Int, depth: Int)
```

## Parameters

- `width`: A value for the x-axis dimension.
- `height`: A value for the y-axis dimension.   Pass   for sizes with one dimension.
- `depth`: A value for the z-axis dimension.   Pass   for sizes with one or two dimensions.

## See Also

- [init()](mtlsize/init.md)
  Creates a default size instance by setting the initial values for its width, height, and depth properties to zero.
- [func MTLSizeMake(Int, Int, Int) -> MTLSize](mtlsizemake(_:_:_:).md)
  Creates a size instance with values for its width, height, and depth properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsize/init(width:height:depth:))*