# rawValue

**Framework**: RealityKit  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

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

- [init()](arview/entitygestures/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/entitygestures/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/entitygestures/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.EntityGestures.Element](arview/entitygestures/element.md)
  The element type of the option set.
- [ARView.EntityGestures.ArrayLiteralElement](arview/entitygestures/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/entitygestures/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [ARView.EntityGestures.RawValue](arview/entitygestures/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures/rawvalue-swift.property)*