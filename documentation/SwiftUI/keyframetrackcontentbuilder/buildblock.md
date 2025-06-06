# buildBlock()

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
static func buildBlock() -> some KeyframeTrackContent<Value>
```

## See Also

- [static func buildArray([some KeyframeTrackContent<Value>]) -> some KeyframeTrackContent<Value>
](keyframetrackcontentbuilder/buildarray(_:).md)
- [static func buildEither<First, Second>(first: First) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](keyframetrackcontentbuilder/buildeither(first:).md)
- [static func buildEither<First, Second>(second: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second>](keyframetrackcontentbuilder/buildeither(second:).md)
- [static func buildExpression<K>(K) -> K](keyframetrackcontentbuilder/buildexpression(_:).md)
- [static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>, next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value>
](keyframetrackcontentbuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock<K>(first: K) -> K](keyframetrackcontentbuilder/buildpartialblock(first:).md)
- [KeyframeTrackContentBuilder.Conditional](keyframetrackcontentbuilder/conditional.md)
  A conditional result from the result builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframetrackcontentbuilder/buildblock())*