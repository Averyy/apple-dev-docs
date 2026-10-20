# encode(to:sourceArrays:resultState:outputStateIsTemporary:)

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
func encode(to cmdBuf: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState outGradientState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray
```

```objc
- (MPSNDArray *) encodeToCommandBuffer:(id<MTLCommandBuffer>) cmdBuf sourceArrays:(NSArray<MPSNDArray *> *) sourceArrays resultState:(MPSState **) outGradientState outputStateIsTemporary:(BOOL) outputStateIsTemporary;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel/encode(to:sourcearrays:resultstate:outputstateistemporary:))*