# CubicKeyframe

**Framework**: SwiftUI  
**Kind**: struct

A keyframe that uses a cubic curve to smoothly interpolate between values.

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
struct CubicKeyframe<Value> where Value : Animatable
```

#### Overview

If you don’t specify a start or end velocity, SwiftUI automatically computes a curve that maintains smooth motion between keyframes.

Adjacent cubic keyframes result in a Catmull-Rom spline.

If a cubic keyframe follows a different type of keyframe, such as a linear keyframe, the end velocity of the segment defined by the previous keyframe will be used as the starting velocity.

Likewise, if a cubic keyframe is followed by a different type of keyframe, the initial velocity of the next segment is used as the end velocity of the segment defined by this keyframe.

## Topics

### Creating the keyframe
- [init(Value, duration: TimeInterval, startVelocity: Value?, endVelocity: Value?)](cubickeyframe/init(_:duration:startvelocity:endvelocity:).md)
  Creates a new keyframe using the given value and timestamp.

## Relationships

### Conforms To
- [KeyframeTrackContent](keyframetrackcontent.md)

## See Also

- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](view/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [struct KeyframeAnimator](keyframeanimator.md)
  A container that animates its content with keyframes.
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
- [struct LinearKeyframe](linearkeyframe.md)
  A keyframe that uses simple linear interpolation.
- [struct MoveKeyframe](movekeyframe.md)
  A keyframe that immediately moves to the given value without interpolating.
- [struct SpringKeyframe](springkeyframe.md)
  A keyframe that uses a spring function to interpolate to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/cubickeyframe)*