# SCSensitivityAnalysis.ContentType

**Framework**: Sensitive Content Analysis  
**Kind**: struct  
**Role**: Structure

A type that identifies a category of sensitive content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ContentType
```

```c
typedef NSString * SCSensitiveContentType;
```

## Discussion

The Sensitive Content Analysis framework uses content type values to indicate the specific nature of sensitive material detected in images or videos. Check the [`detectedTypes`](./detectedtypes.md) property to retrieve the set of content types the framework detects in analyzed media. This information enables your app to provide tailored responses based on the specific type of sensitive content present.

## Topics

### Identifying content categories
- [static let sexuallyExplicit: SCSensitivityAnalysis.ContentType](./contenttype/sexuallyexplicit.md)
  A content type that indicates the presence of nudity or sexually explicit material.
- [static let goreOrViolence: SCSensitivityAnalysis.ContentType](./contenttype/goreorviolence.md)
  A content type that indicates the presence of graphic violence or gore.
### Creating a content type
- [init(rawValue: String)](./contenttype/init%28rawvalue%29.md)
  Creates a content type from a raw string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying content categories
- [var detectedTypes: Set<SCSensitivityAnalysis.ContentType>](./detectedtypes.md)
  A property that contains the categories of sensitive content that analysis detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/contenttype)*