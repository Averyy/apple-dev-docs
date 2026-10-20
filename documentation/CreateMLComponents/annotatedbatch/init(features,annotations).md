# init(features:annotations:)

**Framework**: Create ML Components  
**Kind**: init

Creates an annotated batch.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(features: MLShapedArray<Scalar>, annotations: MLShapedArray<Scalar>)
```

#### Discussion

The features and annotations must have the same rank, and the first dimensions must be equal.

## Parameters

- `features`: A shaped array of features.
- `annotations`: A shaped array of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedbatch/init(features:annotations:))*