# rawValue

**Framework**: Create ML  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
let rawValue: Int
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```

## See Also

- [init()](mlimageclassifier/imageaugmentationoptions/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](mlimageclassifier/imageaugmentationoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init<S>(S)](mlimageclassifier/imageaugmentationoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(rawValue: Int)](mlimageclassifier/imageaugmentationoptions/init(rawvalue:).md)
  Creates an augmentation set with the given raw value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/rawvalue-swift.property)*