# goreOrViolence

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Type Property

A content type that indicates the presence of graphic violence or gore.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let goreOrViolence: SCSensitivityAnalysis.ContentType
```

```c
extern SCSensitiveContentType const SCSensitiveContentTypeGoreOrViolence;
```

## Discussion

The Sensitive Content Analysis framework includes this value in [`detectedTypes`](../detectedtypes.md) when it detects violent or disturbing imagery in analyzed media.

## See Also

### Identifying content categories
- [static let sexuallyExplicit: SCSensitivityAnalysis.ContentType](./sexuallyexplicit.md)
  A content type that indicates the presence of nudity or sexually explicit material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/contenttype/goreorviolence)*