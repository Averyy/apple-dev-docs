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
func fitted<S>(to input: S) async throws -> Self.Transformer where S : Sequence, S.Element == Self.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler/fitted(to:))*