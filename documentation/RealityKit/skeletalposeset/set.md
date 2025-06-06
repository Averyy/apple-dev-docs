# set(_:)

**Framework**: RealityKit  
**Kind**: method

Updates a pose in the set based on its name. If pose with this ID does not exist, does nothing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
mutating func set(_ newValue: SkeletalPoseSet.Element) -> SkeletalPoseSet.Element?
```

#### Return Value

The previous pose value, if named pose exists

## Parameters

- `newValue`: The pose to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposeset/set(_:))*