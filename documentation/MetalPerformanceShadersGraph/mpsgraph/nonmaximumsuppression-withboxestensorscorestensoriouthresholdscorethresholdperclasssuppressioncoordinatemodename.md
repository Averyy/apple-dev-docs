# nonMaximumSuppression(withBoxesTensor:scoresTensor:iouThreshold:scoreThreshold:perClassSuppression:coordinateMode:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a nonMaximumumSuppression operation and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func nonMaximumSuppression(withBoxesTensor boxesTensor: MPSGraphTensor, scoresTensor: MPSGraphTensor, iouThreshold IOUThreshold: Float, scoreThreshold: Float, perClassSuppression: Bool, coordinateMode: MPSGraphNonMaximumSuppressionCoordinateMode, name: String?) -> MPSGraphTensor
```

## Parameters

- `boxesTensor`: A tensor containing the coordinates of the input boxes. Must be a rank 3 tensor of shape [N,B,4] of type 
- `scoresTensor`: A tensor containing the scores of the input boxes. Must be a rank 3 tensor of shape [N,B,K] of type 
- `IOUThreshold`: The threshold for when to reject boxes based on their Intersection Over Union. Valid range is [0,1].
- `scoreThreshold`: The threshold for when to reject boxes based on their score, before IOU suppression.
- `perClassSuppression`: When this is specified a box will only suppress another box if they have the same class.
- `coordinateMode`: The coordinate mode the box coordinates are provided in.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/nonmaximumsuppression(withboxestensor:scorestensor:iouthreshold:scorethreshold:perclasssuppression:coordinatemode:name:))*