# forwardProgressUsage

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A forward progress strategy the framework applies to the pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var forwardProgressUsage: MTLForwardProgressUsage { get }
```

```objc
@property (readonly) MTLForwardProgressUsage forwardProgressUsage;
```

## Discussion

When you create the pipeline with a [`forwardProgressUsage`](../mtlcomputepipelinedescriptor/forwardprogressusage.md) value of [`MTLForwardProgressUsage.automatic`](../mtlforwardprogressusage/automatic.md), this property reflects the usage mode the framework selects. Otherwise, the property reflects the descriptor’s value at the time you create the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/forwardprogressusage)*