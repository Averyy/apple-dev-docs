# extractLabels(from:)

**Framework**: Create ML Components  
**Kind**: method

Extracts all the labels from a list of annotations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func extractLabels(from annotations: [ObjectDetectionAnnotation<Label>]) -> Set<Label>
```

#### Return Value

A set of all the labels present in the annotations.

## Parameters

- `annotations`: A list of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionmetrics/extractlabels(from:))*