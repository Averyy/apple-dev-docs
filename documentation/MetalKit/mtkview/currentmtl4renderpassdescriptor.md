# currentMTL4RenderPassDescriptor

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var currentMTL4RenderPassDescriptor: MTL4RenderPassDescriptor? { get }
```

```objc
@property (nonatomic, readonly, nullable) MTL4RenderPassDescriptor * currentMTL4RenderPassDescriptor;
```

#### Discussion

A render pass descriptor generated from the currentDrawable’s texture and the view’s depth, stencil, and sample buffers and clear values.

This is a convience property.  The view does not use this descriptor and there is no requirement for an app to use this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/currentmtl4renderpassdescriptor)*