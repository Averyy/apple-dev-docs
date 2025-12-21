# dependsOnOthers

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample depends on other samples for decoding.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var dependsOnOthers: Bool? { get set }
```

#### Discussion

This key has no default value. If this key is not present, dependency information for the sample is unknown. A value of false indicates that the sample does not depend on other samples (for example, an I frame). A value of true indicates that the sample does depend on other samples (for example, a P or B frame).

This attachment is read from and written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/dependsonothers)*