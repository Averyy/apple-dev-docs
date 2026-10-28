# inheritDepthBias

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Configures whether the indirect command buffer inherits the depth bias from the encoder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var inheritDepthBias: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL inheritDepthBias;
```

## Discussion

The property’s default value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/inheritdepthbias)*