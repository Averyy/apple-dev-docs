# encode(to:primarySourceArray:secondarySourceArray:sourceGradient:gradientState:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to cmdBuf: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient gradient: MPSNDArray, gradientState state: MPSState) -> MPSNDArray
```

```objc
- (MPSNDArray *) encodeToCommandBuffer:(id<MTLCommandBuffer>) cmdBuf primarySourceArray:(MPSNDArray *) primarySourceArray secondarySourceArray:(MPSNDArray *) secondarySourceArray sourceGradient:(MPSNDArray *) gradient gradientState:(MPSState *) state;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarysecondarygradientkernel/encode(to:primarysourcearray:secondarysourcearray:sourcegradient:gradientstate:))*