# blendingState

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Configure the blend state for color attachments the pipeline state uses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var blendingState: MTL4BlendState { get set }
```

```objc
@property (nonatomic) MTL4BlendState blendingState;
```

## Discussion

This property’s default value is [`MTL4BlendState.disabled`](../mtl4blendstate/disabled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptor/blendingstate)*