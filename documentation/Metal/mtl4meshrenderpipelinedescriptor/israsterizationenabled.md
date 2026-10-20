# isRasterizationEnabled

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Determines whether the pipeline rasterizes primitives.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isRasterizationEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isRasterizationEnabled) BOOL rasterizationEnabled;
```

#### Discussion

By default, this value is [`true`](../../Swift/true.md), specifying that this pipeline rasterizes primitives. Set this property to [`false`](../../Swift/false.md) when you don’t provide a fragment shader function via function [`fragmentFunctionDescriptor`](./fragmentfunctiondescriptor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/israsterizationenabled)*