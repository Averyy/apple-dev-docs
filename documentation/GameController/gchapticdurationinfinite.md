# GCHapticDurationInfinite

**Framework**: Game Controller  
**Kind**: var

An infinite duration for a haptics event.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let GCHapticDurationInfinite: Float
```

#### Discussion

Use this constant to create a [`CHHapticEvent`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEvent) object with an infinite duration. For example, create an infinite haptic event that you update in a loop to adjust a controller’s motor intensity.

## See Also

- [func createEngine(withLocality: GCHapticsLocality) -> CHHapticEngine?](gcdevicehaptics/createengine(withlocality:).md)
  Creates a haptics engine with the specified locality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gchapticdurationinfinite)*