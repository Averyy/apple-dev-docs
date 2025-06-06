# init(_:)

**Framework**: RealityKit  
**Kind**: init

Initializes a collection of weights for a single blend shape.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init<S>(_ weights: S) where S : Sequence, S.Element == Float
```

## Parameters

- `weights`: An array of float weights for the blend shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweights/init(_:))*