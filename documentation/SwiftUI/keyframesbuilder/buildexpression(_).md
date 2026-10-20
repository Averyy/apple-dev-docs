# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Keyframes

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
static func buildExpression<Content>(_ expression: Content) -> Content where Value == Content.Value, Content : Keyframes
```

**Other overloads**:

```swift
static func buildExpression<K>(_ expression: K) -> K where Value == K.Value, K : KeyframeTrackContent
```

## See Also

### Building keyframes
- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](./buildarray%28_%29.md)
- [static buildBlock()](./buildblock%28%29.md)
- [static func buildEither<First, Second>(first: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./buildeither%28first%29.md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](./buildeither%28second%29.md)
- [static buildFinalResult(_:)](./buildfinalresult%28_%29.md)
- [static buildPartialBlock(accumulated:next:)](./buildpartialblock%28accumulated,next%29.md)
- [static buildPartialBlock(first:)](./buildpartialblock%28first%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildexpression(_:))*