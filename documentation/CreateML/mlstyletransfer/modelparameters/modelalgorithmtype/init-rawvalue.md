# init(rawValue:)

**Framework**: Create ML  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(rawValue: String)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

print(PaperSize(rawValue: "Legal"))
// Prints "Optional(PaperSize.Legal)"

print(PaperSize(rawValue: "Tabloid"))
// Prints "nil"
```

## Parameters

- `rawValue`: The raw value to use for the new instance.

## See Also

- [var rawValue: String](mlstyletransfer/modelparameters/modelalgorithmtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType.RawValue](mlstyletransfer/modelparameters/modelalgorithmtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/modelalgorithmtype/init(rawvalue:))*