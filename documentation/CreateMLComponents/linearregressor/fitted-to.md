# fitted(to:)

**Framework**: Create ML Components  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func fitted<Input>(to input: Input) async throws -> Self.Transformer where Input : Sequence, Input.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/fitted(to:))*