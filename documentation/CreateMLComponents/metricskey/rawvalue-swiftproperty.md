# rawValue

**Framework**: Create ML Components  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var rawValue: String
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

- [static let source: MetricsKey](metricskey/source.md)
  A key associated with a temporal stream source (e.g. a file name).
- [static let trainingAccuracy: MetricsKey](metricskey/trainingaccuracy.md)
  A key associated with a training accuracy metric.
- [static let trainingError: MetricsKey](metricskey/trainingerror.md)
  A key associated with a training error metric.
- [static let trainingLoss: MetricsKey](metricskey/trainingloss.md)
  A key associated with a training loss metric.
- [static let trainingMaximumError: MetricsKey](metricskey/trainingmaximumerror.md)
  A key associated with a training maximum error metric.
- [static let trainingMeanAveragePrecision: MetricsKey](metricskey/trainingmeanaverageprecision.md)
  A key associated with a training mean average precision metric.
- [static let validationAccuracy: MetricsKey](metricskey/validationaccuracy.md)
  A key associated with a validation accuracy metric.
- [static let validationError: MetricsKey](metricskey/validationerror.md)
  A key associated with a validation error metric.
- [static let validationLoss: MetricsKey](metricskey/validationloss.md)
  A key associated with a validation loss metric.
- [static let validationMaximumError: MetricsKey](metricskey/validationmaximumerror.md)
  A key associated with a validation maximum error metric.
- [static let validationMeanAveragePrecision: MetricsKey](metricskey/validationmeanaverageprecision.md)
  A key associated with a validation mean average precision metric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/metricskey/rawvalue-swift.property)*