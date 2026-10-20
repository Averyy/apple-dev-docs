# buildPartialBlock(first:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
static func buildPartialBlock<Content>(first: Content) -> Content where Value == Content.Value, Content : Keyframes
```

**Other overloads**:

```swift
static func buildPartialBlock<K>(first: K) -> K where Value == K.Value, K : KeyframeTrackContent
```

## See Also

### Building keyframes
- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](./buildarray%28_%29.md)
- [static buildBlock()](./buildblock%28%29.md)
- [static func buildEither<First, Second>(first: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./buildeither%28first%29.md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./buildeither%28second%29.md)
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Keyframes
- [static buildFinalResult(_:)](./buildfinalresult%28_%29.md)
- [static buildPartialBlock(accumulated:next:)](./buildpartialblock%28accumulated,next%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildpartialblock(first:))*