# buildEither(second:)

**Framework**: SwiftUI  
**Kind**: method

Produces content for a conditional statement in a multi-statement closure when the condition is false.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F> where V == T.Value, T : SliderTickContent, F : SliderTickContent, T.Body == F.Body
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickbuilder/buildeither(second:))*