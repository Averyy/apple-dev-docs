# updatePrecisionRecallCurves(_:)

**Framework**: Create ML Components  
**Kind**: method

Updates the per-label precision-recall curve using the input data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
mutating func updatePrecisionRecallCurves(_ input: some Collection<AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>>) async throws
```

#### Discussion

Call this method before exporting to a Core ML Model and using Vision `VNCoreMLRequest` to make predictions.

## Parameters

- `input`: A collection of annotated examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel/updateprecisionrecallcurves(_:))*