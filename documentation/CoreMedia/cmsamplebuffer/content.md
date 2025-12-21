# CMSampleBuffer.Content

**Framework**: Core Media  
**Kind**: protocol

All buffer types that can be carried by sample buffer are marked by this protocol.

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
protocol Content : Sendable
```

#### Overview

Note: This protocol is a marker protocol sealed to CoreMedia framework. Any types outside of the CoreMedia framework that implement this protocol will cause precondition failures when passed to sample buffer methods.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [CMSampleBuffer.ContentWithFormatDescription](cmsamplebuffer/contentwithformatdescription.md)
- [CMSampleBuffer.MultiSampleContent](cmsamplebuffer/multisamplecontent.md)
### Conforming Types
- [CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer.md)
- [CMSampleBuffer.DynamicContent](cmsamplebuffer/dynamiccontent.md)
- [CMSampleDataReference](cmsampledatareference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/content)*