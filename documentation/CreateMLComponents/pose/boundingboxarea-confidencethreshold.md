# boundingBoxArea(confidenceThreshold:)

**Framework**: Create ML Components  
**Kind**: method

Computes the bounding box area of the pose.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func boundingBoxArea(confidenceThreshold: Float = 0.2) -> Float
```

## Parameters

- `confidenceThreshold`: A threshold confidence between 0 to 1 for the keypoints to be considered valid to compute the bounding box area. The default value is 0.2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pose/boundingboxarea(confidencethreshold:))*