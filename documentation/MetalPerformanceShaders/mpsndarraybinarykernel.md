# MPSNDArrayBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayBinaryKernel
```

```objc
@interface MPSNDArrayBinaryKernel : MPSNDArrayMultiaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](./mpsndarraybinarykernel/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsndarraybinarykernel/init%28device%29.md)
### Instance Properties
- [var primaryDilationRates: MPSNDArraySizes](./mpsndarraybinarykernel/primarydilationrates.md)
- [var primaryEdgeMode: MPSImageEdgeMode](./mpsndarraybinarykernel/primaryedgemode.md)
- [var primaryKernelSizes: MPSNDArraySizes](./mpsndarraybinarykernel/primarykernelsizes.md)
- [var primaryOffsets: MPSNDArrayOffsets](./mpsndarraybinarykernel/primaryoffsets.md)
- [var primaryStrides: MPSNDArrayOffsets](./mpsndarraybinarykernel/primarystrides.md)
- [var secondaryDilationRates: MPSNDArraySizes](./mpsndarraybinarykernel/secondarydilationrates.md)
- [var secondaryEdgeMode: MPSImageEdgeMode](./mpsndarraybinarykernel/secondaryedgemode.md)
- [var secondaryKernelSizes: MPSNDArraySizes](./mpsndarraybinarykernel/secondarykernelsizes.md)
- [var secondaryOffsets: MPSNDArrayOffsets](./mpsndarraybinarykernel/secondaryoffsets.md)
- [var secondaryStrides: MPSNDArrayOffsets](./mpsndarraybinarykernel/secondarystrides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray) -> MPSNDArray](./mpsndarraybinarykernel/encode%28to,primarysourcearray,secondarysourcearray%29.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, destinationArray: MPSNDArray)](./mpsndarraybinarykernel/encode%28to,primarysourcearray,secondarysourcearray,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](./mpsndarraybinarykernel/encode%28to,primarysourcearray,secondarysourcearray,resultstate,destinationarray%29.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](./mpsndarraybinarykernel/encode%28to,primarysourcearray,secondarysourcearray,resultstate,outputstateistemporary%29.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](./mpsndarraymultiarykernel.md)
### Inherited By
- [MPSNDArrayGather](./mpsndarraygather.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarykernel)*