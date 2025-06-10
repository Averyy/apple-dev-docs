# set(_:)

**Framework**: RealityKit  
**Kind**: method

Updates a blend shape weights data instance in the set based on its name. If blend shape weights data with this ID does not exist, does nothing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@discardableResult
mutating func set(_ newValue: BlendShapeWeightsSet.Element) -> BlendShapeWeightsSet.Element?
```

#### Return Value

The previous pose value, if named pose exists. nil otherwise.

## Parameters

- `newValue`: The blend shape weights data to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightsset/set(_:))*