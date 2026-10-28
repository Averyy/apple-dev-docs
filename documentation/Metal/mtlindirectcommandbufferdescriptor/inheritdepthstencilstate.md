# inheritDepthStencilState

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Configures whether the indirect command buffer inherits the depth stencil state from the encoder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var inheritDepthStencilState: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL inheritDepthStencilState;
```

## Discussion

The property’s default value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/inheritdepthstencilstate)*