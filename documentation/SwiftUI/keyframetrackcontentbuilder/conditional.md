# KeyframeTrackContentBuilder.Conditional

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A conditional result from the result builder.

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
struct Conditional<ConditionalValue, First, Second> where ConditionalValue == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value
```

Available when `Value` conforms to `Animatable`.

## Relationships

### Conforms To
- [KeyframeTrackContent](../keyframetrackcontent.md)

## See Also

### Building keyframe track content
- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](./buildarray%28_%29.md)
- [static func buildBlock() -> some KeyframeTrackContent<Value>
](./buildblock%28%29.md)
- [static func buildEither<First, Second>(first: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./buildeither%28first%29.md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./buildeither%28second%29.md)
- [static func buildExpression<K>(K) -> K](./buildexpression%28_%29.md)
- [static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>, next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value>
](./buildpartialblock%28accumulated,next%29.md)
- [static func buildPartialBlock<K>(first: K) -> K](./buildpartialblock%28first%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframetrackcontentbuilder/conditional)*