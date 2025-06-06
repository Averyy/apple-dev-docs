# buildEither(first:)

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
static func buildEither<First, Second>(first component: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second> where Value == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value
```

## See Also

- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](keyframesbuilder/buildarray(_:).md)
- [static buildBlock()](keyframesbuilder/buildblock.md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](keyframesbuilder/buildeither(second:).md)
- [static buildExpression(_:)](keyframesbuilder/buildexpression(_:).md)
  Keyframes
- [static buildFinalResult(_:)](keyframesbuilder/buildfinalresult(_:).md)
- [static buildPartialBlock(accumulated:next:)](keyframesbuilder/buildpartialblock(accumulated:next:).md)
- [static buildPartialBlock(first:)](keyframesbuilder/buildpartialblock(first:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildeither(first:))*