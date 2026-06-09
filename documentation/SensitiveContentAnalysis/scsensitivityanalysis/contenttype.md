# SCSensitivityAnalysis.ContentType

**Framework**: Sensitive Content Analysis  
**Kind**: struct

A type that identifies a category of sensitive content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ContentType
```

#### Discussion

The Sensitive Content Analysis framework uses content type values to indicate the specific nature of sensitive material detected in images or videos. Check the [`detectedTypes`](scsensitivityanalysis/detectedtypes.md) property to retrieve the set of content types the framework detects in analyzed media. This information enables your app to provide tailored responses based on the specific type of sensitive content present.

## Topics

### Identifying content categories
- [static let sexuallyExplicit: SCSensitivityAnalysis.ContentType](scsensitivityanalysis/contenttype/sexuallyexplicit.md)
  A content type that indicates the presence of nudity or sexually explicit material.
- [static let goreOrViolence: SCSensitivityAnalysis.ContentType](scsensitivityanalysis/contenttype/goreorviolence.md)
  A content type that indicates the presence of graphic violence or gore.
### Creating a content type
- [init(rawValue: String)](scsensitivityanalysis/contenttype/init(rawvalue:).md)
  Creates a content type from a raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var detectedTypes: Set<SCSensitivityAnalysis.ContentType>](scsensitivityanalysis/detectedtypes.md)
  A property that contains the categories of sensitive content that analysis detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/contenttype)*