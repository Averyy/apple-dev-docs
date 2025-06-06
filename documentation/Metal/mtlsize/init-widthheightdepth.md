# init(width:height:depth:)

**Framework**: Metal  
**Kind**: init

Initializes a size for an object with the specified dimensions.

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

- `width`: The width of the volume.
- `height`: The height of the volume. Set to   if the object only has one dimension.
- `depth`: The depth of the volume. Set to 1 if the object has one or two dimensions.

## See Also

- [init()](mtlsize/init.md)
  Initializes a box size.
- [func MTLSizeMake(Int, Int, Int) -> MTLSize](mtlsizemake(_:_:_:).md)
  Creates a size for an object using the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsize/init(width:height:depth:))*