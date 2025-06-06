# mapAnnotations(_:)

**Framework**: Swift  
**Kind**: method

Returns a lazy sequence where the elements of the result are computed each time they are read by calling transform function on the annotation of an annotated feature.

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
func mapAnnotations<Feature, Input, Output>(_ transform: @escaping (Input) -> Output) -> LazyMapSequence<Base, AnnotatedFeature<Feature, Output>> where Base.Element == AnnotatedFeature<Feature, Input>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence/mapannotations(_:))*