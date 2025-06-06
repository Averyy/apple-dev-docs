# metadata

**Framework**: Link Presentation  
**Kind**: property

The metadata from which to generate a rich presentation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var metadata: LPLinkMetadata { get set }
```

#### Discussion

This can either be generated automatically from a URL by LPMetadataProvider, or manually constructed with the desired data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkview/metadata)*