# MPSGetCustomKernelMaxBatchSize(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func  
**Role**: Function

Returns the maximum allowed batch size.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MPSGetCustomKernelMaxBatchSize(_ c: MPSCustomKernelArgumentCount, _ MPSMaxTextures: UInt) -> UInt
```

```c
static unsigned long MPSGetCustomKernelMaxBatchSize(MPSCustomKernelArgumentCount c, unsigned long MPSMaxTextures);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsgetcustomkernelmaxbatchsize(_:_:))*