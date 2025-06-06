# buildEither(second:)

**Framework**: Swift Charts  
**Kind**: method

Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2> where T1 : AxisContent, T2 : AxisContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axiscontentbuilder/buildeither(second:))*