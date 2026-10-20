# MTLSizeMake(_:_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Creates a size instance with values for its width, height, and depth properties.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTLSizeMake(_ width: Int, _ height: Int, _ depth: Int) -> MTLSize
```

```c
static MTLSize MTLSizeMake(NSUInteger width, NSUInteger height, NSUInteger depth);
```

## Parameters

- `width`: A value for the x-axis dimension.
- `height`: A value for the y-axis dimension. Pass `1` for sizes with one dimension.
- `depth`: A value for the z-axis dimension. Pass `1` for sizes with one or two dimensions.

## See Also

### Creating a size instance
- [init()](./mtlsize/init%28%29.md)
  Creates a default size instance by setting the initial values for its width, height, and depth properties to zero.
- [init(width: Int, height: Int, depth: Int)](./mtlsize/init%28width,height,depth%29.md)
  Creates a size instance with values for its width, height, and depth properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsizemake(_:_:_:))*