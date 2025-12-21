# id

**Framework**: MapKit JS  
**Kind**: property

The place ID that references a place or a map feature.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get id(): string | undefined;
```

#### Discussion

This value is only available when you initialize an annotation with a [`Place`](place.md), or when the annotation is a [`MapFeatureAnnotation`](mapfeatureannotation.md)that the framework creates when someone selects a map feature with a place ID available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/id)*