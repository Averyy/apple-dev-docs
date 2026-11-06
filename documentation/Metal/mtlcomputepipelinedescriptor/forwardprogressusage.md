# forwardProgressUsage

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A scheduling strategy for code that blocks across SIMD groups.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var forwardProgressUsage: MTLForwardProgressUsage { get set }
```

```objc
@property (nonatomic, readwrite) MTLForwardProgressUsage forwardProgressUsage;
```

## Discussion

Metal resolves scheduling automatically when either this value is [`MTLForwardProgressUsage.automatic`](../mtlforwardprogressusage/automatic.md) or the kernel’s `[[forward_progress_usage]]` attribute is `automatic`. When both are explicit, this property takes priority.

The default value is [`MTLForwardProgressUsage.automatic`](../mtlforwardprogressusage/automatic.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/forwardprogressusage)*