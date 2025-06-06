# buildPartialBlock(first:)

**Framework**: SwiftUI  
**Kind**: method

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

## See Also

- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](keyframesbuilder/buildarray(_:).md)
- [static buildBlock()](keyframesbuilder/buildblock.md)
- [static func buildEither<First, Second>(first: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](keyframesbuilder/buildeither(first:).md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](keyframesbuilder/buildeither(second:).md)
- [static buildExpression(_:)](keyframesbuilder/buildexpression(_:).md)
  Keyframes
- [static buildFinalResult(_:)](keyframesbuilder/buildfinalresult(_:).md)
- [static buildPartialBlock(accumulated:next:)](keyframesbuilder/buildpartialblock(accumulated:next:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildpartialblock(first:))*