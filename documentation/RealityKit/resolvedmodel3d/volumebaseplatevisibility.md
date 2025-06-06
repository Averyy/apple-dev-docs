# volumeBaseplateVisibility(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func volumeBaseplateVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

The baseplate is a semi-transparent view that appears on the ‘floor’ of a volume.

Usage:

```None
WindowGroup() {
    Poker()
        .volumeBaseplateVisibility(.visible)
}
.windowStyle(.volumetric)
```

Defaults to `automatic` (visible).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/volumebaseplatevisibility(_:))*