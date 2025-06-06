# MTLSizeMake(_:_:_:)

**Framework**: Metal  
**Kind**: func

Creates a size for an object using the specified dimensions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func MTLSizeMake(_ width: Int, _ height: Int, _ depth: Int) -> MTLSize
```

#### Return Value

The specified size of an object.

## Parameters

- `width`: The width of the object.
- `height`: The height of the object. Set to   if the object only has one dimension.
- `depth`: The depth of the object. Set to   if the object has one or two dimensions.

## See Also

- [init()](mtlsize/init.md)
  Initializes a box size.
- [init(width: Int, height: Int, depth: Int)](mtlsize/init(width:height:depth:).md)
  Initializes a size for an object with the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsizemake(_:_:_:))*