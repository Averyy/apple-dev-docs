# preferredSurroundingsEffect(_:)

**Framework**: Appintents  
**Kind**: method

Applies an effect to passthrough video.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some View
```

#### Return Value

A view that exhibits the specified preference.

#### Discussion

Use this modifier to indicate a preference for the appearance of passthrough video when displaying the modified view. For example, you can enhance the immersiveness of a scene that uses the default `ImmersionStyle/mixed` immersion style by applying the `SurroundingsEffect/systemDark` preference to a view inside the scene:

```swift
ImmersiveSpace(id: "orbit") {
    Orbit()
        .preferredSurroundingsEffect(.dark)
}
```

When the system presents the `Orbit` view in the above code, it also dims passthrough video. This helps to draw attention to the scene’s virtual content while still enabling people to remain aware of their surroundings.

> **Note**: This modifier expresses a preference, but the system might not be able to honor it.

Use a value of `nil` to indicate that you have no preference. You typically do this to counteract a preference expressed by a view lower in the view hierarchy.

## Parameters

- `effect`: The effect that you want to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/preferredsurroundingseffect(_:))*