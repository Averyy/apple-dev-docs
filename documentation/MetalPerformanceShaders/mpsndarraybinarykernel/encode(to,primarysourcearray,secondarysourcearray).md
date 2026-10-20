# encode(to:primarySourceArray:secondarySourceArray:)

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
func encode(to cmdBuf: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray) -> MPSNDArray
```

```objc
- (MPSNDArray *) encodeToCommandBuffer:(id<MTLCommandBuffer>) cmdBuf primarySourceArray:(MPSNDArray *) primarySourceArray secondarySourceArray:(MPSNDArray *) secondarySourceArray;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarykernel/encode(to:primarysourcearray:secondarysourcearray:))*