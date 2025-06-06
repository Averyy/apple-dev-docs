# init(memberAnnotations:)

**Framework**: MapKit  
**Kind**: init

Creates a cluster annotation with the specified individual annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(memberAnnotations: [any MKAnnotation])
```

#### Return Value

An initialized [`MKClusterAnnotation`](mkclusterannotation.md) object or `nil` if the object could not be created.

## Parameters

- `memberAnnotations`: The annotations to group together as a single entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkclusterannotation/init(memberannotations:))*