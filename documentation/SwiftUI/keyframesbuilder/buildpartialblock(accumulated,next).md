# buildPartialBlock(accumulated:next:)

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
static func buildPartialBlock(accumulated: some KeyframeTrackContent<Value>, next: some KeyframeTrackContent<Value>) -> some KeyframeTrackContent<Value>
```

**Other overloads**:

```swift
static func buildPartialBlock(accumulated: some Keyframes<Value>, next: some Keyframes<Value>) -> some Keyframes<Value>
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
- [static buildPartialBlock(first:)](./buildpartialblock%28first%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildpartialblock(accumulated:next:))*