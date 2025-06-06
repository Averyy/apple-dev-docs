# mapAnnotations(_:)

**Framework**: Create ML  
**Kind**: method

Returns an array containing the results of mapping the given closure over the sequence’s annotations.

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
func mapAnnotations<Feature, Input, Output>(_ transform: (Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>] where Self.Element == AnnotatedFeature<Feature, Input>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/columnnames-swift.struct/mapannotations(_:)-3lsnv)*