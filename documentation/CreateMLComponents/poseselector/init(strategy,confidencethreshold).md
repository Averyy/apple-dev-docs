# init(strategy:confidenceThreshold:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates a pose selector.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(strategy: PoseSelectionStrategy, confidenceThreshold: Float)
```

## Parameters

- `strategy`: The strategy used to choose a pose if multiple poses are detected on the same frame. Default strategy is to select a pose with maximum bounding box area.
- `confidenceThreshold`: A threshold confidence between 0 to 1 for the joints to be considered valid in pose selection. The default value is 0.2.

## See Also

### Creating a selector
- [init()](./init%28%29.md)
  Creates a pose selector.
- [init(strategy: PoseSelectionStrategy)](./init%28strategy%29.md)
  Creates a pose selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/poseselector/init(strategy:confidencethreshold:))*