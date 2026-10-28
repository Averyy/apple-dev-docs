# sexuallyExplicit

**Framework**: Sensitive Content Analysis  
**Kind**: property  
**Role**: Type Property

A content type that indicates the presence of nudity or sexually explicit material.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let sexuallyExplicit: SCSensitivityAnalysis.ContentType
```

```c
extern SCSensitiveContentType const SCSensitiveContentTypeSexuallyExplicit;
```

## Mentions

- [Testing your app’s response to sensitive media](../../testing-your-app-s-response-to-sensitive-media.md)

## Discussion

The Sensitive Content Analysis framework includes this value in [`detectedTypes`](../detectedtypes.md) when it detects nudity or sexually explicit content in analyzed media.

## See Also

### Identifying content categories
- [static let goreOrViolence: SCSensitivityAnalysis.ContentType](./goreorviolence.md)
  A content type that indicates the presence of graphic violence or gore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/contenttype/sexuallyexplicit)*