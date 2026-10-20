# KeyframeTrackContentBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The builder that creates keyframe track content from the keyframes that you define within a closure.

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
@resultBuilder
struct KeyframeTrackContentBuilder<Value> where Value : Animatable
```

## Topics

### Building keyframe track content
- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](./keyframetrackcontentbuilder/buildarray%28_%29.md)
- [static func buildBlock() -> some KeyframeTrackContent<Value>
](./keyframetrackcontentbuilder/buildblock%28%29.md)
- [static func buildEither<First, Second>(first: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./keyframetrackcontentbuilder/buildeither%28first%29.md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./keyframetrackcontentbuilder/buildeither%28second%29.md)
- [static func buildExpression<K>(K) -> K](./keyframetrackcontentbuilder/buildexpression%28_%29.md)
- [static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>, next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value>
](./keyframetrackcontentbuilder/buildpartialblock%28accumulated,next%29.md)
- [static func buildPartialBlock<K>(first: K) -> K](./keyframetrackcontentbuilder/buildpartialblock%28first%29.md)
- [KeyframeTrackContentBuilder.Conditional](./keyframetrackcontentbuilder/conditional.md)
  A conditional result from the result builder.

## See Also

### Creating keyframe-based animation
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](./view/keyframeanimator%28initialvalue,repeating,content,keyframes%29.md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](./view/keyframeanimator%28initialvalue,trigger,content,keyframes%29.md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [struct KeyframeAnimator](./keyframeanimator.md)
  A container that animates its content with keyframes.
- [protocol Keyframes](./keyframes.md)
  A type that defines changes to a value over time.
- [struct KeyframeTimeline](./keyframetimeline.md)
  A description of how a value changes over time, modeled using keyframes.
- [struct KeyframeTrack](./keyframetrack.md)
  A sequence of keyframes animating a single property of a root type.
- [struct KeyframesBuilder](./keyframesbuilder.md)
  A builder that combines keyframe content values into a single value.
- [protocol KeyframeTrackContent](./keyframetrackcontent.md)
  A group of keyframes that define an interpolation curve of an animatable value.
- [struct CubicKeyframe](./cubickeyframe.md)
  A keyframe that uses a cubic curve to smoothly interpolate between values.
- [struct LinearKeyframe](./linearkeyframe.md)
  A keyframe that uses simple linear interpolation.
- [struct MoveKeyframe](./movekeyframe.md)
  A keyframe that immediately moves to the given value without interpolating.
- [struct SpringKeyframe](./springkeyframe.md)
  A keyframe that uses a spring function to interpolate to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframetrackcontentbuilder)*