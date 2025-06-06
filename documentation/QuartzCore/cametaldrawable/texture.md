# texture

**Framework**: Core Animation  
**Kind**: property  
**Required**: Yes

A Metal texture object that contains the drawable’s contents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var texture: any MTLTexture { get }
```

#### Discussion

Use this object to configure a [`MTLRenderPipelineColorAttachmentDescriptor`](https://developer.apple.com/documentation/Metal/MTLRenderPipelineColorAttachmentDescriptor) object to render to the drawable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/texture)*