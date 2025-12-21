# CMSampleBuffer.MultiSampleContent

**Framework**: Core Media  
**Kind**: protocol

This is a marker protocol to indicate content that supports multiple samples.

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
protocol MultiSampleContent : CMSampleBuffer.Content
```

## Relationships

### Inherits From
- [CMSampleBuffer.Content](cmsamplebuffer/content.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer.md)
- [CMSampleBuffer.DynamicContent](cmsamplebuffer/dynamiccontent.md)
- [CMSampleDataReference](cmsampledatareference.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/multisamplecontent)*