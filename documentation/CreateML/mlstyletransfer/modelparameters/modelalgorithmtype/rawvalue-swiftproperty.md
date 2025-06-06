# rawValue

**Framework**: Create ML  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var rawValue: String { get }
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

- [init?(rawValue: String)](mlstyletransfer/modelparameters/modelalgorithmtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType.RawValue](mlstyletransfer/modelparameters/modelalgorithmtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/modelalgorithmtype/rawvalue-swift.property)*