# mapFeatures(_:)

**Framework**: Create ML Components  
**Kind**: method

Returns an array containing the results of mapping the given async closure over the sequence’s features.

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
func mapFeatures<Input, Output, Annotation>(_ transform: (Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Output, Annotation>] where Self.Element == AnnotatedFeature<Input, Annotation>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/mapfeatures(_:)-33517)*