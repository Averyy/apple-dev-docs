# adaptedAsAnnotatedFeatureTransformer(annotationType:)

**Framework**: Create ML Components  
**Kind**: method

Returns an annotated-feature transformer that transforms the features using this transformer while leaving the annotations unchanged.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func adaptedAsAnnotatedFeatureTransformer<Annotation>(annotationType: Annotation.Type = Annotation.self) -> some Transformer<AnnotatedFeature<Self.Input, Annotation>, AnnotatedFeature<Self.Output, Annotation>>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imageexposureadjuster/adaptedasannotatedfeaturetransformer(annotationtype:))*