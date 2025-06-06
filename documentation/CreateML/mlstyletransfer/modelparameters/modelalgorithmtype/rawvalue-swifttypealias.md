# MLStyleTransfer.ModelParameters.ModelAlgorithmType.RawValue

**Framework**: Create ML  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
typealias RawValue = String
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [init?(rawValue: String)](mlstyletransfer/modelparameters/modelalgorithmtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: String](mlstyletransfer/modelparameters/modelalgorithmtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/modelalgorithmtype/rawvalue-swift.typealias)*