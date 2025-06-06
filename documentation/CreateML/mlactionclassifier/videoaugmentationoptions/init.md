# init(_:)

**Framework**: Create ML  
**Kind**: init

Creates a new set from a finite sequence of items.

**Availability**:
- macOS 10.14+

## Declaration

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```None
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## Parameters

- `sequence`: The elements to use as members of the new set.

## See Also

- [init(rawValue: Int)](mlactionclassifier/videoaugmentationoptions/init(rawvalue:).md)
  Creates a video augmentation option set from a raw value.
- [init()](mlactionclassifier/videoaugmentationoptions/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](mlactionclassifier/videoaugmentationoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/init(_:))*