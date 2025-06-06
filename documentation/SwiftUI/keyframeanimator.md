# KeyframeAnimator

**Framework**: SwiftUI  
**Kind**: struct

A container that animates its content with keyframes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct KeyframeAnimator<Value, KeyframePath, Content> where Value == KeyframePath.Value, KeyframePath : Keyframes, Content : View
```

#### Overview

The `content` closure updates every frame while animating, so avoid performing any expensive operations directly within `content`.

## Topics

### Creating a phase animator
- [init(initialValue: Value, repeating: Bool, content: (Value) -> Content, keyframes: (Value) -> KeyframePath)](keyframeanimator/init(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [init(initialValue: Value, trigger: some Equatable, content: (Value) -> Content, keyframes: (Value) -> KeyframePath)](keyframeanimator/init(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [protocol Keyframes](keyframes.md)
  A type that defines changes to a value over time.
- [struct KeyframeTimeline](keyframetimeline.md)
  A description of how a value changes over time, modeled using keyframes.
- [struct KeyframeTrack](keyframetrack.md)
  A sequence of keyframes animating a single property of a root type.
- [struct KeyframeTrackContentBuilder](keyframetrackcontentbuilder.md)
  The builder that creates keyframe track content from the keyframes that you define within a closure.
- [struct KeyframesBuilder](keyframesbuilder.md)
  A builder that combines keyframe content values into a single value.
- [protocol KeyframeTrackContent](keyframetrackcontent.md)
  A group of keyframes that define an interpolation curve of an animatable value.
- [struct CubicKeyframe](cubickeyframe.md)
  A keyframe that uses a cubic curve to smoothly interpolate between values.
- [struct LinearKeyframe](linearkeyframe.md)
  A keyframe that uses simple linear interpolation.
- [struct MoveKeyframe](movekeyframe.md)
  A keyframe that immediately moves to the given value without interpolating.
- [struct SpringKeyframe](springkeyframe.md)
  A keyframe that uses a spring function to interpolate to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframeanimator)*