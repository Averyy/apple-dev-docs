# mapFeatures(_:)

**Framework**: Create ML  
**Kind**: method

Returns an array containing the results of mapping the given closure over the sequence’s features.

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
func mapFeatures<Input, Output, Annotation>(_ transform: (Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>] where Self.Element == AnnotatedFeature<Input, Annotation>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype/mapfeatures(_:)-9ae38)*